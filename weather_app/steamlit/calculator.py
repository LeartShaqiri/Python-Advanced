import streamlit as st

def calculate(num1,num2, operation):
    if operation =='addition':
        result = num1 + num2
    elif operation == 'substraction':  
        result = num1 - num2
    elif operation == 'multiplaction':
        result = num1 * num2

    elif operation =='division':
     try:
            result = num1/num2
     except ZeroDivisionError:
         result = "Cammot devide by zero"
         return result
     

def main():
    st.title("Simple Caluclator")     

    num1 = st.number_imput("Enter the first number, " step=1)

    num2 = st.number_imput("Enter the secind number" step=2)

    

