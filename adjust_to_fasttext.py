
import os
import glob
import pandas as pd
os.chdir("./")

symbols = []
out = []
extension = 'csv'
spooks = pd.read_csv(glob.glob('data/spooky-author-identification/train/train.csv')[0])


merged_csv = []

for row in spooks .iterrows():
    merged_csv.append(['__label__' + row[1]['author'], row[1]['text']])


df = pd.DataFrame(merged_csv, columns=['label', 'text'])
print(df)
pd.DataFrame(df).to_csv("data/out/spook_to_fasttext.csv")
