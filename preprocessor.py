import pandas as pd
df=pd.read_csv('athlete_events.csv')
region_df=pd.read_csv('noc_regions.csv')

def preprocess():
       
        
        #Getting only the athelete data who participated in the summer
        df=df[df['Season']=='Summer']
        
        #merge with region_df
        df=df.merge(region_df,on='NOC',how='left')
        
        #Dropping duplicates
        df=df.drop_duplicates(inplace=True)
        
        #One hot encoding medals
        df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
        
        return df