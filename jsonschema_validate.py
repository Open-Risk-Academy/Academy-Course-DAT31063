import json
import jsonschema
import os

schema = json.load(fp=open('corporate_borrower.schema.json', mode='r'))
data = json.load(fp=open('corporate_borrower.json', mode='r'))[0]
dir = os.path.dirname(os.path.realpath(__file__))
resolver = jsonschema.RefResolver(referrer=schema, base_uri='file://' + dir + '/')
jsonschema.validate(data, schema, resolver=resolver)


