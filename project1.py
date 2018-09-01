import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from pandas import read_excel
import numpy as np
import openpyxl
import re
df=pd.read_excel('dataset1.xlsx')
name=df[['Name']][df.Year=='3rd']
email=df[['Email']][df.Year=='3rd']
name_array=np.array(name)
email_array=np.array(email)
first=" "
first_name=" "
last=" "
last_name=" "
name_list=" "
list_in=" "
for i in range(0,len(name_array)):
    name_data=name_array[i]
    email_data=email_array[i]
    for j in range(0,len(name_data)):
        name1=name_data[j].split(' ')
        email1=email_data[j].split('@gmail.com')
        for k in enumerate(name1):
            for m in range(len(k)):
                if (m==0):
                    if(k[m]==0):
                        first=k[1]
                        first_name=first.lower()
                    elif(k[m]==1):
                        last=k[1]
                        last_name=last.lower()
        for n in enumerate(email1):
            for p in range(len(n)):
                if (p==0):
                    if(n[p]==0):
                        sub=n[1]
                        sub_email=sub.lower()
        match1=re.search(first_name,sub_email)
        match2=re.search(last_name,sub_email)
        if (match1)or(match2):
            name_list=name_data
            for c in range(0,len(name_list)):
                list_in=np.extract(name==name_list,name_array)[c]
                df=df[df.Name!=list_in]
df.reset_index(inplace=True)
df.drop("index",axis=1,inplace=True)
writer=pd.ExcelWriter('NEW_DATASET.xlsx',engine='openpyxl')
df.to_excel(writer,'Sheet1')
writer.save()
df=pd.read_excel('NEW_DATASET.xlsx')
ME=len(df[df.Department=='ME'])
CE=len(df[df.Department=='CE'])
length=len(df)
req=int(0.1*length)
ME_CE=ME+CE
print(length,"STUDENTS ARE ENROLLED FOR DrAIveX\n")
if (length>30)and(ME_CE>=req):
    print("BINGO GUYS!!DrAIveX CAN NOW EXIST IN NSEC\n")
elif(length>30)and(ME_CE<req):
    print("SORRY GUYS!!GET MORE MECHANICAL AND CIVIL DEPARTMENT PEOPLE ON BOARD TO GET STARTED WITH DrAIveX\n")
else:
    print("EXTREMELY SORRY!!YOU GUYS NEED TO WORK REALLY HARD TO MAKE DrAIveX POSSIBLE IN NSEC\n")

            
                 
    

