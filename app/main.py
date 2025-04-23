import streamlit as st
from generator import generate_business_idea
from analyzer import analyze_market
from style import set_page_style
from fastapi import APIRouter, Request
from pydantic import BaseModel
from app.llama_chat import ask_mistral
from fastapi import FastAPI
from routes import chat  # assuming routes/chat.py

app = FastAPI()
app.include_router(chat.router)


router = APIRouter()

class Prompt(BaseModel):
    prompt: str

@router.post("/chat")
async def chat(prompt_data: Prompt):
    response = ask_mistral(prompt_data.prompt)
    return {"response": response}


# Set page config and style
st.set_page_config(page_title="Smart Business Hub", page_icon="📊", layout="wide")
set_page_style()

# Logo and Title
st.markdown('<div class="center">', unsafe_allow_html=True)
st.image("smart business hub.png", width=175)
st.title("Smart Business Hub (SBH)")
st.markdown("Helping you launch, analyze, and grow your next big idea!")
st.markdown("</div>", unsafe_allow_html=True)

# Sidebar Navigation
menu = st.sidebar.radio("Navigate", ["Generate Idea", "Market Analysis", "Business Plan"])

# Page: Generate Idea
if menu == "Generate Idea":
    st.subheader("🎯 Generate a Business Idea")
    category = st.selectbox("Select Category", ["Tech", "Health", "Education", "Finance", "E-commerce", "Custom"])
    custom_input = st.text_input("Custom Keywords (optional)")
    
    if st.button("Generate Idea"):
        idea = generate_business_idea(category, custom_input)
        st.markdown(f'<div class="generated-box">{idea}</div>', unsafe_allow_html=True)

        # Clipboard copy button
        st.markdown(f"""
            <button onclick="navigator.clipboard.writeText('{idea}')" style="
                margin-top: 10px;
                padding: 8px 14px;
                background-color: #0A84FF;
                color: white;
                border: none;
                border-radius: 8px;
                font-weight: bold;
                cursor: pointer;">
                📋 Copy Idea
            </button>
            <script>
                const buttons = window.parent.document.querySelectorAll("button");
                for (const btn of buttons) {{
                    if (btn.innerText === "📋 Copy Idea") {{
                        btn.addEventListener("click", () => alert('Idea copied to clipboard!'));
                    }}
                }}
            </script>
        """, unsafe_allow_html=True)

# Page: Market Analysis
elif menu == "Market Analysis":
    st.subheader("📈 Market Potential Analyzer")
    business_name = st.text_input("Enter Business Idea")
    target_location = st.text_input("Target Location (City, Country)")
    
    if st.button("Analyze Market"):
        analysis = analyze_market(business_name, target_location)
        st.markdown(f"""
            <div style="
                background-color: #e0f3ff;
                padding: 15px;
                border-left: 5px solid #0A84FF;
                border-radius: 10px;
                color: #000;
                font-size: 16px;
            ">
                {analysis}
            </div>
        """, unsafe_allow_html=True)


# Page: Business Plan
elif menu == "Business Plan":
    st.subheader("📝 Business Plan Generator (Coming Soon)")
    st.markdown(
        "<div class='coming-soon-box'>🚧 We're working on this powerful feature!</div>",
        unsafe_allow_html=True
    )
