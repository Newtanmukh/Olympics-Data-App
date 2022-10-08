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
    ('Medal Tally','Overall Analysis')
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

if user_menu=='Overall Analysis':
    df=pd.read_csv('athlete_events.csv')
    region_df=pd.read_csv('noc_regions.csv')
    df=preprocess(df,region_df)
    
    editions = df['Year'].unique().shape[0] - 1
    cities = df['City'].unique().shape[0]
    sports = df['Sport'].unique().shape[0]
    events = df['Event'].unique().shape[0]
    athletes = df['Name'].unique().shape[0]
    nations = df['region'].unique().shape[0]
    
    st.title("Top Statistics")
    col1,col2,col3 = st.columns(3)
    with col1:
        st.header("Editions")
        st.title(editions)
    with col2:
        st.header("Hosts")
        st.title(cities)
    with col3:
        st.header("Sports")
        st.title(sports)

        
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Events")
        st.title(events)
    with col2:
        st.header("Nations")
        st.title(nations)
    with col3:
        st.header("Athletes")
        st.title(athletes)




