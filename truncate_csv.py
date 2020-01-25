import pandas as pd 

csv_data=pd.read_csv("/home/mridu/Desktop/bank/indian_banks/bank_branches.csv")[:10000]
csv_data.to_csv("/home/mridu/Desktop/bank/indian_banks/bank_branches1.csv", index=False)