import re 
import os
import pandas as pd

# path = '/home/Desktop/Political_Category_Voting_GPT/'
# Read the XLSX file
df = pd.read_excel("c:/Users/Desktop/ANES/llama_queries_ANES.xlsx")
# df1 = pd.read_excel("C:/Users/Desktop/All_models_GPT.5/g2ans.xlsx")

if 'option' not in df.columns:
    df['option'] = None



for index, row in df.iterrows():
    if index>=0:
        string = str(df.at[index, 'answer'])
        # pattern1 = r"(\d+)"
        # match1 = re.search(pattern1, string)
        # project = 0
        # if match1:
        #     project = match1.group(1)
        project = df.at[index, 'option'] 
        l = string.split()
        for i in range(len(l)):
            if l[i] == 'over':
                if l[i-1] == 'Obama':
                    project = 2
                elif l[i-1] == 'Romney':
                    project = 1
                if l[i-1] == 'Trump':
                    project = 1
                elif l[i-1] == 'Clinton':
                    project = 2
                if l[i-1] == 'Trump':
                    project = 1
                elif l[i-1] == 'Biden':
                    project = 2
            if 'Trump' in l and ('Biden' not in l and 'Clinton' not in l):
                project = 1
            elif ('Biden' in l or 'Clinton') and 'Trump' not in l:
                project = 2
            if 'Obama' in l and 'Romney' not in l:
                project = 2
            elif 'Romney' in l and 'Obama' not in l:
                project = 1


        df.at[index, 'option'] = project

df.to_excel('c:/Users/Desktop/ANES/llama_queries_ANES.xlsx', index=False)
