import pymssql
import pandas as pd
"""
sql server로부터 db 정보 추출 및 dataframe화
"""
conn = pymssql.connect(server = SERVER, user = USERNAME, password = PASSWORD, database = DB)
query = """
SELECT A, B, C, ...
FROM [SKMR_DATA].[SKST_DATA].[SKInc_DATA]
LEFT JOIN [SKMATA_DATA]
ON SKInc_DATA.akey = SKMATA_DATA.bkey
WHERE SKST_DATA.MATDATE = 'caes1'
"""
df = pd.read_sql(query, conn)
conn.close()
