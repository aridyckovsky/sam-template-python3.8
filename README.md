# SAM Template for Python 3.8

This is a template to conveniently get a serverless application model started
with Python 3.8. In order to use the template and get started with AWS Lambda
functions, you'll need both the AWS and SAM command line interfaces installed.

Once installed, the template can be downloaded from this repository directly
into a specified directory on your local machine.

The file structure that will be generated for your SAM-initialized project
based on this template is below.

### File Structure

```bash
.
├── Makefile
├── README.md
├── events
│   └── event.json
├── requirements.txt
├── src
│   └── service
│       ├── __init__.py
│       └── app.py
├── template.yaml
└── tests
    └── unit
        ├── __init__.py
        └── test_handler.py
```

It's important to understand that the main goal of the template is to make life
easier by bypassing some of the nitty-gritty and often tedious steps to create,
build, and deploy a successful Lambda application. 

### Initialize

To that end, the first step is to initialize your project with this command:


```
sam init -l gh:aridyckovsky/sam-template-python3.8
```

It will prompt you for a project name, defaulting to "My App", and that name is
used to create a project slug, defaulting to "my-app". You should almost never
need to specify a project slug, and simply press enter to the suggested default
(which is dynamically produced based on your project name choice).

### Build

To build your first Lambda function, run

```
make build
```

This is a convenient abstraction over a SAM command. If you'd like to see what
that command is, open the `Makefile` in your project directory.

### Local Run

To see if the Lambda function works as expected, run

```
make run
```

Again, this overlays the more complicated SAM command, and will invoke the
`lambda_handler` function found at `./src/service/app.py` locally. When you use
this command, you should see the underlying SAM invokation (i.e., `sam local
invoke ...`), and then a console message stating

```
Invoking service.app.lambda_handler (python3.8)
```

If the handler runs successfully, you will see a a few more messages, and
finally a JSON data payload starting with a status code of 200.


### Deployment

To deploy the Lambda function, in this case called "Service", to AWS, simply
run

```
make deploy
```

It will ask a series of questions, and if your AWS credentials are up to date
and configured, the command will lead to a new resource being pushed to S3
named after the project and a respective Lambda function.
