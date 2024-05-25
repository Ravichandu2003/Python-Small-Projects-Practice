import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

fifa = pd.read_csv('players_20.csv')
#print(fifa.head())
#for col in fifa.columns:
#    print(col)
#print(fifa.shape)
#print(fifa['nationality'].value_counts())
#print(fifa['nationality'].value_counts()[0:10])
#print(fifa['nationality'].value_counts()[0:5].keys())
plt.figure(figsize=(8,5))
plt.bar(list(fifa['nationality'].value_counts()[0:5].keys()),list(fifa['nationality'].value_counts()[0:5]),color="g")
#print(plt.show())
player_salary =  fifa[['short_name','wage_eur']]
#print(player_salary)
#salaries in an order
player_salary = player_salary.sort_values(by=['wage_eur'],ascending=False)
#print(player_salary)
plt.bar(list(player_salary['short_name'].value_counts()[0:5].keys()),list(player_salary['wage_eur'].value_counts()[0:5]),color=['blue','red','pink','orange','yellow'])
print(plt.show())
