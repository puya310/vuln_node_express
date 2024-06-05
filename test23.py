from datetime import datetime, timedelta

# Calculate the date range for the last 7 days
end_date = datetime.now()
start_date = end_date - timedelta(days=7)

# Format the dates in the required format (YYYY-MM-DD)
end_date_str = end_date.strftime('%Y-%m-%d')
start_date_str = start_date.strftime('%Y-%m-%d')

# Base URL
base_url = "https://app.snyk.io/org/illuminate/reporting"

# URL parameters
params = {
    "introduced_start": start_date_str,
    "introduced_end": end_date_str,
    "introduced_range_preset": "last7days",
    "fromGitHubAuth": "true",
    "v": 1,
    "context[page]": "issues-detail",
    "issue_status": "%255B%2522Open%2522%255D",
    "issue_by": "Severity",
    "table_issues_detail_cols": "SEVERITY%257CSCORE%257CCVE%257CCWE%257CPROJECT%257CEXPLOIT%2520MATURITY%257CAUTO%2520FIXABLE%257CINTRODUCED%257CSNYK%2520PRODUCT",
    "project_name": "%255B%25220518acec-39e5-4ad7-8058-d68a40df1832%2522%252C%2522b06b5db4-2966-4111-b598-493f0e2b28e8%2522%252C%252243380f06-9c5f-4f3b-b5eb-a288bd3ab500%2522%252C%25227c23e1e8-55d1-4c50-8293-62cd14e050c4%2522%252C%2522df468b3b-ba6a-4f1d-956e-f59037b754fd%2522%252C%252215201eda-14ba-4d25-98c1-6b3cfe9eb549%2522%252C%25228ae322d6-2c86-461d-b2c4-83bcb52e28d9%2522%252C%2522517e21c3-07d7-44ff-9fb3-43c88c3b9a1e%2522%252C%252257b93bc5-4b77-4fdb-ba14-cf47e24103d2%2522%252C%25225e9a0c91-d6b5-4344-9f86-e6c5b0781a9b%2522%252C%25227591c7c3-576b-4e6e-8998-7d6e6e59e21d%2522%252C%252235e75649-48a0-4bb6-9cf7-4f00370c4e82%2522%252C%2522d6f82ab8-f3a6-4400-8060-29ff7be77b37%2522%252C%2522be0d3fdc-5def-4f83-8840-93f165ae89c0%2522%252C%2522a0912888-3353-485b-864f-6dc535a34c5a%2522%252C%2522682406fa-5d13-49aa-8723-c4f46a05ccc0%2522%252C%252217513b1a-5ba6-4d0f-9b3f-08de2294c02e%2522%252C%2522d436d09d-480b-4953-92a3-8fdc8415a9fc%2522%252C%25228f7fd14b-0212-4d12-ac26-700931b163aa%2522%252C%252293bba727-2140-41de-b3fe-73a9d8f9d9e8%2522%252C%252235f05563-ef9f-43f4-bc20-e9cb69d75711%2522%252C%2522c572c4c4-73d8-4f20-96fb-29e8ef79a4fd%2522%252C%25221edd7237-b0a1-4b7a-92b7-faffa96fa9a4%2522%252C%252230587b16-ba13-4aff-ac25-024e126d96f2%2522%252C%2522798765a1-b3e9-4339-a5ed-be76380a49dc%2522%252C%2522129e49e7-6e9f-4f66-b63d-12bf339443d1%2522%252C%2522d6b932ae-4b2b-40e6-ac74-749e4782c7a2%2522%252C%2522169f5b37-f94e-4b50-bec8-f644fb708108%2522%252C%252207887083-7831-46ee-b313-f14e8666a62c%2522%252C%2522589e05cf-b685-4246-a438-2da2a9be9c84%2522%252C%25223bcc140f-9311-4470-8ea2-6bfda85b312b%2522%252C%25220c8066fb-6d81-4659-8f44-f8c80389dea8%2522%252C%25222e146995-d8d9-4137-b22b-4f73fae19710%2522%255D"
}

# Generate the URL with the updated date range
url = base_url + "?" + "&".join([f"{key}={value}" for key, value in params.items()])

print("Generated URL for the last 7 days:")
print(url)
