from flask import Flask, request, json
from plural import pluralize, explain, rulefor, RuleError

app = Flask(__name__)

@app.route('/language/<langcode>')
def rulefor_service(langcode):
    langcode = str(langcode)
    rule = rulefor(langcode) or 'null'
    return '{{"langcode":"{0}", "rule":{1} }}'.format(langcode, rule)

@app.route('/rule/<int:rule>')
def explain_service(rule):
    try:
        explanation = explain(rule)
        translations = len(explanation)
    except RuleError:
        explanation = 'null'
        translations = 0
    return '{{"rule":{0}, "translations_required":{2}, "explanation":{1} }}'.format(rule, explanation, translations)

@app.route('/pluralize')
def pluralize_service():
    wordlist = request.args.getlist('w')
    count = int(request.args['c'])
    rule = int(request.args['r'])
    
    response = {"count":count, "rule":rule}
    
    try:
        pluralword = pluralize(wordlist, count, rule)
        response["word"] = pluralword
    except IndexError:
        response["word"] = None
        response["error"] = "Not enough words passed in"
    except RuleError:
        response["word"] = None
        response["error"] = "Invalid rule specified"
        
    return json.dumps(response)

if __name__ == '__main__':
    app.run(debug=True)
