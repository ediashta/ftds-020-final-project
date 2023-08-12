import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

bank_df = pd.read_csv('./csv/BankChurners.csv')
bank_df.drop(columns=["CLIENTNUM", 
                      "Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1",
                      "Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2"], inplace=True)

sns.set(style="whitegrid")
palette=["teal", "darkblue"]
num_col = bank_df.select_dtypes(include=np.number).columns.tolist()
cat_col = bank_df.select_dtypes(include=object).columns.tolist()
cat_col.remove("Attrition_Flag")

st.set_page_config(
    page_title="Customer Churn Classification",
    layout="wide",
    initial_sidebar_state="expanded",
)

def distribution():
    # distribution plot
    
    st.header("Data Distribution")
    
    attr_plot('Attrition_Flag')
    
    col1, col2 = st.columns(2)
    
    numerik = col1.selectbox(label="Select Features",
                   options=num_col)
    
    hist_plot(numerik, col1)
    
    kategorik = col2.selectbox(label="Select Features",
                   options=cat_col)
    
    count_plot(kategorik, col2)
    
    st.markdown('''
                
                ''')

def attr_plot(column):
    fig = plt.figure(figsize=(15,5))
    sns.countplot(data=bank_df, y=column, palette=palette, alpha=0.7)
    st.pyplot(fig)

def hist_plot(column, loc):
    fig = plt.figure(figsize=(15,6))
    sns.histplot(data=bank_df, x=column, kde=True, bins=50, palette=palette, hue="Attrition_Flag")
    loc.pyplot(fig)
    
def count_plot(column,loc):
    fig = plt.figure(figsize=(15,6))
    sns.countplot(data=bank_df, y=column, palette=palette, hue="Attrition_Flag", order=bank_df[column].value_counts().index, alpha=0.7)
    loc.pyplot(fig)
    
if __name__ == "__main__":
    distribution()
