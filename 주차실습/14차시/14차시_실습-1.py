import pandas as pd

df = pd.read_csv('data/winequality-red.csv',dtype=float)


########################################코드##########################################
def encoding_quality(x):
	if x > 5:
		return 1
	else:
		return 0

df['quality'] = df['quality'].apply(encoding_quality)
#####################################################################################

print(len(df.loc[df['quality'] == 0]))
print(len(df.loc[df['quality'] == 1]))