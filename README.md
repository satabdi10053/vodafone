**Title :      Take home assignment - Medior  (WIP)**
**Deliverable 1: ** A draft Airflow DAG or PySpark pipeline showing your design and approach

**Description** :** Below is a complete, end to end design and working for your telecom network metrics pipeline using the Medallion architecture (bronze → silver → gold), orchestrated by Apache Airflow . .

**Requirements**: Python 3.9
**Dependencies** :   For Orchestration apache-airflow , Data Processing	[pyspark, pandas , numpy]  and Storage Format	pyiceberg or delta-spark 

**Created Files For You :**

**Creaed Files :** •	**DAG: src/vodafone_network_pipeline.py**

**Medallion Architecture Overview**
 1.**RAW Data in S3** :
     Path: S3/raw-telecom-network-data/network_metrics_20250723.csv ---Nothing is validated yet, it is just the raw dump
 2. **Airflow S3KeySensor** 
     Confirms the file is present
 3. **Bronze Layer (Raw)**
     • Stored in S3/Iceberg
     **Characteristics:**
     • Append 
     • Correct Column Types
     **Purpose**
     • Preserve the raw data exactly as received
 4. **Transformation**
    **Timestamp Conversion:**
     • Convert Unix timestamps to human-readable datetime.
    **Data Quality Checks**
     • Null Checks
     • Duplicate Detection
     • Schema Validation
 5. **Silver Layer (Cleaned)**
     • Clean and validated rows
     • Data type review
     • Convert timestamp
     • Aggregate data by region and hour:
           Total data_volume_mb per region per hour.
           Average signal_strength per region per hour.
 6. **Gold Layer (Business Aggregates)**
     • Total data_volume_mb per region (daily)
     • Average signal_strength per region (daily)

      Final dataset used for Reporting and Dashboard.
 7. **Superset Dashboard**
      Superset connects to Iceberg tables.
     • Daily performance
     • Regional comparison
     • Hourly Trends
     
    
   ** Deliverable 2** : Example mock table views for bronze, silver, and gold layers (CSV or SQL)
   Bronze sample (Raw)
   Example of Bronze Path: Deliverables 2/bronze [Code]

   Silver Sample (Cleaned)
   Example of Silver Path : Deliverables 2/Silver 

   Gold Sample (Business)
   Example of Gold Path : Deliverables 2/Gold
   
     
    
     
     
          
            



