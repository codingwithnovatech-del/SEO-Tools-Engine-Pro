#!/usr/bin/env python3
"""Generate complete sitemap.xml with all pages"""
import os, glob

BASE = "https://seotoolsengine.com"
TOOLS_DIR = "tools"
BLOG_DIR = "blog"

urls = []

static = [
    ("/", "weekly", "1.0"),
    ("/about.html", "monthly", "0.6"),
    ("/contact.html", "monthly", "0.6"),
    ("/privacy.html", "yearly", "0.3"),
    ("/disclaimer.html", "yearly", "0.3"),
    ("/terms.html", "yearly", "0.3"),
    ("/login.html", "monthly", "0.4"),
    ("/dashboard.html", "monthly", "0.4"),
    ("/admin.html", "monthly", "0.3"),
]
for path, freq, pri in static:
    urls.append((path, freq, pri))

for f in sorted(glob.glob(os.path.join(TOOLS_DIR, "*.html"))):
    name = os.path.basename(f)
    path = "/" + TOOLS_DIR + "/" + name
    pri = "0.9" if name != "index.html" else "0.8"
    urls.append((path, "weekly", pri))

for f in sorted(glob.glob(os.path.join(BLOG_DIR, "*.html"))):
    name = os.path.basename(f)
    path = "/" + BLOG_DIR + "/" + name
    pri = "0.8" if name != "index.html" else "0.7"
    urls.append((path, "monthly", pri))

xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for path, freq, pri in urls:
    xml += f'  <url><loc>{BASE}{path}</loc><lastmod>2026-06-07</lastmod><changefreq>{freq}</changefreq><priority>{pri}</priority></url>\n'
xml += '</urlset>'

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(xml)
print(f"Sitemap generated with {len(urls)} URLs")
