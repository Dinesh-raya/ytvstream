import re
import streamlit as st

st.set_page_config(
    page_title="SafeView for YouTube",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 SafeView for YouTube")
st.write("Watch YouTube videos without ads, comments, or distractions.")

def extract_youtube_id(url: str) -> str:
    patterns = [
        r"(?:https?://)?(?:www\.)?youtu\.be/([a-zA-Z0-9_-]{11})",
        r"(?:https?://)?(?:www\.)?youtube\.com/watch\?v=([a-zA-Z0-9_-]{11})",
        r"(?:https?://)?(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]{11})"
    ]
    for pattern in patterns:
        match = re.match(pattern, url)
        if match:
            return match.group(1)
    return None

youtube_url = st.text_input("Paste your YouTube video link here 👇")

if youtube_url:
    video_id = extract_youtube_id(youtube_url)

    if video_id:
        st.success("✅ Valid YouTube link detected!")
        safe_embed_url = f"https://www.youtube-nocookie.com/embed/{video_id}"

        st.markdown(
            f"""
            <div style="display:flex; justify-content:center; margin-top:20px;">
                <iframe width="700" height="400"
                        src="{safe_embed_url}"
                        title="YouTube video player"
                        frameborder="0"
                        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                        allowfullscreen>
                </iframe>
            </div>
            """ ,
            unsafe_allow_html=True
        )
    else:
        st.error("❌ Please enter a valid YouTube video URL.")
else:
    st.info("👆 Paste a YouTube video link above to view it safely.")
