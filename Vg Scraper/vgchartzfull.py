from bs4 import BeautifulSoup
import urllib.request
from urllib.request import Request
import pandas as pd
import numpy as np
import time

# -----------------------------
# Settings
# -----------------------------
PAGES = 200   # increase to scrape more (adjust if needed)
SLEEP_SECONDS = 1

# -----------------------------
# Storage
# -----------------------------
rec_count = 0
rank = []
gname = []
platform = []
year = []
genre = []
critic_score = []
user_score = []
publisher = []
developer = []
sales_na = []
sales_pal = []
sales_jp = []
sales_ot = []
sales_gl = []

# -----------------------------
# URLs
# -----------------------------
BASE_URL = "http://www.vgchartz.com"

urlhead = BASE_URL + "/gamedb/?page="
urltail = "&console=&region=All&developer=&publisher=&genre=&boxart=Both&ownership=Both"
urltail += "&results=1000&order=Sales&showtotalsales=0&showtotalsales=1&showpublisher=0"
urltail += "&showpublisher=1&showvgchartzscore=0&shownasales=1&showdeveloper=1&showcriticscore=1"
urltail += "&showpalsales=0&showpalsales=1&showreleasedate=1&showuserscore=1&showjapansales=1"
urltail += "&showlastupdate=0&showothersales=1&showgenre=1&sort=GL"

headers = {
    "User-Agent": "Mozilla/5.0"
}

def fetch_html(url):
    req = Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        return response.read()

def safe_text(tag):
    if tag and tag.get_text():
        return tag.get_text(strip=True)
    return None

def parse_float(text):
    if not text or text.startswith("N/A"):
        return np.nan
    try:
        return float(text[:-1])
    except:
        return np.nan

def parse_year(text):
    if not text or text.startswith("N/A"):
        return "N/A"
    try:
        year_part = text.split()[-1]
        if len(year_part) == 2:
            return int("19" + year_part) if int(year_part) >= 80 else int("20" + year_part)
        return int(year_part)
    except:
        return "N/A"

def get_full_url(href):
    if href.startswith("/"):
        return BASE_URL + href
    return href

def get_genre(game_url):
    try:
        html = fetch_html(game_url)
        soup = BeautifulSoup(html, "html.parser")

        info_box = soup.find("div", {"id": "gameGenInfoBox"})
        if not info_box:
            return None

        for h2 in info_box.find_all("h2"):
            if h2.string and "Genre" in h2.string:
                sibling = h2.next_sibling
                return str(sibling).strip() if sibling else None

        return None
    except:
        return None

# -----------------------------
# Main loop
# -----------------------------
for page in range(1, PAGES):
    try:
        url = urlhead + str(page) + urltail
        html = fetch_html(url)
        soup = BeautifulSoup(html, "lxml")

        print(f"Page: {page}")

        # FIXED: handle relative URLs
        links = soup.find_all("a", href=True)
        game_tags = [a for a in links if "/game/" in a["href"]]

        if len(game_tags) > 10:
            game_tags = game_tags[10:]

        for tag in game_tags:
            try:
                name = safe_text(tag)
                if not name:
                    continue

                data = tag.parent.parent.find_all("td")
                if len(data) < 14:
                    continue

                gname.append(name)
                print(f"{rec_count + 1} Fetch data for {name}")

                rank.append(int(data[0].get_text(strip=True)))

                img = data[3].find("img")
                platform.append(img["alt"] if img else None)

                publisher.append(safe_text(data[4]))
                developer.append(safe_text(data[5]))

                critic_score.append(parse_float(data[6].get_text(strip=True)))
                user_score.append(parse_float(data[7].get_text(strip=True)))

                sales_gl.append(parse_float(data[8].get_text(strip=True)))
                sales_na.append(parse_float(data[9].get_text(strip=True)))
                sales_pal.append(parse_float(data[10].get_text(strip=True)))
                sales_jp.append(parse_float(data[11].get_text(strip=True)))
                sales_ot.append(parse_float(data[12].get_text(strip=True)))

                year.append(parse_year(safe_text(data[13])))

                # FIXED: full URL for game page
                game_url = get_full_url(tag["href"])
                genre.append(get_genre(game_url))

                rec_count += 1
                time.sleep(SLEEP_SECONDS)

            except Exception as e:
                print("Skipping row:", e)
                continue

    except Exception as e:
        print(f"Failed page {page}: {e}")
        continue

# -----------------------------
# Save data
# -----------------------------
df = pd.DataFrame({
    "Rank": rank,
    "Name": gname,
    "Platform": platform,
    "Year": year,
    "Genre": genre,
    "Publisher": publisher,
    "Developer": developer,
    "Critic_Score": critic_score,
    "User_Score": user_score,
    "NA_Sales": sales_na,
    "PAL_Sales": sales_pal,
    "JP_Sales": sales_jp,
    "Other_Sales": sales_ot,
    "Global_Sales": sales_gl
})

print(f"Total records scraped: {rec_count}")

df.to_csv("vgsales.csv", index=False)
print("Saved to vgsales.csv")
