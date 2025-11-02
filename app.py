import streamlit as st
from utils.youtube_utils import (
    validate_youtube_url,
    extract_video_id,
    generate_embed_url,
    normalize_url
)
from utils.ui_utils import set_page_style, render_footer

st.set_page_config(page_title="SafeView – Clean YouTube Player", page_icon="🎬", layout="centered")

set_page_style()

st.title("🎬 SafeView – YouTube Distraction‑Free Player")
st.caption("Paste a YouTube link below and watch without ads, comments, or clutter.")

url = st.text_input("Enter YouTube URL:", placeholder="e.g., https://www.youtube.com/watch?v=dQw4w9WgXcQ")

if url:
    url = url.strip()
    url = normalize_url(url)
    if validate_youtube_url(url):
        video_id = extract_video_id(url)
        if video_id:
            embed_url = generate_embed_url(video_id)
            st.markdown(
                f"""
                <div style="display:flex; justify-content:center;">
                  <iframe width="100%" style="max-width:960px; height:480px; border-radius:12px;"
                      src="{embed_url}"
                      frameborder="0"
                      allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
                      allowfullscreen loading="lazy">
                  </iframe>
                </div>
                """ ,
                unsafe_allow_html=True
            )
            st.success("✅ Video loaded. If the video is age‑restricted or private, YouTube may request sign‑in.")
        else:
            st.error("❌ Could not extract a Video ID from that URL. Try a different YouTube link.")
    else:
        st.error("⚠️ That doesn't look like a valid YouTube URL. Please paste a standard YouTube video link.")
else:
    st.info("👆 Paste a valid YouTube link above to begin.")

render_footer()
