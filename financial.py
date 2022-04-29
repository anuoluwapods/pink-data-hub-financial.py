import streamlit as st
import datetime
import pyodbc
import pandas as pd



st.header("Pink Data Hub Financial App")

pink_data = st.sidebar.selectbox("choose", ('Choose','Database','Database Connection'))
 
          
if pink_data == 'Database':
          with st.form("Submit", clear_on_submit=True):
               st.text_input("Company's ID")
               st.date_input("Today's Date",
                         datetime.date(2022, 3, 1 ))
               st.text_input("Company's Name")
               st.text_input("Amount")
               st.text_input("Payment Mode")
               
               st.form_submit_button("Submit")
            
@st.experimental_singleton
def init_connection():
    return pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)

  conn = init_connection()


@st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
    
    
     
if pink_data == 'Database Connection':
    st.header("Database Records")
    rows = run_query("SELECT * FROM dbo.company_details;")
    i = 0
    for row in rows:
        i += 1
        st.write(f"{i}. User : {row[0]} and Pass : {row[1]}:")
        
