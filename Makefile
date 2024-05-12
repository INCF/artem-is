INPUT_DIR = $(inputs/tsv)

ARTEMIS_TSV =   $(wildcard inputs/tsv/*.tsv)

all: install convert

install:
	pip install -r requirements.txt

download:
	python convert_table/src/download.py

convert: download
	python convert_table/src/convert.py

clean_artemis:
	rm -rf $(ARTEMIS_TSV)

validate: validate_syntax validate_schema

package.json:
	npm install `cat npm-requirements.txt`

# Validate jsonld
validate_syntax: package.json
	grep -r  "@context" response_options | cut -d: -f1 | xargs -I fname jsonlint -q fname
	grep -r  "@context" schemas | cut -d: -f1 | xargs -I fname jsonlint -q fname

# you will need to install reproschema-py to run this one ( pip install reproschema )
validate_schema:
	reproschema -l DEBUG validate artemis_schema/schemas/artemis/activities
	reproschema -l DEBUG validate artemis_schema/schemas/artemis/protocols
	reproschema -l DEBUG validate artemis_schema/schemas/artemis/artemis_schema.jsonld
