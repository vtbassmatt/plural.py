from flask import Flask
from plural import pluralize, explain, rulefor, RuleError

app = Flask(__name__)

@app.route('/language/<langcode>')
def rulefor_service(langcode):
    langcode = str(langcode)
    rule = rulefor(langcode) or 'null'
    return '{{"langcode":"{0}", "rule":{1} }}'.format(langcode, rule)

if __name__ == '__main__':
    app.run(debug=True)
