import urllib.request
import xml.etree.ElementTree as ET
import re
import json
import ssl
from bs4 import BeautifulSoup
import time

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def fetch_rss():
    req = urllib.request.Request('https://www.infoq.cn/feed', headers={'User-Agent': 'Mozilla/5.0'})
    res = urllib.request.urlopen(req, context=ctx)
    content = res.read().decode('utf-8')
    root = ET.fromstring(content)
    items = []
    for item in root.findall('.//item'):
        title = item.find('title').text
        link = item.find('link').text
        # filter only AI related titles or if InfoQ feed has categories
        if 'AI' in title or '智能' in title or '模型' in title or 'Agent' in title or '大语言' in title:
            items.append({'title': title, 'link': link})
    return items

def get_summary(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req, context=ctx, timeout=10)
        html = res.read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        
        # Try to find meta description
        meta = soup.find('meta', attrs={'name': 'description'})
        if meta and meta.get('content'):
            return meta.get('content')
            
        # Or find the first paragraph
        p = soup.find('p')
        if p:
            return p.text.strip()
    except Exception as e:
        print(f"Error fetching {url}: {e}")
    return ""

def main():
    items = fetch_rss()
    # If not enough AI, just get top 20 from all
    if len(items) < 20:
        req = urllib.request.Request('https://www.infoq.cn/feed', headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req, context=ctx)
        root = ET.fromstring(res.read().decode('utf-8'))
        items = []
        for item in root.findall('.//item'):
            items.append({
                'title': item.find('title').text,
                'link': item.find('link').text
            })
            
    items = items[:20]
    
    for item in items:
        print(f"Fetching {item['title']}...")
        item['summary'] = get_summary(item['link'])
        time.sleep(1)
        
    with open('infoq_ai.json', 'w', encoding='utf-8') as f:
        json.dump(items, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    main()
