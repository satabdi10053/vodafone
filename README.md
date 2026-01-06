**Title :      Take home assignment - Medior  (WIP)**

****Deliverable 1: ** A draft Airflow DAG or PySpark pipeline showing your design and approach**

**Description** :** Below is a complete, end to end design and working for your telecom network metrics pipeline using the Medallion architecture (bronze → silver → gold), orchestrated by Apache Airflow . .

**Requirements**: Python 3.9
**Dependencies** :   For Orchestration apache-airflow , Data Processing	[pyspark, pandas , numpy]  and Storage Format	pyiceberg or delta-spark 

**Created Files For You :**

**Created Files :** •	**DAG: src/vodafone_network_pipeline.py**

**Medallion Architecture Overview**

 1. **RAW Data in S3** :
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
     
    
   **Deliverable 2 : Example mock table views for bronze, silver, and gold layers (CSV )**
   
   Bronze sample (Raw)
   Example of Bronze Path: Deliverables 2/bronze [Code]

   Silver Sample (Cleaned)
   Example of Silver Path : Deliverables 2/Silver 

   Gold Sample (Business)
   Example of Gold Path : Deliverables 2/Gold

  **Deliverable 3 :  Example validation logs showing errors and how they are handled**
  
  1. Metadata :
     The raw file being checked first :network_metrics_20250723.csv
     
  2. Checks :
      • file naming pattern
      • Confirming the file name matches the expected pattern -network_metrics_YYYYMMDD.csv
      • file exist in Raw Path
      • Ensure all required columns are present
      • Row Count
      • Null checks
      • Ensure no corrupted values
      • duplicate_checks
     
  3. Action :
      • If any check failed ,the file would be moved to a quarantine bucket
      • notification would be sent to respected team
      • The pipeline would be stopped


      **Data Models: What would be the proposed data models across the layers? Why**

     we will apply medallion architecture.

     Bronze(Raw, Append Only):
     Table : bronze/network_metrics
     Partition: Date=YYYY-MM-DD
     WHY: • no transformation that could hide the issue
          • execute the pipeline anytime because the raw structure is preserved.
          • Only append so it is good for auditing

     Silver (Cleaned)
     Why: • Enforcing Datatypes and human readable Timestamp
          • Drop duplicates, Column fixing, apply validation flag


     Gold (Business Ready)
     Why: • designed for Dashboard
          • Good for trend analysis

     **Monitoring & Alerting**

     How would you add incident notifications?
     • whenever airflow task fails , it can run python program to send message to Teams.
     And the alerts include DAG Id, Task id [ which step], Failure reason, logs link. [Code is in the monitoring section]
     •If for critical alert this is done through Pager/Opsgenie.

     **Alert Strategy**
     **Critical (immediate oncall page)**
     1. Pipeline wide issue 
     2. Step wise issue 
    
     **1. Pipeline wide issue --**
          • Dashboard may show stale data
          • SLAs will be missed
          • downstream data will be late
     **2. Stepwise issue**
          • If Raw file is missing , then pipeline is blocked. -Critical alert
          • Data quality issue for column mismatch - Critical
          • irregular Data- Warning


      **Superset (Optional)**

        •	Create charts:
          1.	Total data_volume_mb per region per hour (from gold hourly)
          2.	Average signal_strength per region per day (from gold daily)

     

     

     



     
     

   
     
    
     
     
          
            



