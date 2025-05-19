
# Strategic Gap Radar – Final Version (Clean Start)
# Compatible with OpenAI Python SDK >= 1.0.0

import streamlit as st
import openai

# Load OpenAI API key securely from Streamlit secrets
client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Configure Streamlit page
st.set_page_config(page_title="Strategic Gap Radar", layout="centered")
st.title("🧠 Strategic Gap Radar")
st.markdown("""
Enter a description of your project, organization, or strategy below.
The AI agent will analyze and return a list of inferred strategic gaps,
blind spots, or hidden assumptions.
""")

# User input field
user_input = st.text_area("📝 Input your system or strategic description")

# Button to trigger radar analysis
if st.button("🔍 Analyze for Gaps"):
    if not user_input.strip():
        st.warning("Please provide a description to analyze.")
    else:
        with st.spinner("Analyzing for strategic weaknesses..."):
            system_msg = "You are a strategic analysis agent. Identify risks, blind spots, and logic flaws."
            user_prompt = f"""
Analyze the following project or system description. Identify strategic gaps, including unstated dependencies,
misaligned incentives, structural weaknesses, or hidden risks. Respond in clean bullet points.

Description:
{user_input}

Gaps:
"""
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": system_msg},
                        {"role": "user", "content": user_prompt}
                    ],
                    temperature=0.5,
                    max_tokens=600
                )
                result = response.choices[0].message.content
                st.subheader("📡 Inferred Strategic Gaps")
                st.markdown(result)
            except Exception as error:
                st.error(f"API Error: {error}")
