# Phase 3: Dashboard Visualization & Insights

## Dashboard Architecture & Stakeholder Alignment
Designed and implemented a cross-functional Business Intelligence Command Center in Power BI Desktop, transforming processed ETL flat-file data into multi-tiered interactive reporting arrays.

### 1. Executive & Finance View
- **Metrics Tracked**: Total Financial Exposure, Approval Conversion Rate.
- **Business Logic**: Summarizes direct cost liabilities to track immediate cash flow exposure and portfolio risk.

### 2. Risk & Dealer Operations View
- **Metrics Tracked**: Mean Time to Process (MTTP), Non-Approved High-Cost Flags.
- **Business Logic**: Isolates pending/denied claims over $1,000 to spot dealer-level processing bottlenecks or potential fraudulent activity.

### 3. Marketing Intelligence View
- **Metrics Tracked**: Regional Claim Distributions.
- **Business Logic**: Cross-references asset data with transactional frequencies to assist marketing teams in localized warranty underwriting.

### 4. Product & Engineering View
- **Metrics Tracked**: Make, Model, and Year Failure Rates.
- **Business Logic**: Utilizes aggregated transaction data to identify mechanical failure rates and component durability baselines.

---
*View Dashboard Template File*: [`/dashboards/AutoGuard_Command_Center.pbix`](./dashboards/AutoGuard_Command_Center.pbix)
