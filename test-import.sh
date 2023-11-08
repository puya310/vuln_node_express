curl --include \
     --request POST \
     --header "Content-Type: application/json; charset=utf-8" \
     --header "Authorization: token bfb65030-ed70-4515-a7a4-7b83deb286ac" \
     --data-binary "{
  \"target\": {
    \"owner\": \"d189ded3-15bb-4145-a5fe-b526a77637a1\",
    \"name\": \"Snyk-Goof(nodejs)/Snyk-Goof(nodejs)\",
    \"branch\": \"main\"
  },
  \"files\": [
    {
      \"path\": \"package.json\"
    }
  ]
}" \
'https://api.snyk.io/v1/org/43cbc864-d70e-4b88-96cf-82999e3c2452/integrations/d189ded3-15bb-4145-a5fe-b526a77637a1/import'