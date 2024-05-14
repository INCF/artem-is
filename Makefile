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

# Validate jsonld
validate_syntax:
	grep -r  "@context" response_options | cut -d: -f1 | xargs -I {} jsonlint -q {}
	grep -r  "@context" schemas | cut -d: -f1 | xargs -I {} jsonlint -q {}

# you will need to install reproschema-py to run this one ( pip install reproschema )
validate_schema:
	reproschema -l DEBUG validate artemis_schema/schemas/artemis/activities
	reproschema -l DEBUG validate artemis_schema/schemas/artemis/protocols
	reproschema -l DEBUG validate artemis_schema/schemas/artemis/artemis_schema.jsonld
