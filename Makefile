.PHONY: clean
.PHONY: validate
.PHONY: build
.PHONY: unit_test
.PHONY: integration_test
.PHONY: local_invoke_%
.PHONY: local_startapi
.PHONY: local_startapi_dg_%
.PHONY: deploy
.PHONY: deploy_guided
.PHONY: delete

.DEFAULT_GOAL := build

clean:
# for windows
	if exist ".aws-sam" (	\
		rmdir /s /q .aws-sam	\
	)
# for Linux
#	rm -rf .aws-sam

fmt:
	cd app & go fmt ./...
	cd appbase & go fmt ./...

lint:
	cd app & staticcheck ./...
	cd appbase & staticcheck ./...
	
vet:
	cd app & go vet ./...	
	cd appbase & go vet ./...
	cd app & shadow ./...
	cd appbase & shadow ./...

validate:
	sam validate

build: clean
# for windows	
	sam build --use-container
# for linux
# TODO	

unit_test:
# TODO
	python -m pytest app/tests/unit -v

integration_test:
# TODO
	AWS_SAM_STACK_NAME="todo-app" python -m pytest app/tests/integration -v

local_invoke_%:
	sam local invoke --env-vars local-env.json --event events\event-${@:local_invoke_%=%}.json ${@:local_invoke_%=%}

local_startapi:
	sam local start-api --env-vars local-env.json	

deploy_guided:
	sam deploy --guided

deploy:
	sam deploy

delete:
	sam delete