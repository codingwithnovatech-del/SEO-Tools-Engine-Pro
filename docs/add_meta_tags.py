#!/usr/bin/env python3
"""Batch add OG tags, meta descriptions, canonical URLs to all pages"""
import os, re

def read_file(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()

def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

BASE = "https://seotoolsengine.com"

pages = {
    "about.html":       ("About Us - SEO Agency Pro", "Learn about SEO Agency Pro. We build free SEO tools to help website owners improve their search rankings and grow organic traffic."),
    "contact.html":     ("Contact Us - SEO Agency Pro", "Get in touch with SEO Agency Pro. Send us a message, and we'll respond as soon as possible. Free SEO tools and support."),
    "disclaimer.html":  ("Disclaimer - SEO Agency Pro", "Disclaimer for SEO Agency Pro. All tools and estimates are for guidance purposes only. Results may vary."),
    "login.html":       ("Sign In - SEO Agency Pro", "Sign in to your SEO Agency Pro dashboard or create a free account. Access your projects, keywords, and SEO reports."),
}

def add_tags(filepath, title, desc, is_tool=False, is_blog=False):
    if not os.path.exists(filepath):
        return False
    content = read_file(filepath)
    if is_tool:
        rel = "/tools/" + os.path.basename(filepath)
    elif is_blog:
        rel = "/blog/" + os.path.basename(filepath)
    else:
        name = os.path.basename(filepath)
        rel = "/" + name if name != "index.html" else "/"
    canonical = BASE + rel
    og_tags = f'<meta name="description" content="{desc}">\n  <meta property="og:title" content="{title}">\n  <meta property="og:description" content="{desc}">\n  <meta property="og:url" content="{canonical}">\n  <meta property="og:type" content="website">\n  <meta name="twitter:card" content="summary_large_image">\n  <link rel="canonical" href="{canonical}">'
    if 'og:title' in content:
        return False
    content = content.replace('</title>', '</title>\n  ' + og_tags, 1)
    write_file(filepath, content)
    return True

for page, (title, desc) in pages.items():
    path = os.path.join(".", page)
    if add_tags(path, title, desc):
        print(f"  Added tags: {page}")
    else:
        print(f"  Skipped (has OG): {page}")

print("\n--- Tool Pages ---")
tools_dir = "tools"
for f in sorted(os.listdir(tools_dir)):
    if f.endswith(".html"):
        path = os.path.join(tools_dir, f)
        content = read_file(path)
        name = f.replace(".html", "").replace("-", " ").title()
        if 'og:title' in content:
            print(f"  Skipped (has OG): {f}")
            continue
        title_match = re.search(r'<title>(.*?)</title>', content)
        desc_match = re.search(r'<meta name="description" content="([^"]*)"', content)
        existing_title = title_match.group(1) if title_match else f"{name} - SEO Agency Pro"
        existing_desc = desc_match.group(1) if desc_match else f"Free online {name.lower()} tool."
        if add_tags(path, existing_title, existing_desc, is_tool=True):
            print(f"  Added OG: {f}")

print("\n--- Blog Pages ---")
blog_dir = "blog"
for f in sorted(os.listdir(blog_dir)):
    if f.endswith(".html"):
        path = os.path.join(blog_dir, f)
        content = read_file(path)
        if 'og:title' in content:
            continue
        title_match = re.search(r'<title>(.*?)</title>', content)
        desc_match = re.search(r'<meta name="description" content="([^"]*)"', content)
        if title_match and desc_match:
            if add_tags(path, title_match.group(1), desc_match.group(1), is_blog=True):
                print(f"  Added OG: {f}")

print("\nDone!")
