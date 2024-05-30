## ML_prediction_code_A21 (Single Choice).ipynb

a) Input: 1. dataset (all features)
	     file_path (example): "ANES/ANES/Gen_AI_Outputs/A21_GPT_LLAMA_PREDICTION_2020.xlsx"
	  2. ml model (loading ml model to make predictions)
	     file_path (example): "ANES/ANES/ML/MODELWISE/2020/LLAMA/rnn_model.keras"
b) Output: dataset (input dataset)
c) Run the only cell 


## ML_RNN_MODEL_TRAINING_A21 (Single Choice).ipynb

a) Input: 1. dataset (all features along with y_label column)
	     file_path: "ANES/ANES/Gen_AI_Outputs/A21_GPT_LLAMA_PREDICTION_2020.xlsx"
b) Output: 1. trainX.xlsx
	   2. trainY.xlsx
	   3. testX.xlsx
	   4. testY.xlsx
	   5. rnn_model.keras
	   6. predicty.csv
	   7. Accuracy.txt
	   **file_path example: "ANES/ML/MODELWISE/2020/Original/file_name" (1 to 6)
			        "ANES/ML/MODELWISE/2020/Original/Accuracy.txt" (7)
c) Run all the cells


## jaccard_1.py

a) Input: 1. dataset (all features)
	     file_path: "ANES/ANES/GEN_AI_OUTPUTS/A21_GPT_LLAMA_PREDICTION_2020.xlsx"
b) Output: On the terminal
c) Run the Python file in the terminal: python3 "ANES/ML/COMMON_CODES/jaccard1.py"



