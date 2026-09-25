
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
