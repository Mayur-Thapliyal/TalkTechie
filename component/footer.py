import streamlit as st


def get_footer()->(str):
    footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
max-height: 50px;
position: fixed;
left: 0;
bottom: 0;
width: 100%;
z-index: 1;
background-color: white;
color: black;
text-align: center;
span{
    font-weight: 600;
    color:black;
}
}
</style>
<div class="footer">
Developed with ❤ by <a href="https://www.linkedin.com/in/mayur-thapliyal-8462861b0/" target="_blank"><span>Mayur Thapliyal</span></a> <p>Powered By <span>LangChain + Streamlit</span></p>
</div>
"""
    st.markdown(footer,unsafe_allow_html=True)
