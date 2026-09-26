// Google Trends API in Node.js — npm i apify-client
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('jesting_grass/google-trends-api').call({
    keywords: ['black friday', 'cyber monday'],
    location: 'United Kingdom',
    timeRange: 'past_5_years',
    includeRelatedQueries: true,
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const row of items) console.log(row.keyword, row.averageInterest, row.peakDate);
