# Google Trends API with plain HTTP — one call, JSON back
curl -X POST "https://api.apify.com/v2/acts/jesting_grass~google-trends-api/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"keywords":["chatgpt","claude"],"location":"United States","timeRange":"past_90_days"}'
