"""
import pandas as pd
life_ex = pd.read_csv('data/API_SP.DYN.LE00.IN_DS2_en_csv_v2_5358385.csv', skiprows=4)
health_ex = pd.read_csv('data/API_SH.XPD.CHEX.PC.CD_DS2_en_csv_v2_5359940.csv', skiprows=4)
# Only keep columns for life_ex: Country Name, 2019
life_ex = life_ex[['Country Name', '2019']]

# Only keep columns for life_ex: Country Name, 2019
health_ex = health_ex[['Country Name', '2019']]

# add new column in health_ex with life expectancy
health_ex['Life Expectancy at Birth (total years)'] = life_ex['2019']

# rename 2019 column to Health Expenditure per Capita (current US$)
health_ex.rename(columns={'2019': 'Health Expenditure per Capita (current US$)'}, inplace=True)

# Drop nans
health_ex.dropna(inplace=True)



# sort by Health Expenditure per Capita (current US$)
health_ex.sort_values(by='Health Expenditure per Capita (current US$)', ascending = False, inplace=True)

# reset index
health_ex.reset_index(drop=True, inplace=True)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
from sklearn.linear_model import LinearRegression
sns.set_theme()


# conditional plot for the year 2020
df_2020 = health_ex
plt.scatter(data=df_2020, x='Health Expenditure per Capita (current US$)', y='Life Expectancy at Birth (total years)', c='red', marker='o', s=10, alpha=0.5, label='2019')
# fit a linear model between log GDP and life expectancy
reg = LinearRegression().fit(np.log(df_2020['Health Expenditure per Capita (current US$)']).values.reshape(-1, 1), df_2020['Life Expectancy at Birth (total years)'].values.reshape(-1, 1))
# plot the linear model
x = np.linspace(start=4, stop=12, num=100)
y = reg.coef_[0][0] * x + reg.intercept_[0]
plt.plot(np.exp(x), y, alpha=0.5, c='darkred')

# annotate Japan with country name, make point bigger

for row in df_2020.index:
    if df_2020.loc[row, 'Country Name'] in ['Japan', 'Germany', 'Italy', 'United States']:
        plt.scatter(data=df_2020.loc[row, :], x='Health Expenditure per Capita (current US$)', y='Life Expectancy at Birth (total years)', c='black', marker='o', s=10, alpha=1)
        plt.text(x=df_2020.loc[row, 'Health Expenditure per Capita (current US$)'] + 0.2, y=df_2020.loc[row, 'Life Expectancy at Birth (total years)'] + 0.3 - 1.6*(df_2020.loc[row, 'Country Name'] == 'Germany'), s=df_2020.loc[row, 'Country Name'], fontsize=8)

    




# plt.legend(title='Year')  
plt.title('Life Expectancy vs Health Expenditure for Countries in 2019')
# plt.xscale('log')
# make y axis go from 0 to 100
plt.ylim(40, 90)
plt.xlim(0, 12000)
plt.xlabel('Health Expenditure per Capita (current US$)')
plt.ylabel('Life expectancy at Birth (years)')
plt.show()

"""
"""
import pandas as pd
physical_activity = pd.read_csv('data/physical_ac.csv')
# only include data for countries USA, Japan, Germany, Italy

physical_activity = physical_activity[physical_activity['Unnamed: 0'].isin(['United States of America', 'Japan', 'Germany', 'Italy'])]

# Only include columns Unnamed: 0 and Prevalence of insufficient physical activity among adults aged 18+ years (age-standardized estimate) (%)
physical_activity = physical_activity[['Unnamed: 0', 'Prevalence of insufficient physical activity among adults aged 18+ years (age-standardized estimate) (%)']]

# rename columns to Country Name
physical_activity.rename(columns={'Unnamed: 0': 'Country Name', 'Prevalence of insufficient physical activity among adults aged 18+ years (age-standardized estimate) (%)': 'Prevalence of Insufficient Physical Activity for 18+ Years Adults (age-standardized estimate)'}, inplace=True)

# In column Prevalence of insufficient physical activity among adults aged 18+ years (age-standardized estimate) (%) remove the 12 last characters
physical_activity['Prevalence of Insufficient Physical Activity for 18+ Years Adults (age-standardized estimate)'] = physical_activity['Prevalence of Insufficient Physical Activity for 18+ Years Adults (age-standardized estimate)'].str[:-12]

# In column Prevalence of insufficient physical activity among adults aged 18+ years (age-standardized estimate) (%) convert to float
physical_activity['Prevalence of Insufficient Physical Activity for 18+ Years Adults (age-standardized estimate)'] = physical_activity['Prevalence of Insufficient Physical Activity for 18+ Years Adults (age-standardized estimate)'].astype(float)

# sort by Prevalence of insufficient physical activity among adults aged 18+ years (age-standardized estimate) (%)
physical_activity.sort_values(by='Prevalence of Insufficient Physical Activity for 18+ Years Adults (age-standardized estimate)', ascending = False, inplace=True)

# reset index
physical_activity.reset_index(drop=True, inplace=True)

# Rename united states of america to United States
physical_activity['Country Name'] = physical_activity['Country Name'].str.replace('United States of America', 'United States')

import seaborn as sns
import matplotlib.pyplot as plt
# Make bar plot with countries on x axis and Prevalence of insufficient physical activity among adults aged 18+ years (age-standardized estimate) (%) on y axis in sns theme
sns.barplot(data=physical_activity, x='Country Name', y='Prevalence of Insufficient Physical Activity for 18+ Years Adults (age-standardized estimate)', palette="Blues_r")
plt.title('Prevalence of Insufficient Physical Activity for 18+ Years Adults - 2019')
plt.ylabel('%') 
plt.xlabel('Country')
plt.show()
"""


"""
import pandas as pd
sui = pd.read_csv('data/sui.csv')

# Only keep the first three columns 
sui = sui.iloc[:, :3]

# drop firs row
sui.drop(0, inplace=True)

sui['Age-standardized suicide rates (per 100 000 population)'] = sui['Age-standardized suicide rates (per 100 000 population)'].str[:4]

sui['Age-standardized suicide rates (per 100 000 population)'] = sui['Age-standardized suicide rates (per 100 000 population)'].astype(float)

sui = sui[sui['Unnamed: 1'] == 'Both sexes']

sui = sui[['Unnamed: 0', 'Age-standardized suicide rates (per 100 000 population)']]

# Only include countries 

sui = sui[sui['Unnamed: 0'].isin(['United States of America', 'Japan', 'Germany', 'Italy'])]

# sort by Prevalence of insufficient physical activity among adults aged 18+ years (age-standardized estimate) (%)
sui.sort_values(by='Age-standardized suicide rates (per 100 000 population)', ascending = False, inplace=True)

# reset index
sui.reset_index(drop=True, inplace=True)

# Rename united states of america to United States
sui['Unnamed: 0'] = sui['Unnamed: 0'].str.replace('United States of America', 'United States')

import seaborn as sns
import matplotlib.pyplot as plt
# Make bar plot with countries on x axis and Prevalence of insufficient physical activity among adults aged 18+ years (age-standardized estimate) (%) on y axis in sns theme
sns.barplot(data=sui, x='Unnamed: 0', y='Age-standardized suicide rates (per 100 000 population)', palette="Blues_r")
plt.title('Suicide Rates (per 100 000 population) - 2016')
plt.ylabel('Occurence/100000') 
plt.xlabel('Country')
plt.show()
"""

"""
import pandas as pd
exercise_df = pd.read_csv('data/exercise_dat.csv')
exercise_df

# sort by mu_hours
exercise_df.sort_values(by='mu_hours', ascending = False, inplace=True)
exercise_df
import seaborn as sns
import matplotlib.pyplot as plt
# Make bar plot with countries on x axis and Prevalence of insufficient physical activity among adults aged 18+ years (age-standardized estimate) (%) on y axis in sns theme
sns.barplot(data=exercise_df, x='Country', y='mu_hours', palette="Blues_r")
plt.title('Mean Number of Hours of Physical Exercise/week - 2021')
plt.ylabel('Hours') 
plt.xlabel('Country')
plt.show()
"""
"""
import pandas as pd
obese = pd.read_csv('data/obesity.csv')

import seaborn as sns
import matplotlib.pyplot as plt
# Make bar plot with countries on x axis and Prevalence of insufficient physical activity among adults aged 18+ years (age-standardized estimate) (%) on y axis in sns theme
sns.barplot(data=obese, x='name', y='value', palette="Greens_r")
plt.title('Obesity, Adult Prevalence - 2016')
plt.ylabel('%') 
plt.xlabel('Country')
plt.show()
"""
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
kalo = pd.read_csv('data/daily-per-capita-caloric-supply.csv')
kalo = kalo[kalo['Year']==2018]

kalo = kalo[kalo['Entity'].isin(['United States', 'Japan', 'Germany', 'Italy'])]


# sort by Prevalence of insufficient physical activity among adults aged 18+ years (age-standardized estimate) (%)
kalo.sort_values(by='Daily caloric supply (OWID based on UN FAO & historical sources)', ascending = False, inplace=True)

# reset index
kalo.reset_index(drop=True, inplace=True)


# Make bar plot with countries on x axis and Prevalence of insufficient physical activity among adults aged 18+ years (age-standardized estimate) (%) on y axis in sns theme
sns.barplot(data=kalo, x='Entity', y='Daily caloric supply (OWID based on UN FAO & historical sources)', palette="Greens_r")
plt.title('Daily Caloric Supply - 2018')
plt.ylabel('kcal') 
plt.xlabel('Country')
plt.show()
"""
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
oldest = pd.read_csv('GDP_data/life_cap.csv')
life_ex_df = pd.read_csv('GDP_data/life_expectancy_by_country.csv')

# make line plot in with both lines of oldest and life_ex_df
# set sns theme
sns.set_theme(style="darkgrid")
sns.lineplot(data=oldest, x='year', y='age', color = "green")
sns.lineplot(data=life_ex_df, x='year', y='age', color = "red")
plt.title('Oldest Person Alive vs. Life Expectancy at Birth (world)')
plt.ylabel('Age')
plt.xlabel('Year')
plt.legend(['Age of Oldest Person', 'Life Expectancy'])
plt.show()

"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# load data
#chosen quantile
Q= 0.9
## ITALY
#df_IT2000= pd.read_excel(r"C:\Users\david\Desktop\CORSI ORAAA\SOCIAL_DATA\FINAL PROJECT\project\social_data_project-master\Cause\italy2000.xlsx")
df_IT2019 = pd.read_excel("data/italy (1).xlsx")

df_IT2019=df_IT2019.sort_values(by=['Death rate per 100 000 population'],ascending=False)
z=df_IT2019['Death rate per 100 000 population'].quantile(q=Q,interpolation='linear')
df_IT2019_1=df_IT2019.loc[df_IT2019['Death rate per 100 000 population'] >= z]
## GERMANY
#df_GE2000= pd.read_excel(r"C:\Users\david\Desktop\CORSI ORAAA\SOCIAL_DATA\FINAL PROJECT\project\social_data_project-master\Cause\germany2000.xlsx")
df_GE2019 = pd.read_excel("data/germany (1).xlsx")
df_GE2019=df_GE2019.sort_values(by=['Death rate per 100 000 population'],ascending=False)

y=df_GE2019['Death rate per 100 000 population'].quantile(q=Q,interpolation='linear')
df_GE2019_1=df_GE2019.loc[df_GE2019['Death rate per 100 000 population'] >= y]

## JAPAN
#df_JA2000= pd.read_excel(r"C:\Users\david\Desktop\CORSI ORAAA\SOCIAL_DATA\FINAL PROJECT\project\social_data_project-master\Cause\japan2000.xlsx")
df_JA2019 = pd.read_excel("data/japan (1).xlsx")
df_JA2019= df_JA2019.sort_values(by=['Death rate per 100 000 population'],ascending=False)
df_JA2019
x=df_JA2019['Death rate per 100 000 population'].quantile(q=Q,interpolation='linear')

#// extract the top 50% of the data df_JA2019['Death rate per 100 000 population']
df_JA2019_1=df_JA2019.loc[df_JA2019['Death rate per 100 000 population'] >= x]

df_US2019 = pd.read_excel("data/united_states.xlsx")
df_US2019= df_US2019.sort_values(by=['Death rate per 100 000 population'],ascending=False)
df_US2019
w=df_US2019['Death rate per 100 000 population'].quantile(q=Q,interpolation='linear')

#// extract the top 50% of the data df_JA2019['Death rate per 100 000 population']
df_US2019_1=df_US2019.loc[df_US2019['Death rate per 100 000 population'] >= w]

print("IT:", df_IT2019_1.shape)
print("GE:", df_GE2019_1.shape)
print("JA:", df_JA2019_1.shape)
print("US:", df_US2019_1.shape)


#// plot with sns  3 barplot


fig, ax = plt.subplots(1,2, figsize=(20, 20), sharey=    False)
fig.suptitle('Top 5 Causes of Death by Country in 2019', fontsize=16)

sns.barplot(ax=ax[0], y="Death rate per 100 000 population", x="Cause", data=df_IT2019_1, palette="Blues_r")
ax[0].set_xticklabels(ax[0].get_xticklabels(), rotation=40, ha="right", fontsize=10)
ax[0].set_title('Italy 2019')
ax[0].set_ylabel('Death rate per 100 000 population')
ax[0].set_xlabel('Cause')
ax[0].set_ylim(0, 180)
sns.barplot(ax=ax[1], y="Death rate per 100 000 population", x="Cause", data=df_GE2019_1, palette="Blues_r")
ax[1].set_xticklabels(ax[1].get_xticklabels(), rotation=40, ha="right", fontsize=10)

ax[1].set_title('Germany 2019')
ax[1].set_ylabel('Death rate per 100 000 population')
ax[1].set_xlabel('Cause')
ax[1].set_ylim(0, 180)
#sns.barplot(ax=ax[2], y="Death rate per 100 000 population", x="Cause", data=df_JA2019_1, palette="Blues_r")

"""
ax[2].set_xticklabels(ax[2].get_xticklabels(), rotation=40, ha="right", fontsize=7)

ax[2].set_ylim(0, 180)


ax[2].set_title('Japan 2019')
ax[2].set_ylabel('Death rate per 100 000 population')
ax[2].set_xlabel('Cause')
"""
plt.show()


#// plot with sns  3 barplot


fig, ax = plt.subplots(1,2, figsize=(20, 5), sharey=    False)
fig.suptitle('Top 5 Causes of Death by Country in 2019', fontsize=16)

sns.barplot(ax=ax[0], y="Death rate per 100 000 population", x="Cause", data=df_IT2019_1, palette="Blues_r")
ax[0].set_xticklabels(ax[0].get_xticklabels(), rotation=40, ha="right", fontsize=10)
ax[0].set_title('Italy 2019')
ax[0].set_ylabel('Death rate per 100 000 population')
ax[0].set_xlabel('Cause')
ax[0].set_ylim(0, 180)
sns.barplot(ax=ax[1], y="Death rate per 100 000 population", x="Cause", data=df_GE2019_1, palette="Blues_r")
ax[1].set_xticklabels(ax[1].get_xticklabels(), rotation=40, ha="right", fontsize=10)

ax[1].set_title('Germany 2019')
ax[1].set_ylabel('Death rate per 100 000 population')
ax[1].set_xlabel('Cause')
ax[1].set_ylim(0, 180)
#sns.barplot(ax=ax[2], y="Death rate per 100 000 population", x="Cause", data=df_JA2019_1, palette="Blues_r")

"""
ax[2].set_xticklabels(ax[2].get_xticklabels(), rotation=40, ha="right", fontsize=7)

ax[2].set_ylim(0, 180)


ax[2].set_title('Japan 2019')
ax[2].set_ylabel('Death rate per 100 000 population')
ax[2].set_xlabel('Cause')
"""
plt.show()




