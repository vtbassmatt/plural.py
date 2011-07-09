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
    
def index(count, rule):
    """
    Determines the index into a wordlist for a particular count and rule.
    """
    # rule 0: only one form
    if rule == 0:
        return 0
    
    # rule 1: Germanic/English 2-forms (singular, plural)
    if rule == 1:
        if count == 1:
            return 0
        else:
            return 1
    
    # rule 2: Romance (0/1 singular, plural)
    if rule == 2:
        if count == 0 or count == 1:
            return 0
        else:
            return 1
    
    # rule 3: Latvian (0, ends in 1 other than 11, everything else)
    if rule == 3:
        if count == 0:
            return 0
        elif endsin1(count) and count != 11:
            return 1
        else:
            return 2

def expects(rule):
    """
    Returns a count and description of the expected word list for a rule.
    """
    if rule == 0:
        return ("everything",)
    
    if rule == 1:
        return ("is 1", "everything else")
    
    if rule == 2:
        return ("is 0 or 1", "everything else")
    
    if rule == 3:
        return ("is 0", "ends in 1, not 11", "everything else")

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