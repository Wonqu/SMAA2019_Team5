
import os
import glob
import pandas as pd
os.chdir("./")

symbols = []
out = []
extension = 'csv'
spooks = pd.read_csv(glob.glob('data/spooky-author-identification/train.csv')[0])

eap = pd.read_csv(glob.glob('data/out/eap.csv')[0])
hpl = pd.read_csv(glob.glob('data/out/hpl.csv')[0])
mws = pd.read_csv(glob.glob('data/out/mws.csv')[0])

mamatrix = [spooks. as_matrix(), eap.as_matrix(), hpl.as_matrix(), mws.as_matrix()]

merged_csv = []

# we iterate to length of longest
for i in range(0, len(spooks)):
    for matrix in mamatrix:
        if i < len(matrix):
            print(matrix[i])
            merged_csv.append(['__label__' + matrix[i][2] + ' ' + matrix[i][1]])

df = pd.DataFrame(merged_csv, columns=['label'])
print(df)
pd.DataFrame(df).to_csv("data/out/spook_to_fasttext.csv", index=False, header=False)
