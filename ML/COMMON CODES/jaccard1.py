import pandas as pd

df = pd.read_excel("c:/Users/Desktop/ANES/ANES/GEN_AI_OUTPUTS/A21_GPT_LLAMA_PREDICTION_2020.xlsx")

count_o_g = 0.0
count_o_l = 0.0
count_g_l = 0.0

count = 0.0

for index, row in df.iterrows():
    if index>=0:
        count+=1.0
        if df.at[index, 'A21_original'] == df.at[index, 'A21_GPT']:
            count_o_g += 1.0
        if df.at[index, 'A21_original'] == df.at[index, 'A21_llama']:
            count_o_l += 1.0
        if df.at[index, 'A21_GPT'] == df.at[index, 'A21_llama']:
            count_g_l += 1.0

print("\n")    
print("ORIGINAL vs GPT: ")
print("Overlap Count: ", count_o_g)
print("Jaccard Index: ", count_o_g/count)
print("\n")
print("ORIGINAL vs LLAMA: ")
print("Overlap Count: ", count_o_l)
print("Jaccard Index: ", count_o_l/count)
print("\n")
print("GPT vs LLAMA: ")
print("Overlap Count: ", count_g_l)
print("Jaccard Index: ", count_g_l/count)
print("\n")
