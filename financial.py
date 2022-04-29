import streamlit as st
import pandas as pd
import datetime
from deta import Deta
import base64
from st_aggrid import AgGrid


# Adding Animation at the top of webapp
file_ = open("image_1.png", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="dashboard gif">',
     unsafe_allow_html=True
)


# Styling side bar with image
st.sidebar.image("image.png", use_column_width=True)


st.header("Pink Data Hub Financial App")


pink_data = st.sidebar.selectbox("choose", ('Choose', 'Database', 'Database Connection', 'Download File'))

df = pd.read_csv("company_details.csv")

if pink_data == 'Database':
    form = st.form("forms", clear_on_submit=True)
    id = form.text_input("Company's ID")
    date = form.date_input("Today's Date",
                      datetime.date(2022, 4, 1))
    name = form.text_input("Company's Name")
    amount = form.text_input("Amount")
    payment = form.text_input("Payment Mode")
    submit = form.form_submit_button("Submit")
    if submit:
            st.success("Submitted Successfully")
            data = {"company_id": id, "date": date, "company_name":name, "amount":amount, "payment_mode":payment}
            df = df.append(data, ignore_index=True)
            df.to_csv("company_details.csv", index=False, encoding="utf-8")



if pink_data == 'Database Connection':
    df = pd.read_csv(r"C:\Users\user\Documents\Data Sets\CSV\company_details.csv")
    st.markdown("Data Record: ")
    AgGrid(df, editable=True)
    
 if pink_data == 'Download File':
    df = pd.DataFrame(df)
            file_name = "financial_records.csv"
            file_path = f"./{file_name}"

            df.to_csv(file_path)

            df = open(file_path, 'rb')
            st.download_button(label='Click to download',
                               data=df,
                               file_name=file_name,
                               key='download_df')
            df.close()
