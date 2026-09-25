
import streamlit as st
from groq import Groq

st.set_page_config(
    page_title="LinkedIn Post Generator",
    page_icon="💼",
    layout="centered"
)

st.title("💼 LinkedIn Post Generator")

st.write(
    "Create professional and engaging LinkedIn posts using AI."
)

topic = st.text_area(
    "What is your LinkedIn post topic?",
    placeholder="Example: How AI is changing the workplace"
)

audience = st.selectbox(
    "Target Audience",
    [
        "General Professional Audience",
        "Young Professionals",
        "Entrepreneurs",
        "Students",
        "Developers",
        "Marketing Professionals",
        "Business Leaders"
    ]
)

tone = st.selectbox(
    "Tone",
    [
        "Professional",
        "Conversational",
        "Educational",
        "Inspirational",
        "Thought-provoking"
    ]
)

length = st.selectbox(
    "Post Length",
    [
        "Short",
        "Medium",
        "Long"
    ]
)

col1, col2 = st.columns(2)

with col1:
    emojis = st.checkbox("Include emojis")

with col2:
    hashtags = st.checkbox("Include hashtags")

if st.button("✨ Generate LinkedIn Post"):

    if not topic:
        st.error("Please enter a topic.")

    else:

        try:

            client = Groq(
                api_key=st.secrets["GROQ_API_KEY"]
            )

            emoji_instruction = (
                "Use a small number of relevant emojis."
                if emojis
                else "Do not use emojis."
            )

            hashtag_instruction = (
                "Include 3-5 relevant hashtags."
                if hashtags
                else "Do not include hashtags."
            )

            prompt = f"""
Create a high-quality LinkedIn post.

Topic:
{topic}

Target audience:
{audience}

Tone:
{tone}

Length:
{length}

Requirements:

- Start with a strong hook.
- Provide useful insights.
- Use short paragraphs.
- Make it easy to read.
- Sound natural and human.
- Avoid clickbait.
- Avoid exaggerated claims.
- Encourage meaningful engagement.
- {emoji_instruction}
- {hashtag_instruction}

Return only the final LinkedIn post.
"""

            response = client.chat.completions.create(
                model="openai/gpt-oss-120b",
                messages=[
                    {
                        "role": "system",
                        "content": """
You are an expert LinkedIn content writer.

Create professional, useful and engaging
LinkedIn posts that sound natural and human.
"""
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )
             post = response.choices[0].message.content

            st.subheader("Generated LinkedIn Post")

            st.text_area(
                "Your LinkedIn post:",
                value=post,
                height=400
            )

            st.download_button(
                label="📋 Copy/Download Post",
                data=post,
                file_name="linkedin_post.txt",
                mime="text/plain"
            )

        except Exception as e:
            st.error(f"Something went wrong: {e}")
