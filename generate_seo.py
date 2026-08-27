import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_URL = "https://goldentherapy2.netlify.app"

urls = [f"{BASE_URL}/"]

for root, dirs, files in os.walk(BASE_DIR):
    if "index.html" in files and root != BASE_DIR:
        rel_path = os.path.relpath(root, BASE_DIR).replace("\\", "/")
        urls.append(f"{BASE_URL}/{rel_path}/")

sitemap_content = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for url in urls:
    sitemap_content.append(f"  <url><loc>{url}</loc><priority>0.8</priority></url>")
sitemap_content.append('</urlset>')

with open(os.path.join(BASE_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write("\n".join(sitemap_content))

with open(os.path.join(BASE_DIR, "robots.txt"), "w", encoding="utf-8") as f:
    f.write(f"User-agent: *\nAllow: /\n\nSitemap: {BASE_URL}/sitemap.xml\n")

print("✅ sitemap.xml 및 robots.txt 갱신 완료")

