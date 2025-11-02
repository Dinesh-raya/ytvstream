import re
from urllib.parse import urlparse, parse_qs

def normalize_url(url: str) -> str:
    url = url.strip()
    if url.startswith("http://"):
        url = "https://" + url[len("http://"):]
    return url

def validate_youtube_url(url: str) -> bool:
    if not url or not isinstance(url, str):
        return False
    url = url.strip()
    patterns = [
        r'(https?://)?(www\.)?youtube\.com/watch\?v=[\w-]{11}',
        r'(https?://)?youtu\.be/[\w-]{11}',
        r'(https?://)?(www\.)?youtube\.com/embed/[\w-]{11}',
        r'(https?://)?(www\.)?youtube\.com/shorts/[\w-]{11}',
    ]
    for p in patterns:
        if re.search(p, url):
            return True
    try:
        parsed = urlparse(url)
        qs = parse_qs(parsed.query)
        if 'v' in qs and len(qs['v'][0]) == 11:
            return True
    except Exception:
        pass
    return False

def extract_video_id(url: str) -> str:
    if not url or not isinstance(url, str):
        return None
    url = url.strip()
    patterns = [
        r'v=([\w-]{11})',
        r'youtu\.be/([\w-]{11})',
        r'embed/([\w-]{11})',
        r'shorts/([\w-]{11})'
    ]
    for p in patterns:
        m = re.search(p, url)
        if m:
            return m.group(1)
    try:
        parsed = urlparse(url)
        qs = parse_qs(parsed.query)
        vid = qs.get('v', [None])[0]
        if vid and len(vid) >= 11:
            return vid[:11]
    except Exception:
        pass
    return None

def generate_embed_url(video_id: str) -> str:
    if not video_id:
        return None
    return f"https://www.youtube-nocookie.com/embed/{video_id}?rel=0&modestbranding=1"
