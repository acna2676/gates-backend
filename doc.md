## pipeline 作成

sam pipeline bootstrap (.create_pipeline_bootstrap)
sam pipeline init (.create_pipeline)
aws cloudformation create-stack --stack-name gates-dev-codepipeline --template-body file://codepipeline.yaml --capabilities CAPABILITY_IAM (create_pipeline_stack)
codepipeline の source ステージの編集画面で GitHub との接続を完了させる

## local テスト

sam local start-api --env-vars env.json
※env.json 内で使用している host.docker.internal とは Docker Desktop で用意されている、コンテナからローカル環境を参照する際のホスト名です
※env.json はトップレベルに lambda リソース名を書き、テンプレートにも環境変数を定義しないと動作しない
