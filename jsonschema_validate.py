"""
   Copyright 2022 - 2023 Open Risk (www.openriskmanagement.com)

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

# This code accompanies the Open Risk Academy course "Class Inheritance in Data Science"
# https://www.openriskacademy.com/mod/book/view.php?id=720

import json
import os

import jsonschema

schema = json.load(fp=open('corporate_borrower.schema.json', mode='r'))
data = json.load(fp=open('corporate_borrower.json', mode='r'))[0]
dir = os.path.dirname(os.path.realpath(__file__))
resolver = jsonschema.RefResolver(referrer=schema, base_uri='file://' + dir + '/')
jsonschema.validate(data, schema, resolver=resolver)
