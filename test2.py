import pandas as pd

df_pr=pd.read_csv("data\CARD_SUBWAY_MONTH_201907.csv", encoding='CP949')
print(df_pr)


print(df_pr["사용일자"])

