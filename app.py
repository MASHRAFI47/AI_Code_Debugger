import streamlit as st
from api_calling import solution_generator, issue_generator
from PIL import Image

st.header("Code Debugger")
st.markdown("Upload the image of your code error")
st.divider()

with st.sidebar:
    st.header("Controls")
    
    st.subheader("Uploaded images")
    images = st.file_uploader(
        "Upload the photos of your code",
        type=['jpg', 'jpeg', 'png'],
        accept_multiple_files=True
    )
    
    
    options = st.selectbox(
        "How you want to solve the problem?",
        ("Hints", "Solution with Code"),
        index=None
    )
    
    button = st.button("Click the button to initiate", type="primary")
    
    
if button:
    if not images:
        st.error("Please upload at least one image")
    if not options:
        st.error("Please select the options")
    
    
    if images and options:
        
        pil_images = [Image.open(img) for img in images]
        
        #The issue
        with st.container(border=True):
            st.subheader("The issue")
            
            with st.spinner("AI is initiating your issue"):
                issues = issue_generator(pil_images, options)
                st.markdown(issues)
                

        #The solution
        with st.container(border=True):
            st.subheader("The Solution")
            
            with st.spinner("AI is generating the solution"):
                solution = solution_generator(pil_images, options)
                st.markdown(solution)