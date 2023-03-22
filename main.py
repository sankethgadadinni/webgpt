import os
import json
import openai
import streamlit as st
from utils import webgpt_result, webgpt_results1


def main():
    
    st.title("WebGPT")
    
    query_text = st.text_input("enter the query")
    
    if st.button('predict', use_container_width=True):
    
        results = webgpt_results1(query = query_text, number_of_results = 5)
    
        st.write(results)
    

if __name__ == '__main__':
    
    main()
