
import os
import glob
import pandas as pd
os.chdir("./")

symbols = []
out = []
extension = 'csv'
spooks = pd.read_csv(glob.glob('data/spooky-author-identification/train.csv')[0])

author_to_bin = ""

merged_csv = []

for row in spooks .iterrows():
    print(row[1])
    merged_csv.append([row[1]['text'], row[1]['author'] == 'HPL', row[1]['author'] == 'EAP', row[1]['author'] == 'MWS'])


df = pd.DataFrame(merged_csv, columns=['text', 'is_HPL', 'is_EAP', 'is_MWS'])
print(df)
pd.DataFrame(df).to_csv("data/out/spook_to_lstm.csv", index=False)
