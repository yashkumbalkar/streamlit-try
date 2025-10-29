import streamlit as st

lst = [1,2]

if st.button("Show List"):
    # साधारण list दिखाने के लिए
    st.write(data)

    # JSON format में दिखाने के लिए
    st.json(data)


    # Normal Number
    st.write(5)

    # Number using JSON
    st.json(5)
