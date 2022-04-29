import streamlit as st
from datetime import datetime
from deta import Deta
import json


st.header("Pink Data Hub Financial App")


pink_data = st.sidebar.selectbox("choose", ('Choose', 'Database', 'Database Connection'))


if pink_data == 'Database':
    with st.form("forms", clear_on_submit=True):
         id_name = st.text_input("Company's ID")
         date = st.date_input("Today's Date",
                      datetime.date(2022, 4, 1))
         name = st.text_input("Company's Name")
         amount = st.text_input("Amount")
         payment = st.text_input("Payment Mode")
         submit = st.form_submit_button("Submit")
         now = datetime.now()
         date = now.date.strfttime("%Y/%m/%d")       
deta = Deta(st.secrets["deta_key"])

db = deta.Base("Financial-records")
if submit:
     db.put({"company_id": id_name, "date": date, "company_name":name, "amount":amount, "payment_mode":payment})


"---"


if pink_data ==  'Database Connection':
    db_content = db.fetch().items
    st.write(db_content)
