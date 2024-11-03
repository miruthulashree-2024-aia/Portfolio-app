####create your own (challenge)

import streamlit as st

#function to feedback page

def feedback(session):
    st.write("Why is this {session} your favourite?")
    reason=st.text_input("because...")
    pass 
    st.write("Why is this {session} not your favourite?")
    reason=st.text_input("because...",key="reason_2")
    st.write("Finally click the submit button to record your response")
    if st.button("submit"):
        st.session_state.feedback={"session":session,"reason":reason}  
        st.rerun()  
        
       
             
        
#Main page
st.header("Interactive Feedback Page")   
st.write("welcome to our Interactive Feedback Page!!!.This is a fun and educational way where we were able to find our strength and weekness which helps us to improve our communication skills .let's collaborate and see what kinds of feedbacks we are getting!")  
if "feedback"  not in st. session_state:
    st.write("feedback for the session:")
    st.write("Click the option A and choose the question and enter the reason for choosing it")
    if st.button("option A"):
        feedback("option A")

                
## PORTFOLIO ("Using streamlit") 
import streamlit as st
# Custom CSS to change the background color
st.markdown(
    """
    <style>
    .stApp {
        background-color:Powderedblue; /* cadetblue background color */
    }
    </style>
    
    """,
    unsafe_allow_html=True
)
st.header("MY PORTFOLIO")
st.write("S.Miruthula Shree")  
st.subheader("About Me:")
st.write(" I am Miruthula Shree S .I completed my schooling in SVGV Matric Hr Sec School.I am currently pursuing my Undergraduate Degree with four years course of Artificial Inteligence and Data Science.I would like to start my carrer as a developer.I consider myself as a person who is very optimistic and a person who is very dedicated.I am very passionate about learning new things.")
st.write("Skills:")
st.write(" Basic tags of HTML")
st.write("Profile:")
st.write("www.linkedin.com/in/miruthula-shree-s-5151a0302")
st.subheader('"SKILLS ARE DEVELOPED FROM MISTAKES!!!"')



