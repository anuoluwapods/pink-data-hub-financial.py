import streamlit as st
import pandas as pd
import datetime
import base64
from PIL import Image
import SessionState

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)


image = Image.open('image.png')

 

col1.header("Pink Data Hub Financial App")
col1.write("A Form Web App With Downloadable CSV File")
col2.image(image)




try:
   with st.form("forms", clear_on_submit=True):
        id = col3.text_input("Company's ID")
        date = col4.date_input("Today's Date",
                      datetime.date(2022, 4, 1))
        name = col3.text_input("Company's Name")
        amount = col4.text_input("Amount")
        payment = col3.text_input("Payment Mode")
        submit = st.form_submit_button("Submit")
        if submit:
            st.success("Submitted Successfully")
            data = {"company_id": id, "date": date, "company_name":name, "amount":amount, "payment_mode":payment}
            df = df.append(data, ignore_index=True)
            df.to_csv("company_details.csv", index=False, encoding="utf-8"
            df = SessionState.get(df=data)
            file_name = "financial_records.csv"
            file_path = f"./{file_name}"

            df.to_csv(file_path)

            df = open(file_path, 'rb')
            st.download_button(label='Click to download',
                               data=df,
                               file_name=file_name,
                               key='download_df')
            df.close()
            )
            
