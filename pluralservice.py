from flask import Flask
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

if __name__ == '__main__':
    app.run(debug=True)
