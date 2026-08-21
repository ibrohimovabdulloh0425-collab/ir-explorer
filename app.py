import json
from datetime import datetime

import feedparser
import requests
from bs4 import BeautifulSoup

# 1. Kun.uz yangiliklarini olish va filtrlash
rss_url = "https://kun.uz/news/rss"
print("📡 Kun.uz'dan yangilik yuklanmoqda...\n")

feed = feedparser.parse(rss_url)

keywords = [
    # Iqtisodiyot
    "iqtisod", "iqtisodiyot", "moliya", "bank", "valyuta", "kurs",
    "byudjet", "soliq", "inflyatsiya", "investitsiya", "investor",
    "eksport", "import", "savdo", "narx", "narxlar", "bozor",
    "YIM", "YaIM", "kredit", "qarz", "energetika", "neft", "gaz",
    # Biznes
    "biznes", "tadbirkorlik", "tadbirkor", "kompaniya", "startap",
    "loyiha", "ishlab chiqarish", "eksportchi", "sanoat", "korxona",
    # Siyosat
    "siyosat", "prezident", "hukumat", "vazirlik", "vazir",
    "parlament", "senat", "qonun", "farmon", "qaror",
    "diplomatiya", "xalqaro", "tashqi siyosat", "vashington",
    "moskva", "pekin", "brussel", "sammit", "muzokara"
]

max_news_count = 5
selected_news_list = []

for entry in feed.entries:
    text_to_check = entry.title.lower()
    if hasattr(entry, "summary"):
        text_to_check += " " + entry.summary.lower()

    if any(kw in text_to_check for kw in keywords):
        selected_news_list.append(entry)

    if len(selected_news_list) >= max_news_count:
        break

if not selected_news_list:
    print("⚠️ Mos mavzudagi yangilik topilmadi, oxirgi yangiliklar olinmoqda...\n")
    selected_news_list = feed.entries[:max_news_count]

print(f"📰 {len(selected_news_list)} ta mos yangilik topildi.\n")


def get_full_article(url):
    """Havoladagi sahifadan to'liq maqola matnini va rasmini ajratib oladi."""
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        page = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(page.content, "html.parser")

        # To'liq matn — barcha <p> teglarini yig'amiz
        paragraphs = soup.find_all("p")
        article_text = "\n\n".join(
            p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)
        )

        # Asosiy rasmni topishga urinib ko'ramiz (Open Graph tegidan)
        image_url = None
        og_image = soup.find("meta", property="og:image")
        if og_image and og_image.get("content"):
            image_url = og_image["content"]

        return article_text if article_text else None, image_url
    except Exception as e:
        print(f"⚠️ Maqolani yuklashda xatolik: {e}")
        return None, None


# 2. Har bir yangilikning to'liq ma'lumotini yig'amiz
results_for_json = []

for i, news in enumerate(selected_news_list, start=1):
    title = news.title
    link = news.link
    published = news.published if hasattr(news, "published") else None

    print(f"📌 {i}-Yangilik: {title}")
    print(f"🔗 Havola: {link}")
    print("📄 To'liq matn yuklanmoqda...\n")

    full_text, image_url = get_full_article(link)

    if not full_text:
        # Agar to'liq matnni ololmasa, RSS'dagi qisqacha tavsifga qaytadi
        full_text = news.summary if hasattr(news, "summary") else "Matn topilmadi."
        print("⚠️ To'liq matn topilmadi, RSS tavsifi ishlatildi.\n")

    results_for_json.append({
        "title": title,
        "link": link,
        "published": published,
        "image": image_url,
        "text": full_text
    })

    print("=" * 60 + "\n")

# 3. Natijalarni JSON faylga yozish — index.html shu faylni o'qiydi
output_data = {
    "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "results": results_for_json
}

with open("news_analysis.json", "w", encoding="utf-8") as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print("✅ Natijalar 'news_analysis.json' fayliga yozildi.")
print("   Endi index.html sahifasidagi '📰 Yangiliklar' bo'limida ko'rishingiz mumkin.") 
    