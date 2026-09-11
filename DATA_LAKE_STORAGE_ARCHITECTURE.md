# DATA LAKE STORAGE ARCHITECTURE
## Partitioned Parquet & Query Optimization

Humphrey Virtual Farms manages petabytes of agronomic telemetry. To ensure sub-second analytical query performance and mitigate cloud compute bloat, all edge data undergoes structural transformation upon cloud ingestion.

### 1. Format Transformation
Raw JSON and CSV payloads are strictly prohibited in the Data Lake. All edge telemetry is transformed into columnar Apache Parquet format upon ingestion, ensuring high compression ratios and targeted column retrieval.

### 2. Deterministic Partitioning Schema
Data is not dumped into flat directories. The ingestion engine enforces a strict hierarchical partitioning schema: date={YYYY-MM-DD} / sector={SECTOR_ID} /.
This architecture guarantees that predictive machine learning models can query specific historical slices without executing costly, full-lake table scans.
