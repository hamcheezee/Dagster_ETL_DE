-- Before running this command, you should have executed the following command to copy the Parquet file from the dagster_etl_de-dagster-dagit-1 container to your local machine:
-- `docker cp dagster_etl_de-dagster-dagit-1:/warehouse_location/result/<filename.parquet> <path/to/exported/file>`
CREATE TABLE source__condition_occurrence AS FROM read_parquet('/Users/cheeze/Desktop/Dagster_ETL_DE/warehouse_location/result/read__condition_occurrence.parquet');
CREATE TABLE source__drug_exposure AS FROM read_parquet('/Users/cheeze/Desktop/Dagster_ETL_DE/warehouse_location/result/read__drug_exposure.parquet');
CREATE TABLE source__person AS FROM read_parquet('/Users/cheeze/Desktop/Dagster_ETL_DE/warehouse_location/result/read__person.parquet');
CREATE TABLE T_topten_condition_occurrence AS FROM read_parquet('/Users/cheeze/Desktop/Dagster_ETL_DE/warehouse_location/result/topten_condition_occurrence.parquet');
SHOW TABLES;