import streamlit as st
import os

st.set_page_config(
    page_title='Covid 19 Analysis',
    layout='wide',
    initial_sidebar_state='expanded'
)

st.title(':red[Covid 19] Analysis :copyright:')
st.subheader('Author : Manoj Kumar')

click= st.button('About Me')

if click == True:
    
    st.header('Manoj Kumar')
    st.subheader('Founder & CEO of CodersCave')
    st.subheader('Data Science Enthusiast')
    
    st.write('Follow and Connect with on these platforms !')
    
    
    st.write('[Linkedin](https://www.linkedin.com/in/manoj-kumar-7478ba247/)')
    st.write('[Instagram](https://instagram.com/mano._29)')
    st.write('[Github](https://github.com/ManojKumar2920)')
    
    st.snow()