import streamlit as st

lst = [1,2]

if st.button("Show List"):
    
    st.write(lst)

    
    st.json(lst)


    # Normal Number
    st.write(5)

    # Number using JSON
    st.json(5)
