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

# The rule compiler will automatically infer an "everything else" clause at
# the end of each rule
_rule_definition = {
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

def _rulecompiler():
    # bring in the rule definitions
    global _rule_definition
    
    rulefuncs = []
    # read each rule definition
    for rule in _rule_definition:
        rulefuncs.insert(rule, [])
        # read each rule function definition
        for str in _rule_definition[rule]:
            str = "lambda count: " + str
            # compile the rule function and put it into the rule fns list
            rulefuncs[rule].append(eval(compile(str, '<string>', 'eval')))
        # for each rule, there's an implied "everything else" at the end
        rulefuncs[rule].append(lambda count: True)
        # convert to a tuple for immutability
        rulefuncs[rule] = tuple(rulefuncs[rule])
    # convert to a tuple for immutability
    return tuple(rulefuncs)

def explain(rule):
    """
    Returns a description of the expected word list for a rule.
    """
    global _rule_definition
    
    # special case rule 0, since there's no "else"
    if rule == 0:
        return ("everything",)
    
    try:
        return tuple(list(_rule_definition[rule]) + ["everything else"])
    except KeyError:
        raise RuleError("Invalid rule requested: {0}".format(rule))
    
def _getrules(rule, rule_funcs = _rulecompiler()):
    """
    Returns a tuple of functions which can be used to test a count and return the index of the correct word form
    """
    # maintenance note: _rulecompiler() is expensive and should only
    # be called once, that's why it's a default parameter
    return rule_funcs[rule]
    

def index(count, rule):
    """
    Determines the index into a wordlist for a particular count and rule.
    """
    try:
        ruleset = _getrules(rule)
    except IndexError:
        raise RuleError("Invalid rule requested: {0}".format(rule))
        
    for idx in range(len(ruleset)):
        if ruleset[idx](count):
            return idx
    
    # this should never happen because of the implied "everything else" at the
    # end of each rule
    raise RuleError("Could not locate a suitable rule function")

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