#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import streamlit as st
import pandas as pd
from io import StringIO
import openai


st.title("YOUR CHEAT SHEETS GENERATOR")


openai.api_key = secret_key

@st.cache
def generate_table_text(question):
    model = "gpt-3.5-turbo"
    
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ]
    )
    
    answer = response.choices[0].message.content
    text = answer
    table_text = text[text.find('|'):]
    return table_text

def main():
    st.title("HERE AN OVERVIEW FOR WHAT YOU CAN LEARN")
    
    # Input field
    question = "List all the programming languages you know in a table with name, description and application"
    
    # Generate the table text using OpenAI API only if the question is not empty
    if question:
        table_text = generate_table_text(question)
        df = pd.read_csv(StringIO(table_text), sep='|')
        df = df.iloc[:, 1:-1]
        df = df.iloc[1:-1]
        st.write(df)
        if st.button('Download', key='1'):
            df.to_csv('df.csv')
            st.success('Downloaded dataframe')

if __name__ == '__main__':
    main()

    
def create_dataframe(question):
    table_text = generate_table_text(question)
    df = pd.read_csv(StringIO(table_text), sep='|')
    df = df.iloc[:, 1:-1]
    df = df.iloc[1:-1]
    return df

def process_input(input_value):
    # Perform your processing logic here
    # Replace this with your own implementation
    answer = input_value.upper()
    return answer

def main():
    st.title("Cheatsheet Generator")
    
    # Input fields
    input_language = st.text_input('Enter the programming language')
    input_app = st.text_input('Enter the application')
    
    # Generate the cheatsheet table using OpenAI API only if both inputs are not empty
    if input_language and input_app:
        question = f"Create a cheatsheet for {input_language} for {input_app} in a table"
        df = create_dataframe(question)
        st.write(df)
        
        # Additional logic
        input_answer = st.text_input('Do you want to see the equivalents in other programming languages')
        if input_answer == 'yes':
            n = int(st.text_input("Enter the value of n: "))
            answers = []
            for i in range(n):
                user_input = st.text_input(f"Enter input {i+1}: ")
                if user_input:
                    answer = process_input(user_input)
                    answers.append(answer)
                    st.write(f"Answer for input {i+1}: {answer}")
                else:
                    st.write(f"Please enter input {i+1}")
            
            if len(answers) == n:
                # Generate cheat sheet with updated answers
                answer_text = ', '.join(answers)
                updated_question = f"Create a cheat sheet for {input_language} and {answer_text} for {input_app} in a table"
                updated_df = create_dataframe(updated_question)
                
                # Display the cheat sheet table
                st.write(updated_df)
                
                # Download button for updated cheat sheet
                if st.button('Download', key='3'):
                    updated_df.to_csv('cheatsheet.csv', index=False)
                    st.success('Downloaded updated cheatsheet')
        
if __name__ == '__main__':
    main()
    
    
    
