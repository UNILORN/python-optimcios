install:
	python3 setup.py install

inst-dev:
	pip3 install -r packages_requirements.txt
	cp -n .env.example .env

