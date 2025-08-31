import requests
import re
import sys
from urllib.parse import urlparse, parse_qs

def get_tags_danbooru(post_id: str):
    url = f"https://danbooru.donmai.us/posts/{post_id}.json"
    data = requests.get(url).json()
    return data.get("tag_string", "").split()

def get_tags_rule34(post_id: str):
    url = f"https://api.rule34.xxx/index.php?page=dapi&s=post&q=index&id={post_id}&json=1"
    data = requests.get(url).json()
    if not data:
        return []
    return data[0].get("tags", "").split()

def extract_post_id(url: str):
    # works for .../posts/1234567
    m = re.search(r"/posts/(\d+)", url)
    if m:
        return m.group(1)
    # works for ...id=1234567
    parsed = urlparse(url)
    qs = parse_qs(parsed.query)
    if "id" in qs:
        return qs["id"][0]
    return None

def get_tags(url: str):
    netloc = urlparse(url).netloc
    post_id = extract_post_id(url)
    if not post_id:
        raise ValueError("No post id found")

    if "danbooru.donmai.us" in netloc:
        return get_tags_danbooru(post_id)
    elif "rule34.xxx" in netloc:
        return get_tags_rule34(post_id)
    else:
        raise ValueError(f"Unsupported site: {netloc}")

if __name__ == "__main__":
    url = sys.argv[1]
    tags = get_tags(url)
    print(", ".join(tags))
