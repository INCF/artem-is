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

# you will need to install reproschema-py to run this one ( pip install reproschema )
validate:
	pre-commit run -a  check-json
	reproschema -l DEBUG validate schemas/artemis/activities
	reproschema -l DEBUG validate schemas/artemis/protocols
	reproschema -l DEBUG validate schemas/artemis/artemis_schema.jsonld
