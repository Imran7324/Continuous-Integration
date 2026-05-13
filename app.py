import streamlit as st
#Streamlit UI
st.title("Power Calculator")
st.write("Enter a number to calculate its square, cube and fourth power")
#User Input
n=st.number_input("Enter Number", value=1, step=1)
#Calculating 
square=n**2
cube=n**3
f=n**4
#Printing results
st.write(f"Square of {n} is {square}")
st.write(f"Cube of {n} is {cube}")
st.write(f"Fourth power of {n} is {f}")
#To run this, use "streamlit run filename.py"


