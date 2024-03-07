#extract data from postgresql
from dagster import  asset 
from etl.resources.db_conn import get_postgres_conn
import pandas as pd
import logging


#Transform data from database 
@asset(group_name="Transform", compute_kind="pandas" , io_manager_key="file_io")
def topten_condition_occurrence(context) -> pd.DataFrame:
    """Extract Data from Postgresql."""
    conn = get_postgres_conn()
    cursor = conn.cursor()
    query =  """
        SELECT 
            condition_concept_id, 
            COUNT(*) AS count,
            ROW_NUMBER() OVER (ORDER BY COUNT(*) DESC) AS ranking
        FROM 
            public.source__condition_occurrence
        GROUP BY 
            condition_concept_id
        ORDER BY 
            COUNT(*) DESC
        LIMIT 10;
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
        
    # Convert the fetched rows to a DataFrame
    df = pd.DataFrame(rows, columns=[desc[0] for desc in cursor.description])
    context.log.info(df.head())
    return df

@asset(group_name="Transform", compute_kind="pandas" , io_manager_key="file_io")
def topten_drug_exposure(context) -> pd.DataFrame:
    # pass
    """Extract Data from Postgresql."""
    conn = get_postgres_conn()
    cursor = conn.cursor()
    query =  """
        SELECT 
            drug_source_concept_id, 
            COUNT(*) AS count,
            ROW_NUMBER() OVER (ORDER BY COUNT(*) DESC) AS ranking
        FROM 
            public.source__drug_exposure
        GROUP BY 
            drug_source_concept_id
        ORDER BY 
            COUNT(*) DESC
        LIMIT 10;
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
        
    # Convert the fetched rows to a DataFrame
    df = pd.DataFrame(rows, columns=[desc[0] for desc in cursor.description])
    context.log.info(df.head())
    return df