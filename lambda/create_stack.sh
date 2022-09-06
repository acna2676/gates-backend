# S3 bucket for sam package
aws cloudformation create-stack --stack-name  gates-dev-sam-package --template-body file://cfn_sam_package_bucket.yml

# eventbridge and lambda package
sam package --template-file news_crawler.yml --output-template-file packaged_dev-news_crawler.yml --s3-bucket gates-dev-sam-package

sam deploy --template-file packaged_dev-news_crawler.yml --stack-name gates-dev-newsCrawler --capabilities CAPABILITY_IAM --parameter-overrides ApiKey=38b71e80eb38b29f4c9dfe728b2817121754038c

aws cloudformation delete-stack --stack-name gates-dev-newsCrawler
