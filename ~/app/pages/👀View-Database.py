import streamlit as st
import pandas as pd
import datetime
import base64
from PIL import Image

col1, col2 = st.columns(2)



image = Image.open('image.png')


col1.header("Pink Data Hub Financial App")
col2.image(image)

data = {"company_id": id, "date": date, "company_name":name, "amount":amount, "payment_mode":payment}
df = df.append(data, ignore_index=True)
df.to_csv("company_details.csv", index=False, encoding="utf-8")

df = pd.read_csv("company_details.csv")
st.markdown("Data Record: ")
st.dataframe(df)
    

