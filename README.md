# Pulsegen AI Review Trend Analysis

This project implements an **Agentic AI system** to analyze Google Play Store reviews and generate **monthly topic trend reports** for product teams.

The system ingests reviews **daily (batch-wise)**, extracts high-recall feedback topics using an agentic approach, consolidates semantically similar issues, and produces a **time-series trend table**.

This solution is built as part of the **Pulsegen Assignment**.

---

##  Features

- Daily batch ingestion of Google Play Store reviews  
- Agentic topic extraction (no LDA / TopicBERT)  
- Semantic consolidation of similar feedback  
- Monthly trend analysis (Topics × Dates)  
- CSV output report (submission-ready)  
- Single-file, end-to-end executable pipeline  

---

##  Why Agentic AI?

Traditional topic models struggle with:
- Short, noisy app reviews
- Evolving user issues
- Semantic duplication (e.g., “rude delivery guy” vs “delivery partner behaved badly”)

This project uses an **agent-based approach** that:
- Maximizes recall
- Dynamically adapts topics
- Produces meaningful trends for product decision-making

---
