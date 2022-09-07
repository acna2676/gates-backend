# TTL有効化
aws dynamodb update-time-to-live --table-name gates-dev --time-to-live-specification "Enabled=true, AttributeName=ttl" --endpoint-url http://localhost:8000
