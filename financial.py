import streamlit as st
import pandas as pd
import datetime
from deta import Deta
import json

st.header("Pink Data Hub Financial App")


pink_data = st.sidebar.selectbox("choose", ('Choose', 'Database', 'Database Connection'))



if pink_data == 'Database':
    form = st.form("forms", clear_on_submit=True)
    id = form.text_input("Company's ID")
    date = form.date_input("Today's Date",
                      datetime.date(2022, 4, 1))
    name = form.text_input("Company's Name")
    amount = form.text_input("Amount")
    payment = form.text_input("Payment Mode")
    submit = form.form_submit_button("Submit")
deta = Deta(st.secrets["deta_key"])
db = deta.Base("Financial-records")
if submit:
     db.put({"company_id": id, "date": date, "company_name":name, "amount":amount, "payment_mode":payment})
  


if pink_data ==  'Database Connection':
    db_content = db.fetch().items
    st.write(db_content)
