install:
	python3 setup.py install

inst-dev:
	pip3 install -r packages_requirements.txt
	npm install -g wscat

dev:
	wscat -l 9999
