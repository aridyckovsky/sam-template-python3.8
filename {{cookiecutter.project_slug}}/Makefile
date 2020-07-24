SERVICE=Service

build:
	sam build -m requirements.txt --use-container

build-layer:
	mkdir -p "$(ARTIFACTS_DIR)/python"
	cp *.py "$(ARTIFACTS_DIR)/python"
	python -m pip install -r requirements.txt -t "$(ARTIFACTS_DIR)/python"

run:
	sam local invoke "$(SERVICE)" -e ./events/event.json

deploy:
	sam deploy --guided

clean:
	rm -rf .aws-sam
