"""An implementation of Mozilla's plural forms
https://developer.mozilla.org/en/Localization_and_Plurals

The public API consists of three methods:
- pluralize
- explain
- rulefor"""

def pluralize(wordlist, count, rule):
    """Determines the correct pluralization of a word.
    
    Expects a word list/tuple (in a particular order, depending on the rule),
    a count of things, and a rule to follow."""
    return wordlist[__index(count, rule)]

def explain(rule):
    """Returns a description of the expected word list for a rule."""

    # bring the rule defs into scope
    global __rule_definition
    
    # special case rule 0, since there's no "else" needed
    if rule == 0:
        return ("everything",)
    
    try:
        return tuple(list(__rule_definition[rule]) + ["everything else"])
    except KeyError:
        raise RuleError("Invalid rule requested: {0}".format(rule))
    
def rulefor(langcode):
    """Returns the rule for a particular language code
    
    Constructed from the languages given in the Mozilla document and the
    tool at http://rishida.net/utils/subtags/"""
    
    langcode = str.lower(langcode)
    
    # Asian (Chinese, Japanese, Korean, Vietnamese), Persian, Turkic/Altaic
    # (Turkish), Thai, Lao
    if langcode in ('zh','ja','ko','vi','fa','tr','th','lo'):
        return 0
    
    # Germanic (Danish, Dutch, English, Faroese, Frisian, German, Norwegian,
    # Swedish), Finno-Ugric (Estonian, Finnish, Hungarian), Language isolate
    # (Basque), Latin/Greek (Greek), Semitic (Hebrew), Romanic (Italian,
    # Portuguese, Spanish, Catalan)
    if langcode in ('da','nl','en','fo','fy','de','nb','nn','no','sv',
                    'et','fi','hu','eu','el','he','it','es','ca',
                    'pt','pt-pt','pt_pt'):
        return 1
    
    # Romanic (French, Brazilian Portuguese)
    if langcode in ('fr', 'pt_br', 'pt-br'):
        return 2
    
    # Baltic (Latvian)
    if langcode in ('lv',):
        return 3
    
    # Celtic (Scottish Gaelic)
    if langcode in ('gd',):
        return 4
    
    # Romanic (Romanian)
    if langcode in ('ro',):
        return 5
    
    # Baltic (Lithuanian)
    if langcode in ('lt',):
        return 6
    
    # Slavic (Croatian, Serbian, Russian, Ukrainian)
    if langcode in ('hr','sr','ru','uk'):
        return 7
    
    # Slavic (Slovak, Czech)
    if langcode in ('sk','cs'):
        return 8
    
    # Slavic (Polish)
    if langcode in ('pl',):
        return 9
    
    # Slavic (Slovenian, Sorbian)
    if langcode in ('sl','wen','dsb','hsb'):
        return 10
    
    # Celtic (Irish Gaeilge)
    if langcode in ('ga',):
        return 11
    
    # Semitic (Arabic)
    if langcode in ('ar',):
        return 12
    
    # Semitic (Maltese)
    if langcode in ('mt',):
        return 13
    
    # Slavic (Macedonian)
    if langcode in ('mk',):
        return 14
    
    # Icelandic 
    if langcode in ('is',):
        return 15

# The rule compiler will automatically infer an "everything else" clause at
# the end of each rule
__rule_definition = {
    # rule 0: Asian, only one form
    0: ( ),
    
    # rule 1: Germanic/English 2-forms (singular, plural)
    1: ("amount == 1", ),
    
    # rule 2: Romance (0/1 singular, plural)
    2: ("amount == 0 or amount == 1", ),
    
    # rule 3: Latvian (0, ends in 1 other than 11, everything else)
    3: ("amount == 0",
        "endsin1(amount) and amount != 11",),
    
    # rule 4: Scottish Gaelic (1/11, 2/12, 3-19, everything else)
    4: ("amount == 1 or amount == 11",
        "amount == 2 or amount == 12",
        "amount >= 3 and amount <= 19",),
    
    # rule 5: Romanian (1, 0 + 01-19, everything else)
    5: ("amount == 1",
        "amount == 0 or endsinanyof(amount, strrange('01',19))",),
    
    # rule 6: Lithuanian (ends in 1 but not 11, ends in 0 or 10-20, everything else)
    6: ("endsin1(amount) and not endsin11(amount)",
        "endsin0(amount) or endsinanyof(amount, strrange('10',11))",),
    
    # rule 7: Russian (ends in 1 but not 11, ends in 2-4 but not 12-14, everything else)
    7: ("endsin1(amount) and not endsin11(amount)",
        "endsinanyof(amount, strrange('2',3)) and not endsinanyof(amount, strrange('12',3))",),
    
    # rule 8: Slovak (is 1, is 2-4, everything else)
    8: ("amount == 1",
        "amount in (2,3,4)",),
    
    # rule 9: Polish (is 1, ends in 2-4 but not 12-14, everything else)
    9: ("amount == 1",
        "endsinanyof(amount, (2,3,4)) and not endsinanyof(amount, (12,13,14))",),
    
    # rule 10: Slovenian (ends in 01, ends in 02, ends in 03 or 04, everything else)
    10: ("endsin01(amount)",
        "endsin02(amount)",
        "endsin03(amount) or endsin04(amount)",),
    
    # rule 11: Irish Gaeilge (1, 2, 3-6, 7-10, everything else)
    11: ("amount == 1",
        "amount == 2",
        "amount >= 3 and amount <= 6",
        "amount >= 7 and amount <= 10",),
    
}

def __rulecompiler():
    # bring in the rule definitions
    global __rule_definition
    
    rulefuncs = []
    # read each rule definition
    for rule in __rule_definition:
        rulefuncs.insert(rule, [])
        # read each rule function definition
        for str in __rule_definition[rule]:
            str = "lambda amount: " + str
            # compile the rule function and put it into the rule fns list
            rulefuncs[rule].append(eval(compile(str, '<string>', 'eval')))
        # for each rule, there's an implied "everything else" at the end
        rulefuncs[rule].append(lambda amount: True)
        # convert to a tuple for immutability
        rulefuncs[rule] = tuple(rulefuncs[rule])
    # convert to a tuple for immutability
    return tuple(rulefuncs)

def __getrules(rule, rule_funcs = __rulecompiler()):
    """Returns a tuple of functions which can be used to test a count and return the index of the correct word form"""
    # maintenance note: __rulecompiler() is expensive and should only
    # be called once, that's why it's a default parameter
    return rule_funcs[rule]
    

def __index(count, rule):
    """Determines the index into a wordlist for a particular count and rule."""
    try:
        ruleset = __getrules(rule)
    except IndexError:
        raise RuleError("Invalid rule requested: {0}".format(rule))
        
    for idx in range(len(ruleset)):
        if ruleset[idx](count):
            return idx
    
    # this should never happen because of the implied "everything else" at the
    # end of each rule
    raise RuleError("Could not locate a suitable rule function")

class RuleError(Exception):
    """Represents an error locating or applying a language rule"""
    pass

def _endsin(value, finaldigit):
    """Returns true if a particular value ends in a particular digit."""
    # ensure we're dealing with an integer
    if value % 1 != 0:
        raise TypeError("value should be an integer")
    
    if int(finaldigit) < 0:
        raise IndexError("finaldigit should be a positive integer")
    
    # invert the sign of negative numbers
    if value < 0:
        value = value * -1
    
    # coerce to string, all remaining comparisons will be stringwise
    finaldigit = str(finaldigit)
    
    if len(finaldigit) < 2:
        # remove the 10s digit and up
        testdigit = str(value - ((value / 10) * 10))
        return testdigit == finaldigit
    elif len(finaldigit) < 3:
        # remove the 100s digit and up, convert to string
        testdigits = str(value - ((value / 100) * 100))
        if len(testdigits) < 2:
            testdigits = "0" + testdigits
        return testdigits == finaldigit
    else:
        raise IndexError("_endsin only handles 1 and 2 digit tests")

def endsin1(value):
    """Returns true if a value ends in 1."""
    return _endsin(value, 1)

def endsin01(value):
    """Returns true if a value ends in 01."""
    return _endsin(value, "01")

def endsin02(value):
    """Returns true if a value ends in 02."""
    return _endsin(value, "02")

def endsin03(value):
    """Returns true if a value ends in 03."""
    return _endsin(value, "03")

def endsin04(value):
    """Returns true if a value ends in 04."""
    return _endsin(value, "04")

def endsin11(value):
    """Returns true if a value ends in 11."""
    return _endsin(value, 11)

def endsin0(value):
    """Returns true if a value ends in 0."""
    return _endsin(value, 0)

def endsinanyof(value, suffixes):
    """Returns true if a value ends in any of the suffixes."""
    return any([_endsin(value, suffix) for suffix in suffixes])

def strrange(start, count):
    """Returns a range of numbers in string format, padded with 0s"""
    # create a formatstring that will pad with the proper amount of zeroes
    formatstr = "{{0:0{0}}}".format(len(start))
    # build and return the list
    return [formatstr.format(x) for x in range(int(start), int(start) + count)]
