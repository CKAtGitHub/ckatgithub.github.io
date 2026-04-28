import urllib.request
import json

url = "https://www.infoq.cn/public/v1/article/getCategory"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
try:
    with urllib.request.urlopen(req) as response:
        res = json.loads(response.read().decode('utf-8'))
        for t in res.get('data', []):
            if 'ai' in t.get('alias', '').lower() or 'ai' in t.get('name', '').lower() or '人工' in t.get('name', ''):
                print(t)
except Exception as e:
    print(f"Error fetching: {e}")
