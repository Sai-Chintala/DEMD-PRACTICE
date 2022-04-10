from flask import Flask, request
import streamlit as st

def hello():

    try:
        st.title("Learning Streamlit")
        stud_name = st.text_input("StudentName")
        numb = st.text_input("RollNo")
        
        result =  f"Student Name is {stud_name} and Roll Number is {numb}", 200

        if st.button("Print output"):
            st.success(result)

    except Exception as e:
        return f"Error occured with message : {e}", 401

if __name__ == "__main__":
    hello()