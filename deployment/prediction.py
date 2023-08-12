import streamlit as st
import pandas as pd
import numpy as np
import pickle
import tensorflow as tf
import matplotlib.pyplot as plt
from PIL import Image
from urllib import request
from io import BytesIO


def predict():
    
    
    with open('./model/xgb_tuned.pkl', 'rb') as file_1:
        prediction_model = pickle.load(file_1)

    with open('./model/model_kmeans.pkl', 'rb') as file_2:
        cluster_model = pickle.load(file_2)
    
    #biodata
    st.subheader("Customer Biodata")
    col1, col2, col3 = st.columns(3)
    gender = col1.radio(label="Gender", options=["M", "F"])
    marital = col2.selectbox(label="Marital Status", options=["Single", "Married", "Divorced", "Unkown"])
    relationship = col3.number_input(label="No. of Relationshop", step=1, value=4)
    
    col1, col2, col3 = st.columns(3)
    education = col1.selectbox(label="Education Level", options=["Graduate", "Unedicated", "High School", "College", "Post=Graduate", "Doctorate"])
    income = col2.selectbox(label="Income Bracket", options=["Less than $40K", "$40K - $60K", "$60K - $80K", "$80K - $120K", "$120K+", "Unkown"])
    card = col3.radio(label="Card Type", options=["Blue", "Silver", "Gold", "Platinum"])
    
    #behaviour
    st.subheader("Customer Behaviour")
    
    col1, col2, col3 = st.columns(3)
    active_months = col1.slider(label="Months Inactive", max_value=6, value=2)
    last_contact = col2.slider(label="Last Contact", max_value=6, value=2)
    credit_limit = col3.number_input(label="Credit Limit", step=0.1, value=10834.0)
    
    col1, col2, col3 = st.columns(3)
    revolving_bal = col1.number_input(label="Revolving Balance", step=1, value=0)
    transaction_count = col2.number_input(label="Transaction Count", step=1, value=51)
    transaction_amount = col3.number_input(label="Transaction Amount", step=1, value=2249)
    
    col1, col2, col3 = st.columns(3)
    amount_chng = col1.slider(label="Amount Change",step=0.01,min_value=0.0, max_value=5.0, value=0.522)
    count_change = col2.slider(label="Count Change", step=0.01,min_value=0.0, max_value=5.0, value=0.594)
    util_ratio = col3.slider(label="Utilization Ratio", step=0.01,min_value=0.0, max_value=1.0, value=0.0)
    
    submit = st.button(label="Submit")
    
    if submit:
        data_inf = {
                'Total_Relationship_Count': [relationship],
                'Months_Inactive_12_mon': [active_months],
                'Contacts_Count_12_mon': [last_contact],
                'Credit_Limit': [credit_limit],
                'Total_Revolving_Bal': [revolving_bal],
                'Total_Amt_Chng_Q4_Q1': [amount_chng],
                'Total_Trans_Amt': [transaction_amount],
                'Total_Trans_Ct': [transaction_count],
                'Total_Ct_Chng_Q4_Q1': [count_change],
                'Avg_Utilization_Ratio': [util_ratio],
                'Gender': [gender],
                'Education_Level': [education],
                'Marital_Status': [marital],
                'Income_Category': [income],
                'Card_Category': [card],
        }
        
        data_inf= pd.DataFrame(data_inf)
        
        pred_inf = prediction_model.predict(data_inf)
        if pred_inf == 0:
            pred_inf = "Attrited Customer"
        else:
            pred_inf = "Existing Customer"
            
        if pred_inf == "Attrited Customer":
            cluster_inf = cluster_model.predict(data_inf)
        else:
            cluster_inf = None

        if cluster_inf == 0:
            cluster_inf = "Cluster 1 : High Spent Amount, High Usage Frequency"
        elif cluster_inf == 1:
            cluster_inf = "Cluster 2 : Low Spent Amount, Low Usage Frequency"
            
        st.write(pred_inf)
        st.write(cluster_inf)


if __name__ == "__main__":
    predict()
