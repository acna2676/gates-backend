## pipeline 作成

sam pipeline bootstrap (.create_pipeline_bootstrap)
sam pipine init (.create_pipeline)
aws cloudformation create-stack --stack-name gates-dev-codepipeline --template-body file://codepipeline.yaml --capabilities CAPABILITY_IAM (create_pipeline_tack)
codepipeline の source ステージの編集画面で GitHub との接続を完了させる
