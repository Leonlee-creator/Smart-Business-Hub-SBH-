import streamlit as st

def set_page_style():
    st.markdown("""
        <style>
            body {
                background-color: #f7f9fc;
            }
            .stApp {
                background: #f9f9f9;
                color: #333;
                font-family: 'Segoe UI', sans-serif;
            }

            /* Padding for app content */
            .css-18e3th9 {
                padding: 2rem;
            }

            /* Style for generated text */
            .generated-box {
                background-color: #ffffff;
                padding: 1rem 1.5rem;
                margin-top: 1rem;
                border-left: 5px solid #4CAF50;
                border-radius: 10px;
                box-shadow: 0 2px 6px rgba(0,0,0,0.1);
                color: #222;
                font-size: 1.05rem;
            }

            /* Optional button customization */
            .stButton > button {
                background-color: #0066ff;
                color: white;
                border: none;
                padding: 0.6rem 1.2rem;
                border-radius: 8px;
                font-weight: bold;
                transition: background-color 0.3s ease;
            }

            .stButton > button:hover {
                background-color: #004ec2;
            }
        </style>
    """, unsafe_allow_html=True)
