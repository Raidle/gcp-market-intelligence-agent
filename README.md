Yahoo Finance API
        ↓
Cloud Scheduler (runs every hour)
        ↓
Cloud Function → fetches + drops CSV into GCS
        ↓
GCS trigger → another Cloud Function → loads into BigQuery
        ↓
ADK Agent on Cloud Run
  ├── Tool: query_bigquery(sql)
  ├── Tool: get_latest_price(ticker)
  └── Tool: summarize_anomalies(date)
        ↓
Talk to it via a simple CLI or minimal web UI
