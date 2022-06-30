if pink_data == 'Database Connection':
    df = pd.read_csv("company_details.csv")
    st.markdown("Data Record: ")
    st.dataframe(df)
    

