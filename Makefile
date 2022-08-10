.PHONY:


INPUT_DIR = $(inputs/tsv)

ARTEMIS_TSV =   $(wildcard inputs/tsv/*.tsv)

all: install download

install:
	pip install -r requirements.txt

download:
	python convert_table/src/download.py


clean_artemis:
	rm -rf $(ARTEMIS_TSV)
