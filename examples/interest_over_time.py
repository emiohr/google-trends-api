"""Google Trends interest over time in Python — no pytrends, no 429 errors.

pip install "apify-client>=3"
export APIFY_TOKEN=...   # free account: https://console.apify.com
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("jesting_grass/google-trends-api").call(run_input={
    "keywords": ["chatgpt", "claude", "gemini"],   # up to 5 compared per query
    "location": "United States",                   # or "" for worldwide
    "timeRange": "past_12_months",
})

for row in client.dataset(run.default_dataset_id).iterate_items():
    print(f'{row["keyword"]:<10} avg={row["averageInterest"]:<5} peak={row["peakInterest"]} on {row["peakDate"]}')
