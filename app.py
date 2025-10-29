import streamlit as st
import json

lst = [1,2]

if st.button("Show List"):

    # साधारण list दिखाने के लिए
    st.info("In single line")
    st.write(str(lst))

    # JSON format में दिखाने के लिए
    st.warning("in json format")
    st.json(lst)

    # New
    st.warning("in code format")
    st.code(json.dumps(lst), language="json")
    st.code(lst)

    # Our Format
    st.success("our desired format")
    pretty_json = json.dumps(lst, indent=2)
    st.code(pretty_json, language="json")


    st.error("normal numbers")
    # Normal Number
    st.write(5)

    # Number using JSON
    st.json({5:5})
