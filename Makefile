all: data/ndc-content-world-bank.csv data/ndc-content-cait.csv data/ndc-content-klimalog-die-gdi.csv

data/ndc-content-world-bank.csv: scripts/worldbank.py venv
	./venv/bin/python scripts/worldbank.py

data/ndc-content-cait.csv: scripts/cait.py venv
	./venv/bin/python scripts/cait.py

data/ndc-content-klimalog-die-gdi.csv:
	@echo $@
	wget https://klimalog.die-gdi.de/ndc/assets/map_data/Explorer-INDC-Data.csv -O data/ndc-content-klimalog-die-gdi.csv

venv: scripts/requirements.txt
	[ -d ./venv ] || python3 -m venv venv
	./venv/bin/pip install --upgrade pip
	./venv/bin/pip install -Ur scripts/requirements.txt
	touch venv

clean:
	rm -rf data/*.csv venv
