SERVICE={{cookiecutter.project_slug}}

build:
	sam build -m requirements.txt --use-container

run:
	sam local invoke "$(SERVICE)" -e ./events/events.json

deploy:
	sam deploy --guided

clean:
	rm -rf .aws-sam
