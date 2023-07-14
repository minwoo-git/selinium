import pandas as pd

df_data=pd.read_csv("data\CARD_SUBWAY_MONTH_201907.csv", encoding='CP949')
print(df_data)

#dataframe : 여러줄 / dictionary
#series : 한줄 / list

#column
print(df_data["노선명"]) #--> series

#row / index
print(df_data.loc[3]) # --> series

#
df_data[cond] #cond와 같이 조건을 넣으면 조건에 부합하는 dataframe을 내준다.