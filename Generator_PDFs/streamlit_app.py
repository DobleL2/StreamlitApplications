import streamlit as st
from fpdf import FPDF
import base64

def create_download_link(val, filename):
    b64 = base64.b64encode(val)
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Download file</a>'

def main():
    st.title("Welcome to My Streamlit App 3.0")

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
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(40, 10, st.session_state.report_text)
        
        html = create_download_link(pdf.output(dest="S").encode("latin-1"), "test")
        st.markdown(html, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
