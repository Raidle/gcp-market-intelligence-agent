# MarketTranslator
 
An AI agent that ingests live financial market data, stores it on Google Cloud Platform, and lets you query it in plain English. Instead of writing SQL or digging through spreadsheets, you just ask it things like *"what happened to crude oil futures last Friday?"* and it goes and finds out.
 
Built to learn GCP infrastructure and Google's Agent Development Kit (ADK): data pipelines, cloud deployment, and conversational AI in one project.
 
---
 
## What It Does
 
- Automatically pulls live market data (equities, futures) on a schedule
- Stores and structures it in BigQuery for fast querying
- Exposes a conversational AI agent that answers natural language questions about the data
- Runs entirely on GCP — Cloud Functions, Cloud Run, BigQuery, and Pub/Sub wired together
---
