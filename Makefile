.PHONY:


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
