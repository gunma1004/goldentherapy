import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_URL = "https://goldentherapy2.netlify.app"

# sitemap에 포함할 URL 목록 (메인 페이지 우선 추가)
urls = [{"loc": f"{BASE_URL}/", "priority": "1.0", "changefreq": "daily"}]

# 제외할 디렉터리 목록 (정적 자산, 템플릿 등)
EXCLUDE_DIRS = {".git", ".github", "css", "images", "js", "__pycache__"}

for root, dirs, files in os.walk(BASE_DIR):
    # 제외 대상 디렉터리 필터링
    dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
    
    if "index.html" in files and root != BASE_DIR:
        rel_path = os.path.relpath(root, BASE_DIR).replace("\\", "/")
        
        # 구/동 페이지는 priority 0.8 설정
        urls.append({
            "loc": f"{BASE_URL}/{rel_path}/",
            "priority": "0.8",
            "changefreq": "weekly"
        })

# sitemap.xml 생성
sitemap_content = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
]

for item in urls:
    sitemap_content.append("  <url>")
    sitemap_content.append(f"    <loc>{item['loc']}</loc>")
    sitemap_content.append(f"    <changefreq>{item['changefreq']}</changefreq>")
    sitemap_content.append(f"    <priority>{item['priority']}</priority>")
    sitemap_content.append("  </url>")

sitemap_content.append('</urlset>')

with open(os.path.join(BASE_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write("\n".join(sitemap_content))

# robots.txt 생성
robots_content = f"""User-agent: *
Allow: /

Sitemap: {BASE_URL}/sitemap.xml
"""

with open(os.path.join(BASE_DIR, "robots.txt"), "w", encoding="utf-8") as f:
    f.write(robots_content)

print(f"✅ sitemap.xml ({len(urls)}개 URL) 및 robots.txt 갱신 완료")
