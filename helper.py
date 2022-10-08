import pandas as pd
import numpy as np

def medal_tally(year,country):
    flag=0
    
    country=str(country)
    year=str(year)
    df=pd.read_csv('athlete_events.csv')
    region_df=pd.read_csv('noc_regions.csv')
    temp_df=df
    temp_df = temp_df[temp_df['Season'] == 'Summer']
    # merge with region_df
    temp_df = temp_df.merge(region_df, on='NOC', how='left')
    # dropping duplicates
    temp_df.drop_duplicates(inplace=True)
    # one hot encoding medals
    temp_df = pd.concat([temp_df, pd.get_dummies(temp_df['Medal'])], axis=1)
    temp_df=temp_df.drop_duplicates(subset=['Team','NOC','Games','Season','Year','City','Sport','Event','Medal'])
    temp_df['Gold']=temp_df['Gold'].astype('int')
    temp_df['Silver']=temp_df['Silver'].astype('int')
    temp_df['Bronze']=temp_df['Bronze'].astype('int')
    
    if country=='Overall' and year=='Overall':
        pass
    if country=='Overall' and year!='Overall':
        temp_df=temp_df[temp_df['Year']==int(year)]
    if country!='Overall' and year=='Overall':
        flag=1
        temp_df=temp_df[temp_df['region']==country]
    if country!='Overall' and year!='Overall':
        temp_df=temp_df[(temp_df['region']==country) & (temp_df['Year']==int(year))]
    
    
    if flag==1:
        x = temp_df.groupby('Year').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Year',ascending=True).reset_index()
    else:
        x = temp_df.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold',ascending=False).reset_index()
    
    
    x['total']=x['Gold']+x['Silver']+x['Bronze']
    return x


def country_year_list():
    df=pd.read_csv('athlete_events.csv')
    region_df=pd.read_csv('noc_regions.csv')
    df = df[df['Season'] == 'Summer']
    # merge with region_df
    df = df.merge(region_df, on='NOC', how='left')
    # dropping duplicates
    df.drop_duplicates(inplace=True)
    # one hot encoding medals
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
    
    
    
    years=list(df['Year'].unique())
    years.sort()
    years.insert(0,'Overall')
    
    country=list(df['region'].dropna().unique())
    country.sort()
    country.insert(0,'Overall')
    
    return years,country
    
    
    