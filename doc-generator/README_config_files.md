# Config Files

Config files support most of the command-line arguments of the doc_generator.py script (except for --help and --config). Additional configuration options are supported for some output modes.

If an option is specified in more than one way, command-line arguments override those in the config file.

Config files must be valid JSON.

## Supported Attributes

Note that the names of some config keys differ from their command-line counterparts, as noted. Unless otherwise noted, the meaning of the parameter is the same as its command-line counterpart. The `uri_mapping` attribute is expected. All other attributes are optional in config files.

- actions_in_property_table: Boolean. If true, omit "Actions" from the property tables.
- add_toc: Boolean. If true, generate a table of contents and either substitute it for `[add_toc]` in the boilerplate (intro or postscript), or place it at the beginning of the output document. Makes sense only for HTML mode. If `[add_toc]` appears anywhere in the boilerplate, this flag is automatically set to true.
- boilerplate_intro: location of a markdown file providing content to place at the beginning of the document (prior to the generated schema documentation). If a relative path, should be relative to the location of the config file.
- boilerplate_postscript: location of a markdown file providing content to place at the end of the document (after to the generated schema documentation). If a relative path, should be relative to the location of the config file.
- combine_multiple_refs: specifies a threshold at which multiple references to the same object within a schema will be moved into Property Details, instead of expanded in place. See below for more detail.
- content_supplement: location of a content supplement file. This is a JSON file that specifies content substitutions to be made within the generated schema documentation. If a relative path, should be relative to the location of the config file.
- escape_chars (command line: `escape`): Characters to escape in generated Markdown. For example, use --escape=@ if strings with embedded @ are being converted to mailto links by your markdown processor.
- excluded_annotations: A list of annotation names (strings) to omit. Wildcard match is supported for strings that begin with "*".
- excluded_pattern_properties: pattern properties to omit from output. Note that backslashes must be escaped in JSON ("\" becomes "\\").
- excluded_properties: A list of property names (strings) to omit. Wildcard match is supported for strings that begin with "*" ("*odata.count" matches "Members\@odata.count" and others).
- excluded_schemas: Schemas (by name) to omit from output.
- format (command line: `format`): Output format. One of `markdown`, `slate`, `html`, `csv`
- html_title: A string to use as the `title` element in HTML output.
- import_from: Name of a file or directory containing JSON schemas to process. Wild cards are acceptable. Default: json-schema.
- locale: specifies a locale code (case-sensitive) for localized output. Localization of strings supplied by the doc generator code uses gettext. Locale files go in the "locale" directory in the doc_generator root. Translated descriptions and annotations may be supplied in localized JSON schema files.
- normative: Produce normative (developer-focused) output. U
- object_reference_disposition: a data structure that specifies properties that should be moved to the "Common Objects" section and/or objects that should be included inline where they are referenced, to override default behavior. See below.
- omit_version_in_headers: Boolean. If true, omit schema versions in section headers.
- outfile (command line: `out`): Output file (default depends on output format: output.md for Markdown, index.html for HTML, output.csv for CSV
- payload_dir (command line: `payload_dir`): Directory location for JSON payload and Action examples. Optional. See below for more detail.
- profile_doc (command line: `profile`): Path to a JSON profile document, for profile output.
- profile_terse (command line: `terse`): Boolean. Produce "terse" profile output; meaningful only in profile mode. See below for more detail.
- profile_uri_to_local: For profile mode only, an object like uri_mapping, for locations of profiles.
- property_index (command line: `property_index`): Boolean: Produce Property Index output. See README_Property_Index(README_Property_Index.md) for more information about this mode.
- property_index_config_out (command line: `property_index_config_out`): Generate an updated config file, with specified filename (property_index mode only).
- registry_uri_to_local: For profile mode only, an object like uri_mapping, for locations of registries.
- subset (command_line: `subset`): Path to a JSON profile document. Generates "Schema subset" output, with the subset defined in the JSON profile document.
- uri_mapping: this should be an object with the partial URL of schema repositories as attributes, and local directory paths as values.


### In More Detail

#### combine_multiple_refs

The combine_multiple_refs attribute specifies a threshold at which multiple references to the same object within a schema will be moved into Property Details, instead of expanded in place. For example, include the following to specify that if an object is referred to three or more times, it should be moved into property details:

```
      "combine_multiple_refs": 3,
```

#### object_reference_disposition

The object_reference_disposition attribute specifies a JSON object with "common_object" and "include" fields (either or both may be specified), each of which specifies a list. The "common_object" list consists of property names, for example "Redundancy." The "include" list specifies properties by their full path. For example:

```json
    "object_reference_disposition": {
        "common_object": [
            "Redundancy"
        ],
        "include": [
            "http://redfish.dmtf.org/schemas/v1/PCIeDevice.json#/definitions/PCIeInterface"
        ]
    }
```

#### payload_dir

The payload_dir attribute specifies a directory location for JSON payload and Action examples. If relative, this path is relative to the working directory in which the doc_generator.py script is run. Within the payload directory, use the following naming scheme for example files:

 * &lt;schema_name&gt;-v<major_version>-example.json for JSON payloads
 * &lt;schema_name&gt;-v&lt;major_version&gt;-action-&lt;action_name%gt;.json for action examples

#### profile_terse

The profile_terse attribute is meaningful only when a profile document is also specified. When true, "terse" output will be produced. By default, profile output is verbose and includes all properties regardless of profile requirements. "Terse" output is intended for use by Service developers, including only the subset of properties with profile requirements.

## Examples

Several files in the sample_inputs directory provide examples of configuration files that might be used to produce different types of documentation. Below are some example command-line invocations.

These assume that you have a clone of the DMTF/Redfish repo and the DMTF/Redfish-Tools repo in the same parent directory, and that your working directory is the Redfish clone -- so that the schemas are in ./json-schema and doc_generator.py is at ../Redfish-Tools/doc-generator/doc_generator.py relative to your current working directory.
n
Note that the config files themselves contain references to other files in this directory.


### Produce full documentation, in HTML format:

 python ../Redfish-Tools/doc-generator/doc_generator.py --config=../Redfish-Tools/doc-generator/sample_inputs/standard_html/config.json

# TODO: UPDATE THE BELOW

Config file references supplemental file *supplement_for_standard_output.md*

### Produce full documentation, with normative descriptions and in HTML format:

 python ../Redfish-Tools/doc-generator/doc_generator.py --config=../Redfish-Tools/doc-generator/sample_inputs/config_for_normative_html.json

Config file references supplemental file *supplement_for_standard_output.md*

Note that the "object_reference_disposition" part of this config identifies specific behavior for the Redundancy resource and for PCIeInterface (defined in PCIeDevice).

### Produce Profile output (terse mode, markdown format):

  python ../Redfish-Tools/doc-generator/doc_generator.py --config=../Redfish-Tools/doc-generator/sample_inputs/config_for_profile_terse.json

Config file references supplemental file *SampleProfileInput.md* and the profile OCPBasicServer.v1_0_0.json (which in turn references OCPManagedDevice.v1_0_0.json).

### Produce Subset documentation (HTML format):

  python ../Redfish-Tools/doc-generator/doc_generator.py --config=../Redfish-Tools/doc-generator/sample_inputs/config_for_subset.json

Config file references supplemental file *SampleProfileInput.md* and the profile OCPBasicServer.v1_0_0.json (which in turn references OCPManagedDevice.v1_0_0.json).


### Produce Property Index output (HTML format):

  python ../Redfish-Tools/doc-generator/doc_generator.py --config=../Redfish-Tools/doc-generator/sample_inputs/config_for_property_index.json

Note that the config file for property index output includes some elements that are specific to that mode: DescriptionOverrides. Property Index mode does not use a supplemental markdown document.

### Produce CSV output:

 python ../Redfish-Tools/doc-generator/doc_generator.py --config=../Redfish-Tools/doc-generator/sample_inputs/config_for_csv.json

Config file references supplemental file *supplement_for_standard_output.md*. (Note that there's a lot of detail in this supplemental file that's irrelevant to CSV output, and is simply ignored.)
