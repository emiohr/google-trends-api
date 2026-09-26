# Google Trends API (Python, Node.js, cURL) — a working pytrends alternative

Get **Google Trends data through a simple API**: interest over time, **related queries (top, rising, Breakout)**, related topics and **interest by region** — for any keyword, any country, any time range since 2004, and for Web, **YouTube**, News, Images and Google Shopping search.

> **Why this exists:** [pytrends](https://github.com/GeneralMills/pytrends) was **archived in April 2025** and constantly fails with `429 Too Many Requests`. Google's own [Trends API](https://developers.google.com/search/apis/trends) is an invite-only alpha. This repo shows how to get the same data reliably in a few lines of code.

The data comes from the [**Google Trends Scraper & API**](https://apify.com/jesting_grass/google-trends-api) on Apify, which reads a commercial Google Trends data feed instead of scraping the website — so it doesn't get blocked, and failed lookups are free.

## Quick start (Python)

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=your_token   # free account at https://console.apify.com
```

```python
from apify_client import ApifyClient

client = ApifyClient("YOUR_APIFY_TOKEN")
run = client.actor("jesting_grass/google-trends-api").call(run_input={
    "keywords": ["chatgpt", "claude", "gemini"],
    "location": "United States",
    "timeRange": "past_12_months",
    "includeRelatedQueries": True,
})
for row in client.dataset(run.default_dataset_id).iterate_items():
    print(row["keyword"], row["averageInterest"], row["peakDate"])
    print("  rising:", [q["query"] for q in row["relatedQueries"]["rising"][:5]])
```

More examples in [`examples/`](examples):

| File | What it shows |
|---|---|
| [`interest_over_time.py`](examples/interest_over_time.py) | Compare up to 5 keywords over time |
| [`related_queries.py`](examples/related_queries.py) | Rising / Breakout keyword ideas + top regions (YouTube search) |
| [`pandas_dataframe.py`](examples/pandas_dataframe.py) | Timeline as a pandas DataFrame — like pytrends `interest_over_time()` |
| [`node.js`](examples/node.js) | Same thing in Node.js |
| [`curl.sh`](examples/curl.sh) | One HTTP call, JSON back |

## pytrends → this API

| pytrends | Here |
|---|---|
| `pytrends.build_payload(kw_list, timeframe='today 12-m', geo='US')` | `{"keywords": kw_list, "timeRange": "past_12_months", "location": "United States"}` |
| `interest_over_time()` | `row["timeline"]` (+ `averageInterest`, `peakInterest`, `peakDate`) |
| `related_queries()` | `"includeRelatedQueries": true` → `row["relatedQueries"]["top" / "rising"]` |
| `related_topics()` | `"includeRelatedTopics": true` → `row["relatedTopics"]` |
| `interest_by_region()` | `"includeInterestByRegion": true` → `row["interestByRegion"]` |
| `gprop='youtube'` | `"searchType": "youtube"` (also `news`, `images`, `froogle`) |
| `429 Too Many Requests` 😩 | — |

## Output

```json
{
  "keyword": "black friday",
  "location": "Sweden",
  "averageInterest": 7,
  "peakInterest": 100,
  "peakDate": "2025-11-23",
  "timeline": [{ "date": "2025-09-28", "value": 2, "partial": false }],
  "relatedQueries": {
    "top": [{ "query": "black friday 2025", "value": "100" }],
    "rising": [{ "query": "när är black friday 2026", "value": "Breakout" }]
  },
  "interestByRegion": [{ "region": "Stockholm County", "geoCode": "SE-AB", "value": 100 }]
}
```

## Pricing

Pay per use, no subscription: one query compares up to 5 keywords, and related queries / topics / regions are optional add-ons. Failed lookups are never charged. Current prices are on the [Actor page](https://apify.com/jesting_grass/google-trends-api). Apify's free plan includes monthly credit to try it.

## FAQ

**Is there an official Google Trends API?** Google announced one in 2025 as a limited alpha for selected testers. Until it's generally available, a hosted API like this is the practical option.

**Why does pytrends return 429?** pytrends loads the Google Trends website like a browser. Google rate-limits that traffic, so bursts of requests get `429 Too Many Requests`. Sleeping, proxies and retries only partly help.

**Can AI agents use it?** Yes — every Apify Actor is available as a tool through the [Apify MCP server](https://mcp.apify.com).

## License

Examples are MIT licensed. Not affiliated with or endorsed by Google.
