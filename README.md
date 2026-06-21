# AutoGuard-Claims-Dashboard
A proof-of-concept analytics pipeline for automotive warranty, claims processing, featuring automated, ETL workflow, and predictive trend modeling.
### Project Architecture & Documentation
The complete proof-of-concept documentation for this pipeline can be reviewed here:
- **Author**: Raeven Brown
- **Documentation**: [Automotive Warranty POC Walkthrough](https://docs.google.com/document/d/1d1dK_nrhLY_xDbB-bTi1V9FKxpHJSYs3/edit?usp=sharing&ouid=113467168658017302682&rtpof=true&sd=true) 
---

### Phase 1: Database Design (SQL)
I designed a relational database to model the warranty claims lifecycle. The schema consists of two distinct tables linked via a one-to-many foreign key relationship to avoid data redundancy and maintain efficiency.

- **`vehicles` table**: Acts as the master asset list (storing Make, Model, and Year).
- **`claims` table**: Acts as the transactional history (tracking repair cost and status).

*View the code:* [`database/schema.sql`](./database/schema.sql)  
*View the sample records:* [`database/mock_data.sql`](./database/mock_data.sql)

---

### Phase 2: Data Orchestration & Pipeline Automation (Python/Pandas)
To remove static manual SQL inserts, I engineered an automated ETL (Extract, Transform, Load) pipeline using Python and the `pandas` library to programmatically ingest, clean, and structure raw entries. 

1. **Extraction (The Ingest)**: Data is extracted programmatically from structured dictionaries mimicking raw inputs.
2. **Transformation (The Cleaning)**: Applied automated boolean masking to validate thresholds (dynamically filtering claims where `repair_cost > 1000` without manual intervention).
3. **Load (The Output)**: Processed outputs are tabulated relationally alongside programmatic Key Performance Indicator (KPI) summaries (Total Exposure, Average Cost, Approval Rate).

*View the pipeline script:* [`src/etl_pipeline.py`](./src/etl_pipeline.py)

---

### Phase 3: Dashboard Visualization & Insights
*(Coming Soon)* - Integrating relational datasets with front-end analytical interfaces for live performance monitoring.
