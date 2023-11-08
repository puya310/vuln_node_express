#!/usr/bin/env bash
curl --include \
     --request POST \
     --header "Content-Type: application/json" \
     --header "Authorization: token 283aae43-ddc2-46e1-ae34-d517ec6c4241" \
     --data-binary "{
  \"key\": \"component\",
  \"value\": \"tagtest1\"
}" \
'https://api.snyk.io/v1/org/28a25d20-bb8b-42c9-be21-3815eb36930d/project/62432a37-2ce9-40ea-834b-691b2ac09882/tags'