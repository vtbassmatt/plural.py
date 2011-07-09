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

def rulefunctions(rule):
    """
    Returns a tuple of functions which can be used to test a count and return the index of the correct word form
    """
    # rule 0: only one form
    if rule == 0:
        return (lambda count: True,)
        
    # rule 1: Germanic/English 2-forms (singular, plural)
    if rule == 1:
        return (lambda count: count == 1, lambda count: True)
        
    # rule 2: Romance (0/1 singular, plural)
    if rule == 2:
        return (lambda count: count == 0 or count == 1, lambda count: True)
        
    # rule 3: Latvian (0, ends in 1 other than 11, everything else)
    if rule == 3:
        return (lambda count: count == 0, lambda count: endsin1(count) and count != 11, lambda count: True)
        
    # rule 4: Scottish Gaelic (1/11, 2/12, 3-19, everything else)
    if rule == 4:
        return (lambda count: count == 1 or count == 11,
                lambda count: count == 2 or count == 12,
                lambda count: count >= 3 and count <= 19,
                lambda count: True)

def lc(body):
    return lambda count: body

def index(count, rule):
    """
    Determines the index into a wordlist for a particular count and rule.
    """
    ruleset = rulefunctions(rule)
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