.PHONY: build

build:
	sam build

deploy-infra:
	sam build && aws-vault exec <username> --no-session -- sam deploy

deploy-site:
	aws-vault exec <username> --no-session -- aws s3 sync 