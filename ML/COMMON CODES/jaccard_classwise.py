import pandas as pd

df = pd.read_excel("c:/Users/Desktop/ANES/ANES/GEN_AI_OUTPUTS/A21_GPT_LLAMA_PREDICTION_2020.xlsx")

count_o_g = [0.0]*2
count_o_l = [0.0]*2
count_g_l = [0.0]*2

count = [0.0]*2

for index, row in df.iterrows():
    for i in range(1,3):
        if df.at[index, 'A21_llama']==i:
            count[i-1]+=1.0
            if df.at[index, 'A21_original'] == df.at[index, 'A21_GPT']:
                count_o_g[i-1] += 1.0
            if df.at[index, 'A21_original'] == df.at[index, 'A21_llama']:
                count_o_l[i-1] += 1.0
            if df.at[index, 'A21_GPT'] == df.at[index, 'A21_llama']:
                count_g_l[i-1] += 1.0

for i in range(1, 3):
    print("\nA21_Class "+str(i))
    print("\n")       
    print("ORIGINAL vs GPT: ")
    print("Overlap Count: ", count_o_g[i-1])
    if count[i-1]==0:
        print("Jaccard Index: ", 0)   
    else:
        print("Jaccard Index: ", count_o_g[i-1]/count[i-1])   
    print("\n")
    print("ORIGINAL vs LLAMA: ")
    print("Overlap Count: ", count_o_l[i-1])
    if count[i-1]==0:
        print("Jaccard Index: ", 0) 
    else:
        print("Jaccard Index: ", count_o_l[i-1]/count[i-1])
    print("\n")
    print("GPT vs LLAMA: ")
    print("Overlap Count: ", count_g_l[i-1])
    if count[i-1]==0:
        print("Jaccard Index: ", 0) 
    else:
        print("Jaccard Index: ", count_g_l[i-1]/count[i-1])
    print("\n")

# print("\n")    
# print("GPT3 vs GPT 3.5: ")
# print("Overlap count: ", count_3_3_5)
# print("Jaccard index: ", count_3_3_5/count)

# print("\n")    
# print("LLAMA vs GPT 3.5: ")
# print("Overlap count: ", count_LL_3_5)
# print("Jaccard index: ", count_LL_3_5/count)

# print("\n")    
# print("LLAMA vs GPT 3: ")
# print("Overlap count: ", count_LL_3)
# print("Jaccard index: ", count_LL_3/count)

