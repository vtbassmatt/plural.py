"""
An implementation of Mozilla's plural forms
https://developer.mozilla.org/en/Localization_and_Plurals
"""

def pluralize(wordlist, count, rule):
    """
    Determines the correct pluralization of a word.
    
    Expects a word list/tuple (in a particular order, depending on the rule),
    a count of things, and a rule to follow.
    """
    return wordlist[index(count, rule)]

# The rule compiler will automatically infer an "everything else" clause at the
# end of each ruleset
rule_definition = {
    # rule 0: Asian, only one form
    0: ( ),
    
    # rule 1: Germanic/English 2-forms (singular, plural)
    1: ("count == 1", ),
    
    # rule 2: Romance (0/1 singular, plural)
    2: ("count == 0 or count == 1", ),
    
    # rule 3: Latvian (0, ends in 1 other than 11, everything else)
    3: ("count == 0",
        "endsin1(count) and count != 11",),
    
    # rule 4: Scottish Gaelic (1/11, 2/12, 3-19, everything else)
    4: ("count == 1 or count == 11",
        "count == 2 or count == 12",
        "count >= 3 and count <= 19",),
}

def createrulefuncs():
    # bring in the rule definitions
    global rule_definition
    
    rulefuncs = []
    # read each ruleset
    for rule in rule_definition:
        rulefuncs.insert(rule, [])
        # read each rule
        for str in rule_definition[rule]:
            str = "lambda count: " + str
            # compile the rule and put it into the rule functions list
            rulefuncs[rule].append(eval(compile(str, '<string>', 'eval')))
        # for each ruleset, there's an implied "everything else" at the end
        rulefuncs[rule].append(lambda count: True)
        # convert to a tuple for immutability
        rulefuncs[rule] = tuple(rulefuncs[rule])
    # convert to a tuple for immutability
    return tuple(rulefuncs)

def expects(rule):
    """
    Returns a count and description of the expected word list for a rule.
    """
    # rule 0: only one form
    if rule == 0:
        return ("everything",)
    
    # rule 1: Germanic/English 2-forms (singular, plural)
    if rule == 1:
        return ("is 1", "everything else")
    
    # rule 2: Romance (0/1 singular, plural)
    if rule == 2:
        return ("is 0 or 1", "everything else")
    
    # rule 3: Latvian (0, ends in 1 other than 11, everything else)
    if rule == 3:
        return ("is 0", "ends in 1, not 11", "everything else")
    
    # rule 4: Scottish Gaelic (1/11, 2/12, 3-19, everything else)
    if rule == 4:
        return ("is 1 or 11", "is 2 or 12", "others between 3 and 19", "everything else")

def getrules(rule, rule_funcs = createrulefuncs()):
    """
    Returns a tuple of functions which can be used to test a count and return the index of the correct word form
    """
    # maintenance note: createrulefuncs() is expensive and should only
    # be called once, that's why it's a default parameter
    return rule_funcs[rule]
    

def index(count, rule):
    """
    Determines the index into a wordlist for a particular count and rule.
    """
    ruleset = getrules(rule)
    for idx in range(len(ruleset)):
        if ruleset[idx](count):
            return idx
    
    raise RuleError("Could not locate a suitable rule")

class RuleError(Exception):
    pass

def endsin(value, finaldigit):
    """
    Returns true if a particular value ends in a particular digit.
    """
    # ensure we're dealing with an integer
    if value % 1 != 0:
        raise TypeError("count should be an integer")
    
    # invert the sign of negative numbers
    if value < 0:
        value = value * -1
        
    # remove the 10s digit and up
    testdigit = value - ((value / 10) * 10)
    return testdigit == finaldigit

def endsin1(value):
    """
    Returns true if a value ends in 1.
    """
    return endsin(value, 1)