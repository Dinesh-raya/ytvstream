\
    import streamlit as st

    def set_page_style():
        st.markdown(
            \"\"\"
            <style>
            /* Page background & text */
            .css-18e3th9 {padding-top:1rem;}
            .stApp { background: linear-gradient(180deg, #0f172a 0%, #071025 100%); }
            .stTextInput>div>div>input { background-color: #0b1220; color: #e6eef8; border-radius: 10px; border: 1px solid #233044; padding: 10px; }
            .stButton>button { background-color: #2563eb; color: white; border-radius: 8px; }
            /* Responsive iframe container (max-width) */
            iframe { box-shadow: 0 10px 30px rgba(2,6,23,0.6); }
            .footer { text-align: center; font-size: 0.9em; color: #9aa8bf; margin-top: 20px; }
            </style>
            \"\"\" ,
            unsafe_allow_html=True
        )

    def render_footer():
        st.markdown('<div class="footer">🔒 SafeView – Distraction-free YouTube player • Built with Streamlit</div>', unsafe_allow_html=True)
