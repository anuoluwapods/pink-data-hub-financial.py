import streamlit as st
import datetime
import pyodbc
import pandas as pd



st.header("Pink Data Hub Financial App")

@st.experimental_singleton
def init_connection():
    return pyodbc.connect(
        driver="SQL Server",
        server="ANUOLUWAPODS\SQLEXPRESS",
        DATABASE="pink_data_hub",
        UID="test",
        PWD="test,
        
    )

conn = init_connection()

pink_data = st.sidebar.selectbox("Database", "Database Connection")
 
          
if pink_data == "Database":
          with st.form("Submit", clear_on_submit=True):
               st.text_input("Company's ID")
               st.text_input("Company's Name")
               st.text_input("Amount")
               st.text_input("Payment Mode")
               st.date_input("Today's Date",
                         datetime.date(2022, 3, 1 ))
               st.form_submit_button("Submit")

@st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()
    
if pink_data == "Database Connection":
    st.header("Database Records")
    rows = run_query("SELECT * from company_details;")
    i = 0
    for row in rows:
        i += 1
        st.write(f"{i}. User : {row[0]} and Pass : {row[1]}:")
