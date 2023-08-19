import pandas as pd
import numpy as np
import streamlit as st

#Function to write a text to File
FILE_NAME = "./data/text.txt"

def write_text(text):
    with open(FILE_NAME,'a') as file:
        file.write(text+'\n')


# text = 'Hello World'
# write_text(text)

txt = st.text_area('Text to analyze')

if st.button('Add'):
    write_text(txt)

