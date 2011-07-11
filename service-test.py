#import os
import pluralservice
import unittest

class PluralServiceTestCase(unittest.TestCase):
    
    def setUp(self):
        pluralservice.app.config['TESTING'] = True
        self.app = pluralservice.app.test_client()

    def test_language_en(self):
        rv = self.app.get('/language/en')
        assert '"langcode": "en"' in rv.data
        assert '"rule": 1' in rv.data
        assert 'null' not in rv.data
        assert '"error":' not in rv.data
    
    def test_language_klingon(self):
        rv = self.app.get('/language/klingon')
        assert '"langcode": "klingon"' in rv.data
        assert '"rule": null' in rv.data
        assert '"error": "Invalid language specified"' in rv.data
    
    def test_rule_1(self):
        rv = self.app.get('/rule/1')
        assert '"explanation": [' in rv.data
        assert '"translations_required": 2' in rv.data
        assert '"rule": 1' in rv.data
        assert '"error":' not in rv.data

    def test_rule_500(self):
        rv = self.app.get('/rule/500')
        assert '"explanation": null' in rv.data
        assert '"translations_required": 0' in rv.data
        assert '"rule": 500' in rv.data
        assert '"error": "Invalid rule specified"' in rv.data

    def test_pluralize_0(self):
        rv = self.app.get('/pluralize?w=bird&w=birds&c=2&r=0')
        assert '"count": 2' in rv.data
        assert '"word": "bird"' in rv.data
        assert '"rule": 0' in rv.data
        assert '"error":' not in rv.data

    def test_pluralize_1(self):
        rv = self.app.get('/pluralize?w=bird&w=birds&c=2&r=1')
        assert '"count": 2' in rv.data
        assert '"word": "birds"' in rv.data
        assert '"rule": 1' in rv.data
        assert '"error":' not in rv.data

    def test_pluralize_1_error(self):
        rv = self.app.get('/pluralize?w=bird&c=2&r=1')
        assert '"count": 2' in rv.data
        assert '"word": null' in rv.data
        assert '"rule": 1' in rv.data
        assert '"error": "Not enough words passed in"' in rv.data

    def test_pluralize_500(self):
        rv = self.app.get('/pluralize?w=bird&w=birds&c=2&r=500')
        assert '"count": 2' in rv.data
        assert '"word": null' in rv.data
        assert '"rule": 500' in rv.data
        assert '"error": "Invalid rule specified"' in rv.data

if __name__ == '__main__':
    unittest.main()
