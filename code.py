# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
data = pd.read_csv(path)
data.rename(columns = {'Total':"Total_Medals"}, inplace = True)
data.head()
#Code starts here



# --------------
#Code starts here
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'], 'Summer', 'Winter')
data['Better_Event'] = np.where(data['Total_Summer'] == data['Total_Winter'], 'Both', data['Better_Event'])
better_event = data['Better_Event'].value_counts().index.values[0]
print('Better_Event', better_event)



# --------------
#Code starts here
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

top_countries = data[['Country_Name', 'Total_Summer', 'Total_Winter','Total_Medals']]
top_countries= top_countries[:-1] 
def top_ten(data, col):
    country_list = []
    country_list=list((data.nlargest(10,col)['Country_Name']))
    return country_list
top_10_summer = top_ten(top_countries,'Total_Summer')
print('Top_10_Summer:\n',top_10_summer,'\n')
top_10_winter = top_ten(top_countries,'Total_Winter')
print('Top_10_Winter:\n', top_10_winter,'Total_Winter')
top_10 = top_ten(top_countries,'Total_Medals')
print('Total_Medals:\n',top_10,'\n')
common = list(set(top_10_summer) & set(top_10_winter) & set(top_10))
print('Common Countries :\n',common,'\n')


# --------------
#Code starts here
import matplotlib.pyplot as plt
summer_df=data[data['Country_Name'].isin(top_10_summer)]
winter_df=data[data['Country_Name'].isin(top_10_winter)]
top_df=data[data['Country_Name'].isin(top_10)]
plt.figure(figsize=(20,20))
plt.bar(top_df['Country_Name'], top_df['Total_Medals'])
plt.title('Top 10')
plt.xlabel('Country_Name')
plt.ylabel('Total Medals')


# --------------
#Code starts here
import matplotlib.pyplot as plt
summer_df['Golden_Ratio']=summer_df['Gold_Summer'] / summer_df['Total_Summer']
summer_max_ratio=max(summer_df['Golden_Ratio'])
summer_country_gold=summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']
winter_df['Golden_Ratio']=winter_df['Gold_Winter'] / winter_df['Total_Winter']
winter_max_ratio=max(winter_df['Golden_Ratio'])
winter_country_gold=winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']
top_df['Golden_Ratio'] = top_df['Gold_Total'] / top_df['Total_Medals']
top_max_ratio=max(top_df['Golden_Ratio'])
top_country_gold=top_df.loc[top_df['Golden_Ratio'].idxmax(), 'Country_Name']



# --------------
#Code starts here
data_1 = data[:-1]
data_1['Total_Points'] = data_1['Gold_Total'] * 3 + data_1['Silver_Total'] *2 + data_1['Bronze_Total']*1
most_points = max(data_1['Total_Points'])
best_country = data_1.loc[data_1['Total_Points'].idxmax(), 'Country_Name']
print('The maximum points acheived is ', most_points, 'by',best_country)


# --------------
#Code starts here
best = data[data['Country_Name'] == best_country]
best = best[['Gold_Total', 'Silver_Total', 'Bronze_Total']]
best.plot.bar(stacked = True)
plt.xlabel('United States')
plt.ylabel('Medals')
plt.xticks(rotation = 45)



