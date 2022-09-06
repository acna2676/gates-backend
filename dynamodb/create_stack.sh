[hosting]
aws cloudformation create-stack --stack-name gates-dev-dynamodb --template-body file://template.yml
aws cloudformation update-stack --stack-name gates-dev-dynamodb --template-body file://template.yml
aws cloudformation delete-stack --stack-name gates-dev-dynamodb
