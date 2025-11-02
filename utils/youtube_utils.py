\
    import re
    from urllib.parse import urlparse, parse_qs

    def normalize_url(url: str) -> str:
        \"\"\"Ensure URL uses https and strip whitespace.\"\"\"
        url = url.strip()
        if url.startswith("http://"):
            url = "https://" + url[len("http://"):]
        return url

    def validate_youtube_url(url: str) -> bool:
        \"\"\"Return True if URL looks like a YouTube video URL.\"\"\"
        if not url or not isinstance(url, str):
            return False
        url = url.strip()
        patterns = [
            r'(https?://)?(www\\.)?youtube\\.com/watch\\?v=[\\w-]{11}',
            r'(https?://)?youtu\\.be/[\\w-]{11}',
            r'(https?://)?(www\\.)?youtube\\.com/embed/[\\w-]{11}',
            r'(https?://)?(www\\.)?youtube\\.com/shorts/[\\w-]{11}',
        ]
        for p in patterns:
            if re.search(p, url):
                return True
        # As a fallback, try to parse query param 'v'
        try:
            parsed = urlparse(url)
            qs = parse_qs(parsed.query)
            if 'v' in qs and len(qs['v'][0]) == 11:
                return True
        except Exception:
            pass
        return False

    def extract_video_id(url: str) -> str:
        \"\"\"Extract the 11-character YouTube video ID from many URL forms.\"\"\"
        if not url or not isinstance(url, str):
            return None
        url = url.strip()

        # Common patterns
        patterns = [
            r'v=([\\w-]{11})',              # watch?v=ID
            r'youtu\\.be/([\\w-]{11})',     # youtu.be/ID
            r'embed/([\\w-]{11})',          # embed/ID
            r'shorts/([\\w-]{11})'          # shorts/ID
        ]
        for p in patterns:
            m = re.search(p, url)
            if m:
                return m.group(1)

        # Try parsing query params
        try:
            parsed = urlparse(url)
            qs = parse_qs(parsed.query)
            vid = qs.get('v', [None])[0]
            if vid and len(vid) >= 11:
                # sometimes v has extra params; take first 11 chars if matches pattern
                vid = vid[:11]
                return vid
        except Exception:
            pass

        return None

    def generate_embed_url(video_id: str) -> str:
        \"\"\"Return privacy-enhanced embed URL with recommended params.\"\"\"
        if not video_id:
            return None
        # rel=0 (do not show related videos from other channels), modestbranding=1 reduces branding
        return f"https://www.youtube-nocookie.com/embed/{video_id}?rel=0&modestbranding=1"
