import urllib.request
import json
import datetime
import os
import re
import time

def fetch_infoq_ai_articles(size=20):
    url = "https://www.infoq.cn/public/v1/article/getList"
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://www.infoq.cn/topic/ai"
    }
    # ID 31 for AI topics on InfoQ
    data = json.dumps({"type": 1, "size": size, "id": 31}).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers=headers, method='POST')
    try:
        with urllib.request.urlopen(req) as response:
            res = json.loads(response.read().decode('utf-8'))
            if res.get('code') == 0:
                return res['data']
    except Exception as e:
        print(f"Error fetching article list: {e}")
    return []

def fetch_article_detail(uuid):
    url = "https://www.infoq.cn/public/v1/article/getDetail"
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://www.infoq.cn/"
    }
    data = json.dumps({"uuid": uuid}).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers=headers, method='POST')
    try:
        with urllib.request.urlopen(req) as response:
            res = json.loads(response.read().decode('utf-8'))
            if res.get('code') == 0:
                return res['data']
    except Exception as e:
        print(f"Error fetching detail for {uuid}: {e}")
    return None

def parse_inline(c):
    if c.get('type') == 'text':
        text = c.get('text', '')
        if text == '\xa0':
            return ''
        marks = c.get('marks', [])
        is_bold = any(m.get('type') == 'strong' for m in marks)
        is_italic = any(m.get('type') == 'italic' for m in marks)
        is_code = any(m.get('type') == 'code' for m in marks)
        
        if is_bold:
            text = f"**{text}**"
        if is_italic:
            text = f"*{text}*"
        if is_code:
            text = f"`{text}`"
            
        link_mark = next((m for m in marks if m.get('type') == 'link'), None)
        if link_mark:
            href = link_mark.get('attrs', {}).get('href', '')
            text = f"[{text}]({href})"
            
        return text
    elif c.get('type') == 'hardbreak':
        return "\n"
    elif c.get('type') == 'link':
        text = ""
        for child in c.get('content', []):
            text += parse_inline(child)
        href = c.get('attrs', {}).get('href', '')
        return f"[{text}]({href})"
    return ""

def parse_block(block):
    t = block.get('type')
    content = block.get('content', [])
    
    res = ""
    if t == 'paragraph':
        for c in content:
            res += parse_inline(c)
        if res.strip():
            res += "\n\n"
    elif t == 'heading':
        level = block.get('attrs', {}).get('level', 2)
        res += "#" * level + " "
        for c in content:
            res += parse_inline(c)
        res += "\n\n"
    elif t == 'bulletedlist':
        for item in content:
            res += "- "
            for p in item.get('content', []):
                for c in p.get('content', []):
                    res += parse_inline(c)
            res += "\n"
        res += "\n"
    elif t == 'orderedlist':
        for idx, item in enumerate(content):
            res += f"{idx+1}. "
            for p in item.get('content', []):
                for c in p.get('content', []):
                    res += parse_inline(c)
            res += "\n"
        res += "\n"
    elif t == 'blockquote':
        for p in content:
            res += "> "
            for c in p.get('content', []):
                res += parse_inline(c)
            res += "\n"
        res += "\n"
    elif t == 'image':
        url = block.get('attrs', {}).get('src', '')
        res += f"![]({url})\n\n"
    elif t == 'codeblock':
        res += "```\n"
        for c in content:
            res += c.get('text', '')
        res += "\n```\n\n"
    else:
        for c in content:
            res += parse_inline(c)
        if res.strip():
            res += "\n\n"
    return res

def fetch_and_parse_content_json(content_url):
    try:
        with urllib.request.urlopen(content_url) as response:
            content_json = json.loads(response.read().decode('utf-8'))
            blocks = content_json.get('content', [])
            md = ""
            for b in blocks:
                md += parse_block(b)
            return md
    except Exception as e:
        print(f"Error fetching content JSON: {e}")
        return ""

def sanitize_title(title):
    title = re.sub(r'[\\/*?:"<>|]', '', title)
    title = title.replace(' ', '-')
    return title

def main():
    articles = fetch_infoq_ai_articles(20)
    print(f"Fetched {len(articles)} articles from list API.")

    os.makedirs('_posts', exist_ok=True)

    for idx, article in enumerate(articles):
        uuid = article['uuid']
        print(f"Fetching detail for {uuid} ({idx+1}/20)...")
        detail = fetch_article_detail(uuid)
        time.sleep(0.5) # simple rate limit
        
        if not detail:
            print(f"Skipping {uuid} due to no detail.")
            continue
            
        content_url = detail.get('content_url')
        full_md_content = ""
        if content_url:
            full_md_content = fetch_and_parse_content_json(content_url)
        else:
            # fallback if content is directly in the detail API
            full_md_content = detail.get('content', '')
            
        dt = datetime.datetime.fromtimestamp(article['publish_time'] / 1000.0)
        date_str = dt.strftime('%Y-%m-%d')
        time_str = dt.strftime('%Y-%m-%d %H:%M:%S %z')
        
        title = article['article_title'].replace('"', "'")
        safe_title = sanitize_title(title)
        if not safe_title:
            safe_title = f"article-{idx}"
        
        filename = f"_posts/{date_str}-{safe_title}.md"
        
        author = article.get('author', '')
        if isinstance(author, list):
            author = ', '.join([a.get('nickname', '') for a in author]) if author and isinstance(author[0], dict) else ', '.join(map(str, author))
        if not author:
            author = article.get('no_author', 'InfoQ').replace('作者：', '')
        if isinstance(author, str):
            author = author.replace('"', "'")

        link = f"https://www.infoq.cn/article/{uuid}"
        
        content = f"""---
layout: post
title: "{title}"
tags: [AI, InfoQ, 人工智能]
comments: true
author: "{author}"
---

{full_md_content}

> *本文由 AI 助手自动生成并排版自 InfoQ，原文链接：[{title}]({link})*
"""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Generated {filename}")

if __name__ == "__main__":
    main()