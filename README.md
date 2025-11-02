# SafeView for YouTube (Optimized)

Minimal, optimized Streamlit app that provides a distraction-free YouTube viewing experience
using YouTube's privacy-enhanced embed domain (`youtube-nocookie.com`).

## Features
- Accepts any standard YouTube link format (watch, youtu.be, embed, shorts)
- Validates and extracts the video ID robustly
- Uses privacy-enhanced embed with `rel=0` and `modestbranding=1`
- Modern dark UI, lazy loading iframe, and responsive layout
- Modular code (utils for easy extension)

## Run locally
1. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate    # Windows (PowerShell)
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the app:
   ```bash
   streamlit run app.py
   ```
4. Open http://localhost:8501 in your browser and paste a YouTube link.

## Project structure
```
safeshare_youtube_optimized/
├── app.py
├── utils/
│   ├── youtube_utils.py
│   └── ui_utils.py
├── static/
└── requirements.txt
```

## Notes
- Some videos (age-restricted/private) will still require sign-in via YouTube and cannot be embedded.
- This project intentionally does not download or re-host YouTube content to stay within YouTube's terms.
