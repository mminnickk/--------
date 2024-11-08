import requests
from bs4 import BeautifulSoup

# URL에서 HTML 가져오기
url = "https://https://www.google.com/?hl=ko"
response = requests.get(url)
html_content = response.text

# BeautifulSoup으로 HTML 파싱
soup = BeautifulSoup(html_content, "html.parser")

# 주요 요소 추출하기
title = soup.title.string if soup.title else "No Title"
main_heading = soup.find("h1").get_text(strip=True) if soup.find("h1") else "No Main Heading"
paragraphs = [p.get_text(strip=True) for p in soup.find_all("p")[:5]]  # 상위 5개 문단 추출
images = [img['src'] for img in soup.find_all("img", src=True)[:3]]  # 상위 3개 이미지 src 추출

# 간단한 HTML 템플릿으로 구성
template = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Site Overview</title>
</head>
<body>
    <h1>{title}</h1>
    <h2>Main Heading: {main_heading}</h2>
    <h3>Top Paragraphs:</h3>
    {"".join([f"<p>{para}</p>" for para in paragraphs])}
    <h3>Top Images:</h3>
    {"".join([f'<img src="{img}" alt="Image" style="max-width: 200px;"/>' for img in images])}
</body>
</html>
"""

# 결과 HTML 파일로 저장
with open("site_overview.html", "w", encoding="utf-8") as file:
    file.write(template)

print("site_overview.html 파일로 저장되었습니다.")
