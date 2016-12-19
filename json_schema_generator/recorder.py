# -*- coding: utf-8 -*-

import json
from json_schema_generator.generator import SchemaGenerator


class Recorder(object):

    def __init__(self, generator):
        self.generator = generator

    @classmethod
    def from_url(cls, url):
        from six.moves.urllib.request import urlopen

        json_data = urlopen(url).read()
        generator = SchemaGenerator.from_json(json_data)

        return cls(generator)

    @classmethod
    def from_dict(self, jsondict):
        generator = SchemaGenerator.from_json(json.dumps(jsondict))
        json_schema_data = generator.to_json()
        return json_schema_data

    def save_json_schema(self, file_path, **kwargs):
        json_schema_data = self.generator.to_json(**kwargs)

        with open(file_path, 'w') as json_schema_file:
            json_schema_file.write(json_schema_data)

