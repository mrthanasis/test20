import os
cwd = os.getcwd()

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=cwd+"\My-Project-2020-c7c568ac149d.json"
import google.auth
import google.auth.transport.requests
from google.cloud import bigquery
client = bigquery.Client()
import pandas as pd
import numpy as np

def lastdaysresults(x):
    x=int(x)
    query=("""
    select a.UserType,a.deviceCategory, sum(a.transactions) as Conversions, sum(a.visits) as Impressions,
    sum(a.transactions)/ sum(a.visits) as Convertion_rate , a.lastdays, a.date
    from (select case when visitNumber=1 then 'New' else 'Return' end as UserType, device.deviceCategory, totals.transactions, totals.visits,
    DENSE_RANK() OVER(ORDER BY CAST(date AS INT64) DESC) AS lastdays, date
    from `bigquery-public-data.google_analytics_sample.ga_sessions_*`) a
    where lastdays<={}
    group by a.lastdays,a.date, UserType, a.deviceCategory"""
    ).format(str(x*2))
    query_job = client.query(
    query,
    # Location must match that of the dataset(s) referenced in the query.
    location="US")
    df=query_job.result().to_dataframe()
    
    lastxdays=df.groupby(['lastdays','date']).sum().eval("Conversion_rate=Conversions/Impressions")\
    .query('lastdays<={}'.format(x)).reset_index().set_index('date')[['Conversion_rate']]
    
    
    periods=df.assign(Period=np.where(df['lastdays']<=x,'ThisPeriod','PastPeriod')).groupby('Period').sum()\
    .eval("Conversion_rate=Conversions/Impressions")[['Conversion_rate']]
    
    breakdown=df.assign(Period=np.where(df['lastdays']<=x,'ThisPeriod','PastPeriod')).groupby(['Period','UserType','deviceCategory'])\
    .sum().eval("Conversion_rate=Conversions/Impressions")[['Conversion_rate']].reset_index()
    
    
    return(lastxdays.to_dict(),periods.to_dict(),breakdown.to_dict())