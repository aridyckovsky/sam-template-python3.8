SERVICE=Service

build:
	sam build -m requirements.txt --use-container

run:
	sam local invoke "$(SERVICE)" -e ./events/event.json

deploy:
	sam deploy --guided

clean:
	rm -rf .aws-sam
