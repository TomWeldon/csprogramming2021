import pandas as pd
import re
import matplotlib.pyplot as plt

logFilename = 'access.log'



colNames = ('ip','dash1','userId','time','url','status code','size of response','referer','user agent','dunno')
df = pd.read_csv(logFilename,sep=' ', header=None, names=colNames)
df.drop(columns=['dash1','userId','dunno'], inplace=True)
#get rid of [] i 'time'
def getNewValue(x):
    newvalue = re.search('[\w:/]+',x).group()
    return newvalue
# New col contents
def sessionId(x):
    newSessionCol= re.search('(?<=D=)(.*)(?= HTTP)',x).group()
    return newSessionCol
# Making new column and populating it
df['session ID'] = df['url'].apply(sessionId)

#df['time'] = df['time'].apply(getNewValue)
#chamge 'time' format
#df['time']= pd.to_datetime(df['time'], format='%d/%b/%Y:%H:%M:%S')
# Set time to be index
#df = df.set_index(['time'])
excelFilename = 'access.xlsx'
df.to_excel(excelFilename, index=True, sheet_name='data')
#summary = df['size of response'].sum()
summary = df.groupby('session ID', as_index=False).agg({'size of response': 'sum'})
summary = summary.sort_values('size of response', ascending = False).head(10)
print(summary)
#summary = 'aggSessionID.xlsx'
#df.to_excel(summary, index=True,sheet_name='aggregate')
#print(df.iloc[1])
#print(df.dtypes)


