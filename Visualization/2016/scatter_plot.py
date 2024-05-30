import matplotlib.pyplot as plt
import pandas as pd

df1 = pd.read_excel('c:/Users/Desktop/ANES/ANES/scatter_plots/2016/original_gain.xlsx')
df2 = pd.read_excel('c:/Users/Desktop/ANES/ANES/scatter_plots/2016/llama_gain.xlsx')
df3 = pd.read_excel('c:/Users/Desktop/ANES/ANES/scatter_plots/2016/gpt_gain.xlsx')

Human = df1['Feature'].tolist()[:7]
llama_7b = df2['Feature'].tolist()[:7]
gpt3_5 = df3['Feature'].tolist()[:7]

y_Human = df1['Feature importance(gain)'].tolist()[:7]
y_llama_7b = df2['Feature importance(gain)'].tolist()[:7]
y_gpt3_5 = df3['Feature importance(gain)'].tolist()[:7]

plt.grid()
plt.scatter(Human, y_Human, c ="black", 
			linewidths = 4, 
			marker ="s", 
			edgecolor ="black", 
			s = 80, label = 'Human')

plt.scatter(llama_7b, y_llama_7b, c ="orange",
			linewidths = 4,
			marker ="o", 
			edgecolor ="orange", 
			s = 100, label='llama7b')


plt.scatter(gpt3_5, y_gpt3_5, c ="purple",
			linewidths = 4,
			marker ="+", 
			# edgecolor ="red", 
			s = 120, label='GPT3.5')

plt.axhline(y=11.8, color='r', linestyle='-', xmin=0.018, xmax=0.418)
plt.axhline(y=0.15, color='r', linestyle='-', xmin=0.018, xmax=0.418)
plt.axvline(x=-0.25, color='r', linestyle='-', ymin=0.02, ymax=.952)
plt.axvline(x=3.28, color='r', linestyle='-', ymin=0.02, ymax=.952)

plt.axhline(y=3, color='b', linestyle='-', xmin=0.47, xmax=0.87)
plt.axhline(y=0.15, color='b', linestyle='-', xmin=0.47, xmax=0.87)
plt.axvline(x=3.73, color='b', linestyle='-', ymin=0.02, ymax=0.247)
plt.axvline(x=7.26, color='b', linestyle='-', ymin=0.02, ymax=0.247)

i=0
# plt.yticks([i*0.2 for i in range(1,35)])
for i, label in enumerate(plt.gca().get_xticklabels()):
    if i < 4:
        label.set_weight("bold")
        i+=1
# plt.text(1.5, 6.3, 'overlaping top features', ha='center', fontsize = 17)
        
plt.xticks(rotation=90, fontsize='18')
plt.yticks(fontsize='18')
plt.legend(fontsize='16')
plt.xlabel("Features of Voters / Persona's", fontweight='bold', fontsize='20')
plt.ylabel("xgb-LIME (GAIN)", fontweight='bold', fontsize='20')
plt.show()
