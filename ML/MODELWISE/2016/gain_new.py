import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df1 = pd.read_excel('c:/Users/Desktop/ANES/ANES/ML/MODELWISE/2016/ORIGINAL/feature_analysis.xlsx')
df2 = pd.read_excel('c:/Users/Desktop/ANES/ANES/ML/MODELWISE/2016/LLAMA/feature_analysis_llama.xlsx')
df3 = pd.read_excel('c:/Users/Desktop/ANES/ANES/ML/MODELWISE/2016/GPT/feature_analysis_gpt.xlsx')

# Sample data
Human = df1['Feature'].tolist()[:5]
llama_7b = df2['Feature'].tolist()[:5]
gpt3_5 = df3['Feature'].tolist()[:5]
# gpt3 = df4['Feature'].tolist()[:5]

# Human = [feature + '_h' for feature in Human]
# llama_7b = ["   "+feature for feature in llama_7b]
# gpt3_5 = ['  ' + feature for feature in gpt3_5]
# gpt3 = [' ' + feature for feature in gpt3]

# Create a main effects plot
fig, ax = plt.subplots()

x = ['Human', 'llama_7b', 'GPT3.5', 'GPT3']

# Plot main effects for factor A with markers
ax.plot(x[0], [df1['Feature importance(gain)'].tolist()[:5]], marker='o', label='Human')

# Plot main effects for factor B with markers
ax.plot(x[1], [df2['Feature importance(gain)'].tolist()[:5]], marker='o', label='llama_7b')

# Plot main effects for factor C with markers
ax.plot(x[2], [df3['Feature importance(gain)'].tolist()[:5]], marker='o', label='GPT3.5')

# Plot main effects for factor D with markers
# ax.plot(x[3], [df4['Feature importance(gain)'].tolist()[:5]], marker='o', label='GPT3')

ax.set_xlabel("Features of Voters / Persona's")
ax.set_ylabel('xgb-LIME (GAIN)')
ax.set_title('Feature Analysis')
plt.xticks(rotation=90)
# ax.legend()

# ax.grid(True)  # Add grid

llama_an = [0]*5
gpt3_5_an = [0]*5
# gpt3_an = [0]*5
for i in range(0,5):
    for j in range(0,5):
        if Human[i]==llama_7b[j]:
            ax.plot([x[0], x[1]], [df1['Feature importance(gain)'].tolist()[:5][i], df2['Feature importance(gain)'].tolist()[:5][j]], linestyle='-', color='gray', alpha=0.5)
            llama_an[j] = 1
        if Human[i]==gpt3_5[j]:
            ax.plot([x[0], x[2]], [df1['Feature importance(gain)'].tolist()[:5][i], df3['Feature importance(gain)'].tolist()[:5][j]], linestyle='-', color='gray', alpha=0.5)
            gpt3_5_an[j]=1
        # if Human[i]==gpt3[j]:
        #     ax.plot([x[0], x[3]], [df1['Feature importance(gain)'].tolist()[:5][i], df4['Feature importance(gain)'].tolist()[:5][j]], linestyle='-', color='gray', alpha=0.5)
        #     gpt3_an[j] = 1
for i in range(0,5):
    for j in range(0,5):
        if llama_7b[i]==gpt3_5[j]:
            ax.plot([x[1], x[2]], [df2['Feature importance(gain)'].tolist()[:5][i], df3['Feature importance(gain)'].tolist()[:5][j]], linestyle='-', color='gray', alpha=0.5)
            gpt3_5_an[j]=1
        # if llama_7b[i]==gpt3[j]:
        #     ax.plot([x[1], x[3]], [df2['Feature importance(gain)'].tolist()[:5][i], df4['Feature importance(gain)'].tolist()[:5][j]], linestyle='-', color='gray', alpha=0.5)
        #     gpt3_an[j]=1
# for i in range(0,5):
#     for j in range(0,5):
#         if gpt3_5[i]==gpt3[j]:
#             ax.plot([x[2], x[3]], [df3['Feature importance(gain)'].tolist()[:5][i], df4['Feature importance(gain)'].tolist()[:5][j]], linestyle='-', color='gray', alpha=0.5)
#             gpt3_an[j]=1

for i in range(0,5):
    ax.annotate(text=Human[i], xy=(x[0], [df1['Feature importance(gain)'].tolist()[:5]][0][i]))
for i in range(0,5):
    if llama_an[i]==0:
        ax.annotate(text=llama_7b[i], xy=(x[1], [df2['Feature importance(gain)'].tolist()[:5]][0][i]))
for i in range(0,5):
    if gpt3_5_an[i]==0:
        ax.annotate(text=gpt3_5[i], xy=(x[2], [df3['Feature importance(gain)'].tolist()[:5]][0][i]))
# for i in range(0,5):
#     if gpt3_an[i]==0:
#         ax.annotate(text=gpt3[i], xy=(x[3], [df4['Feature importance(gain)'].tolist()[:5]][0][i]))
# ax.set_ylim(0, 2)
plt.yscale("log")
plt.show()
