SERVICE={{cookiecutter.project_slug}}

build:
	sam build -m requirements.txt --use-container

run:
	sam local invoke "$(SERVICE)" -e ./events/events.json

clean:
	rm -rf .aws-sam
