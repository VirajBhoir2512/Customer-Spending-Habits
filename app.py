import pickle
import pandas as pd
import streamlit as st

st.set_page_config(page_title='Spending habits',page_icon='💹',layout='wide')

with open('Pipeline.pkl','rb') as file:
    pipeline=pickle.load(file)

data=pd.read_csv('cleaned_data.csv')
st.header('Customer Spending Habits')
with st.container():
    col1,col3,col2=st.columns([4,1,3])
    with col1:
        Age=st.slider(label='Age',min_value=18,max_value=100)
        Annual_Income=st.slider(label='Annual_Income',min_value=150000,max_value=2000000)
        Website_Visits=st.slider(label='Website_Visits',min_value=1)
        Previous_Purchases=st.slider(label='Previous_Purchases',min_value=0)
    with col2:
        Membership_Type=st.radio('Membership_Type',options=data['Membership_Type'].unique(),horizontal=True)
        Preferred_Category=st.radio('Preferred_Category',options=data['Preferred_Category'].unique(),horizontal=True)
        City_Tier=st.radio('City_Tier',options=data['City_Tier'].unique(),horizontal=True)
        Discount_Used=st.radio('Discount_Used',options=data['Discount_Used'].unique(),horizontal=True)

data={
'Age':Age,
'Annual_Income':Annual_Income,
'Website_Visits':Website_Visits,
'Previous_Purchases':Previous_Purchases,
'Membership_Type':Membership_Type,
'Preferred_Category':Preferred_Category,
'City_Tier':City_Tier,
'Discount_Used':Discount_Used
}

new_data=pd.DataFrame(data,index=[0])
if st.button(label='Predict Spendings'):
    spending=pipeline.predict(new_data)[0]
    st.success(f'Predicted Spendings: ₹{spending:.0f}',width=680)