# Copyright Notice:
# Copyright 2020 Distributed Management Task Force, Inc. All rights reserved.
# License: BSD 3-Clause License. For full text see link: https://github.com/DMTF/Redfish-Tools/blob/master/LICENSE.md

"""
File: test_localized_schemas.py

Brief: test(s) for detection and use of localized schemas.
"""

import os
import os.path
import copy
from unittest.mock import patch
import pytest
from doc_generator import DocGenerator

testcase_path = os.path.join('tests', 'samples', 'localized_schemas', 'general', 'input')

base_config = {
    'excluded_by_match': ['@odata.count', '@odata.navigationLink'],
    'profile_resources': {},
    'units_translation': {},
    'excluded_annotations_by_match': ['@odata.count', '@odata.navigationLink'],
    'excluded_schemas': [],
    'excluded_properties': ['@odata.id', '@odata.context', '@odata.type'],
    'uri_replacements': {},

    'profile': {},
    'escape_chars': [],

    'output_format': 'markdown',
}

# TODO: this is non-normative output. Also add a normative version.
@patch('urllib.request') # so we don't make HTTP requests. NB: samples should not call for outside resources.
def test_localized_schemas_default(mockRequest):
    """ Verify a few expected strings are output in the default way when no locale is specified.
    """

    config = copy.deepcopy(base_config)
    input_dir = os.path.abspath(testcase_path)

    config['uri_to_local'] = {'redfish.dmtf.org/schemas/v1': input_dir}
    config['local_to_uri'] = {input_dir : 'redfish.dmtf.org/schemas/v1'}

    docGen = DocGenerator([ input_dir ], '/dev/null', config)

    files_to_process = docGen.get_files(docGen.import_from)
    output = docGen.generate_docs()

    expected_strings = [
        'The ComputerSystem schema represents a computer or system instance',
        'The BootOptionReference of the Boot Option to perform a one-time boot from when BootSourceOverrideTarget is `UefiBootNext`.',
        'The name of the boot order property that the system uses for the persistent boot order. *For the possible property values, see BootOrderPropertySelection in Property details.*',
        '| AliasBootOrder | The system uses the AliasBootOrder property to specify the persistent boot order. |',
        ]
        # TODO: add some tests of the annotations.
    for x in expected_strings:
        assert x in output




# @patch('urllib.request') # so we don't make HTTP requests. NB: samples should not call for outside resources.
# def test_localized_schemas_en(mockRequest):
#     """ Verify that our same test strings are output the same way when "en" is specified explicitly.
#     """

#     config = copy.deepcopy(base_config)
#     config['locale'] = 'en'
#     input_dir = os.path.abspath(testcase_path)

#     config['uri_to_local'] = {'redfish.dmtf.org/schemas/v1': input_dir}
#     config['local_to_uri'] = {input_dir : 'redfish.dmtf.org/schemas/v1'}

#     docGen = DocGenerator([ input_dir ], '/dev/null', config)

#     files_to_process = docGen.get_files(docGen.import_from)
#     output = docGen.generate_docs()

#     expected_strings = [
#         'The ComputerSystem schema represents a computer or system instance',
#         'The BootOptionReference of the Boot Option to perform a one-time boot from when BootSourceOverrideTarget is `UefiBootNext`.',
#         'The name of the boot order property that the system uses for the persistent boot order. *For the possible property values, see BootOrderPropertySelection in Property details.*',
#         '| AliasBootOrder | The system uses the AliasBootOrder property to specify the persistent boot order. |',
#         ]
#         # TODO: add some tests of the annotations.

#     for x in expected_strings:
#         assert x in output


# @patch('urllib.request') # so we don't make HTTP requests. NB: samples should not call for outside resources.
# def test_localized_schemas_TEST(mockRequest):
#     """ Verify that the test strings are output correctly when TEST is specified for the locale.
#     """

#     config = copy.deepcopy(base_config)
#     config['locale'] = 'TEST'
#     input_dir = os.path.abspath(testcase_path)

#     config['uri_to_local'] = {'redfish.dmtf.org/schemas/v1': input_dir}
#     config['local_to_uri'] = {input_dir : 'redfish.dmtf.org/schemas/v1'}

#     docGen = DocGenerator([ input_dir ], '/dev/null', config)

#     files_to_process = docGen.get_files(docGen.import_from)
#     output = docGen.generate_docs()

#     expected_strings = [
#         'THE COMPUTERSYSTEM SCHEMA REPRESENTS A COMPUTER OR SYSTEM INSTANCE',
#         'THE BOOTOPTIONREFERENCE OF THE BOOT OPTION TO PERFORM A ONE-TIME BOOT FROM WHEN BOOTSOURCEOVERRIDETARGET IS `UEFIBOOTNEXT`.',
#         'THE NAME OF THE BOOT ORDER PROPERTY THAT THE SYSTEM USES FOR THE PERSISTENT BOOT ORDER. *FOR THE POSSIBLE PROPERTY VALUES, SEE BootOrderPropertySelection IN PROPERTY DETAILS.*',
#         '| AliasBootOrder | THE SYSTEM USES THE ALIASBOOTORDER PROPERTY TO SPECIFY THE PERSISTENT BOOT ORDER. |',
#         ]

#     for x in expected_strings:
#         assert x in output
