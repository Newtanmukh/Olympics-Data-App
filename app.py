import streamlit as st
import pandas as pd
import helper
 
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

st.sidebar.title("Olympics Analysis")

user_menu=st.sidebar.radio(
    'Select an option',
    ('Medal Tally','Overall Analysis','Country-wise Analysis','Athlete wise analysis')
    )







df=pd.read_csv('athlete_events.csv')

if user_menu=='Medal Tally':
    st.sidebar.header("Medal Tally")
    years,countries=helper.country_year_list()
    selected_year=st.sidebar.selectbox("Select Year",years)
    selected_country=st.sidebar.selectbox("Select Country",countries)
    
    if selected_year=='Overall' and selected_country=='Overall':
        st.title('Overall Tally')
    
    if selected_year!='Overall' and selected_country=='Overall':
        st.title('Medal Tally in '+str(selected_year)+' Olympics')
    
    if selected_year=='Overall' and selected_country!='Overall':
        st.title(selected_country + ' Overall Performance ')
        
    if selected_year!='Overall' and selected_country!='Overall':
        st.title(selected_country + ' Performance '+'in '+str(selected_year)+" Olympics")
    
    
    
    medals=helper.medal_tally(selected_year,selected_country)
    st.table(medals)








