# Copyright Notice:
# Copyright 2020 Distributed Management Task Force, Inc. All rights reserved.
# License: BSD 3-Clause License. For full text see link: https://github.com/DMTF/Redfish-Tools/blob/master/LICENSE.md

"""
File: test_subset.py

Brief: test(s) for subset mode.
"""

import os
import copy
from unittest.mock import patch
import pytest
from doc_generator import DocGenerator
from .discrepancy_list import DiscrepancyList

testcase_path = os.path.join('tests', 'samples')

base_config = {
    'output_format': 'markdown',
	"actions_in_property_table": False,
	"excluded_properties": [
		"@odata.context",
		"@odata.type",
		"@odata.id",
		"@odata.etag",
		"Oem",
		"HealthRollup"

	],
	"excluded_annotations": [
		"*@odata.count",
		"*@odata.navigationLink"
	],
	"excluded_schemas": [
		"*Collection",
		"HostedStorageServices",
		"StorageService",
		"StorageSystem",
		"StorageServiceCollection",
		"StorageSystemCollection",
		"idRef"
	],
	"excluded_pattern_properties": [
		"^([a-zA-Z_][a-zA-Z0-9_]*)?@(odata|Redfish|Message)\\.[a-zA-Z_][a-zA-Z0-9_]*$"
	],
    "excluded_by_match": [],
	"units_translation": {
		"s": "seconds",
		"Mb/s": "Mbits/second",
		"By": "bytes",
		"Cel": "Celsius",
		"MiBy": "mebibytes",
		"W": "Watts",
		"V": "Volts",
		"mW": "milliWatts",
		"m": "meters"
	}
}

@patch('urllib.request') # so we don't make HTTP requests. NB: samples should not call for outside resources.
def test_subset_mode(mockRequest):
    """ TODO """

    config = copy.deepcopy(base_config)

    config['output_format'] = 'html'

    input_dir = os.path.abspath(os.path.join(testcase_path, 'subset_mode', 'json-schema'))
    config['uri_to_local'] = {'redfish.dmtf.org/schemas/v1': input_dir}
    config['local_to_uri'] = { input_dir : 'redfish.dmtf.org/schemas/v1'}

    subset_config = os.path.abspath(os.path.join(testcase_path, 'subset_mode', 'subset_spec.json'))
    # config['subset_doc'] = subset_config
    config['profile_mode'] = 'subset'
    config['profile_doc'] = subset_config

    docGen = DocGenerator([ input_dir ], '/dev/null', config)
    output = docGen.generate_docs()

    assert False
