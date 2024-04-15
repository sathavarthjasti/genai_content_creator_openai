import streamlit as st
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="AI Content Generator", layout="centered")
st.title("📝 AI Content Generator")

content_type = st.selectbox("Select content type:", ["Blog Post", "Tweet", "Ad Copy", "Product Description"])
topic = st.text_input("Enter a topic or product:")
tone = st.selectbox("Tone:", ["Professional", "Casual", "Humorous", "Persuasive"])
length = st.slider("Length (approx. words)", min_value=50, max_value=500, value=150)

if st.button("Generate"):
    with st.spinner("Generating content..."):
        prompt = f"Write a {tone.lower()} {content_type.lower()} about '{topic}' in approximately {length} words."
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=length * 2,
                temperature=0.7
            )
            output = response.choices[0].message.content.strip()
            st.subheader("✍️ Generated Content")
            st.write(output)
        except Exception as e:
            st.error(f"Error: {e}")
