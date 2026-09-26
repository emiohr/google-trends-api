"""Google Trends timeline as a pandas DataFrame (drop-in for pytrends interest_over_time())."""
import os

import pandas as pd
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("jesting_grass/google-trends-api").call(run_input={
    "keywords": ["bitcoin", "ethereum"],
    "timeRange": "past_5_years",
})

frames = []
for row in client.dataset(run.default_dataset_id).iterate_items():
    s = pd.Series({p["date"]: p["value"] for p in row["timeline"]}, name=row["keyword"])
    frames.append(s)
df = pd.concat(frames, axis=1)
df.index = pd.to_datetime(df.index)
print(df.tail())
