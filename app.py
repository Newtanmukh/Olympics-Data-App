import streamlit as st
import pandas as pd

st.sidebar.radio(
    'Select an option',
    ('Medal Tally','Overall Analysis','Country-wise Analysis','Athlete wise analysis')
    )

df=pd.read_csv('athlete_events.csv')
region_df=pd.read_csv('noc_regions.csv')


def preprocess(df,region_df):
    # filtering for summer olympics
    df = df[df['Season'] == 'Summer']
    # merge with region_df
    df = df.merge(region_df, on='NOC', how='left')
    # dropping duplicates
    df.drop_duplicates(inplace=True)
    # one hot encoding medals
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
    return df


data=preprocess(df,region_df)

st.dataframe(data)