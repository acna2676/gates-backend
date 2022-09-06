sam package --template-file template.yml --output-template-file packaged.yml --s3-bucket gates-dev-sam-package
sam deploy --template-file packaged.yml --stack-name gates-dev-apig --capabilities CAPABILITY_IAM
aws cloudformation delete-stack --stack-name gates-dev-apig
