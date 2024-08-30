import streamlit as st





st.title("Structured Query Language")

st.header("Practice questions")

st.text("NB: Use the jumiaa schemas")

st.write("##")
st.subheader("Questions")
st.write("---")

#Question 1
st.write('''Q1. Show the first 7 employees from 
         employees table in Jumiaa_hr without using “USE jumiaa_hr;” syntax.''')
st.markdown('<p style="color:red;">Try the question before clicking to see the answer</p>', unsafe_allow_html=True)

with st.expander("Expand to see the commands"):
    st.image("q1.png")

#Question 2
st.write("##")
st.write('''Q2. What is the total points of individuals whose second name
          starts with “m” and their city name contains “m” from customers table?''')
st.markdown('<p style="color:red;">Try the question before clicking to see the answer</p>', unsafe_allow_html=True)
with st.expander("Expand to see the commands"):
    st.image("q2.png")

#Questions 3
st.write("##")
st.write('''Q3. From invoices table write a sql command that shows 
         how much was paid between '2019-01-05' and '2019-02-01' ''')
st.markdown('<p style="color:red;">Try the question before clicking to see the answer</p>', unsafe_allow_html=True)
with st.expander("Expand to see the commands"):
    st.image("q3.png")

#Question 4
st.write("##")
st.write('''Q4. Write a command showing which customers came 
         from the same states as where offices were located?''')
st.markdown('<p style="color:blue;">Hint: Inner Join</p>', unsafe_allow_html=True)
st.markdown('<p style="color:red;">Try the question before clicking to see the answer</p>', unsafe_allow_html=True)
with st.expander("Expand to see the commands"):
    st.image("q4.png")
