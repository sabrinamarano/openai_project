#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import streamlit as st
 
st.title("WIP")
 
st.write("""HOW TO LEARN QUICKLY""")

import openai
import pandas as pd
from io import StringIO

openai.api_key = st.secrets["secret_key"]

model = "gpt-3.5-turbo"
question = "List all the programming languages you know in a table with name, description and application"

response = openai.ChatCompletion.create(
    model=model,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": question}
    ]
)

answer = response.choices[0].message.content
text = answer
table_text = text[text.find('|') :]

# Create a DataFrame from the table text
df = pd.read_csv(StringIO(table_text), sep='|')
df=df.iloc[:, 1:-1]
df=df.iloc[1:-1]
df




#init_path

#input_1=input()
#input_1

input_1=st.text_input("What you want to learn?")

if input_1:
    model = "gpt-3.5-turbo"
    question = f"Create a plan study for {input_1} in a table "

    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "system", "content": "You are a helpful assistant."},{"role": "user", "content": question}])

    answer = response.choices[0].message.content
    text = answer
    table_text = text[text.find('|') :]

# Create a DataFrame from the table text
    df = pd.read_csv(StringIO(table_text), sep='|')
    df=df.iloc[:, 1:-1]
    df=df.iloc[1:-1]
    df






