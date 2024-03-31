import streamlit as st
from fpdf import FPDF
import base64
import plotly.express as px
import pandas as pd

def create_download_link(val, filename):
    b64 = base64.b64encode(val)
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Download file</a>'

class PDFWithBackground(FPDF):
    def __init__(self):
        super().__init__()
        self.background = None

    def set_background(self, image_path):
        self.background = image_path

    def header(self):
        pass  # Override if you want to add a header

    def footer(self):
        if self.background:
            self.image(self.background, 0, 0, self.w, self.h)

def main():
    st.set_page_config(page_title='Full App')
    
    st.title("Mi primera aplicación analítica")

    # Initialize session state
    if 'report_text' not in st.session_state:
        st.session_state.report_text = ""
    
    if 'export' not in st.session_state:
        st.session_state.export = False

    with st.form("my_form"):
        name = st.text_input("Enter your name:")
        favorite_color = st.selectbox("Choose your favorite color", ["Red", "Green", "Blue"])
        submitted = st.form_submit_button("Submit")

    if submitted:
        st.session_state.report_text = f"Hello, {name}! Your favorite color is {favorite_color}."
        st.session_state.export = True
            
    if st.session_state.export:
        pdf = PDFWithBackground()
        pdf.add_page()
        pdf.set_background('background.png')
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(80, 10, st.session_state.report_text)

        html = create_download_link(pdf.output(dest="S").encode("latin-1"), "test")
        st.markdown(html, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
