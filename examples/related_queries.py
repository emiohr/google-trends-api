"""Rising and "Breakout" related queries from Google Trends — keyword research in 10 lines."""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("jesting_grass/google-trends-api").call(run_input={
    "keywords": ["protein powder"],
    "location": "United States",
    "searchType": "youtube",            # web | youtube | news | images | froogle (Shopping)
    "includeRelatedQueries": True,
    "includeInterestByRegion": True,
})

for row in client.dataset(run.default_dataset_id).iterate_items():
    print("Rising searches for", row["keyword"])
    for q in row["relatedQueries"]["rising"][:10]:
        print(f'  {q["query"]:<40} {q["value"]}')
    print("Top regions:", [r["region"] for r in row["interestByRegion"][:5]])
