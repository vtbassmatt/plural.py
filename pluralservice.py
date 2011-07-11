from flask import Flask, request, json, make_response
from plural import pluralize, explain, rulefor, RuleError

app = Flask(__name__)

@app.route('/language/<langcode>')
def rulefor_service(langcode):
    langcode = str(langcode)
    rule = rulefor(langcode) or None
    
    response = {"langcode":langcode, "rule": rule}
    if rule is None:
        response["error"] = "Invalid language specified"
    
    response = make_response(json.dumps(response))
    response.mimetype = 'application/json'
    return response

@app.route('/rule/<int:rule>')
def explain_service(rule):

    response = {"rule":rule}
    
    try:
        response["explanation"] = explain(rule)
        response["translations_required"] = len(explain(rule))
    except RuleError:
        response["explanation"] = None
        response["translations_required"] = 0
        response["error"] = "Invalid rule specified"
    
    response = make_response(json.dumps(response))
    response.mimetype = 'application/json'
    return response

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
        
    response = make_response(json.dumps(response))
    response.mimetype = 'application/json'
    return response

if __name__ == '__main__':
    app.run(debug=True)
