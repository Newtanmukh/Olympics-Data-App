import pandas as pd
def medal_tally(df):
    region_df=pd.read_csv('noc_regions.csv')
    df = df[df['Season'] == 'Summer']
    # merge with region_df
    df = df.merge(region_df, on='NOC', how='left')
    # dropping duplicates
    df.drop_duplicates(inplace=True)
    # one hot encoding medals
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
    medal_df = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    medal_df=medal_df.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold',
                                                                                      ascending=False).reset_index()
    
    medal_df['Gold']=medal_df['Gold'].astype('int')
    medal_df['Silver']=medal_df['Silver'].astype('int')
    medal_df['Bronze']=medal_df['Bronze'].astype('int')
    medal_df['Total']=medal_df['Gold']+medal_df['Silver']+medal_df['Bronze']
    return medal_df