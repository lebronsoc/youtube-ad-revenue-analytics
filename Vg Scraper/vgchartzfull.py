from bs4 import BeautifulSoup
import urllib.request
from urllib.request import Request
import pandas as pd
import numpy as np
import time

# -----------------------------
# Settings
# -----------------------------
PAGES = 19  # original script used 19, which loops from 1 to 18
SLEEP_SECONDS = 1  # be polite to the site and reduce blocking risk

# -----------------------------
# Storage lists
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
urlhead = "http://www.vgchartz.com/gamedb/?page="
urltail = "&console=&region=All&developer=&publisher=&genre=&boxart=Both&ownership=Both"
urltail += "&results=1000&order=Sales&showtotalsales=0&showtotalsales=1&showpublisher=0"
urltail += "&showpublisher=1&showvgchartzscore=0&shownasales=1&showdeveloper=1&showcriticscore=1"
urltail += "&showpalsales=0&showpalsales=1&showreleasedate=1&showuserscore=1&showjapansales=1"
urltail += "&showlastupdate=0&showothersales=1&showgenre=1&sort=GL"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

def fetch_html(url):
    req = Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        return response.read()

def safe_text(tag):
    if tag is None:
        return None
    if tag.string is not None:
        return " ".join(tag.string.split())
    text = tag.get_text(" ", strip=True)
    return " ".join(text.split()) if text else None

def parse_float(value):
    if value is None:
        return np.nan
    value = value.strip()
    if value.startswith("N/A") or value == "":
        return np.nan
    try:
        return float(value[:-1]) if value.endswith("%") else float(value)
    except:
        return np.nan

def parse_year(value):
    if value is None:
        return "N/A"
    value = value.strip()
    if value.startswith("N/A") or value == "":
        return "N/A"
    try:
        release_year = value.split()[-1]
        if len(release_year) == 2 and release_year.isdigit():
            if int(release_year) >= 80:
                return np.int32("19" + release_year)
            else:
                return np.int32("20" + release_year)
        if len(release_year) == 4 and release_year.isdigit():
            return np.int32(release_year)
    except:
        pass
    return "N/A"

def get_genre_from_game_page(game_url):
    try:
        site_raw = fetch_html(game_url)
        sub_soup = BeautifulSoup(site_raw, "html.parser")

        info_box = sub_soup.find("div", {"id": "gameGenInfoBox"})
        if not info_box:
            return None

        h2s = info_box.find_all("h2")

        for h2 in h2s:
            if h2.string and h2.string.strip() == "Genre":
                # The genre is usually the next sibling text node
                next_node = h2.next_sibling
                if next_node is None:
                    return None
                genre_text = str(next_node).strip()
                return genre_text if genre_text else None

        return None
    except:
        return None

# -----------------------------
# Main scrape loop
# -----------------------------
for page in range(1, PAGES):
    surl = urlhead + str(page) + urltail

    try:
        r = fetch_html(surl)
        soup = BeautifulSoup(r, "lxml")
        print(f"Page: {page}")
    except Exception as e:
        print(f"Failed to load page {page}: {e}")
        continue

    # Find only links that actually have an href and point to game pages
    all_a_tags = soup.find_all("a", href=True)
    game_tags = [
        a for a in all_a_tags
        if a.get("href", "").startswith("http://www.vgchartz.com/game/")
    ]

    # Keep the original script's behavior of skipping navigation links,
    # but only if there are enough tags to skip.
    if len(game_tags) > 10:
        game_tags = game_tags[10:]

    for tag in game_tags:
        try:
            game_name = safe_text(tag)
            if not game_name:
                continue

            gname.append(game_name)
            print(f"{rec_count + 1} Fetch data for game {gname[-1]}")

            # Move up the DOM tree to the table row
            data = tag.parent.parent.find_all("td")

            # Skip broken or unexpected rows
            if len(data) < 14:
                continue

            rank.append(np.int32(data[0].get_text(strip=True)))
            platform_tag = data[3].find("img")
            platform.append(platform_tag.attrs["alt"] if platform_tag and "alt" in platform_tag.attrs else None)
            publisher.append(safe_text(data[4]))
            developer.append(safe_text(data[5]))

            critic_score.append(
                float(data[6].get_text(strip=True))
                if not data[6].get_text(strip=True).startswith("N/A") else np.nan
            )
            user_score.append(
                float(data[7].get_text(strip=True))
                if not data[7].get_text(strip=True).startswith("N/A") else np.nan
            )

            sales_gl.append(
                float(data[8].get_text(strip=True)[:-1])
                if not data[8].get_text(strip=True).startswith("N/A") else np.nan
            )
            sales_na.append(
                float(data[9].get_text(strip=True)[:-1])
                if not data[9].get_text(strip=True).startswith("N/A") else np.nan
            )
            sales_pal.append(
                float(data[10].get_text(strip=True)[:-1])
                if not data[10].get_text(strip=True).startswith("N/A") else np.nan
            )
            sales_jp.append(
                float(data[11].get_text(strip=True)[:-1])
                if not data[11].get_text(strip=True).startswith("N/A") else np.nan
            )
            sales_ot.append(
                float(data[12].get_text(strip=True)[:-1])
                if not data[12].get_text(strip=True).startswith("N/A") else np.nan
            )

            year.append(parse_year(safe_text(data[13])))

            # Genre from individual game page
            url_to_game = tag.get("href")
            game_genre = get_genre_from_game_page(url_to_game)
            genre.append(game_genre)

            rec_count += 1

            time.sleep(SLEEP_SECONDS)

        except Exception as e:
            print(f"Skipping a row because of error: {e}")
            continue

# -----------------------------
# Build dataframe and save CSV
# -----------------------------
columns = {
    "Rank": rank,
    "Name": gname,
    "Platform": platform,
    "Year": year,
    "Genre": genre,
    "Critic_Score": critic_score,
    "User_Score": user_score,
    "Publisher": publisher,
    "Developer": developer,
    "NA_Sales": sales_na,
    "PAL_Sales": sales_pal,
    "JP_Sales": sales_jp,
    "Other_Sales": sales_ot,
    "Global_Sales": sales_gl
}

print(f"Total records scraped: {rec_count}")

df = pd.DataFrame(columns)

print(df.columns)

df = df[[
    "Rank", "Name", "Platform", "Year", "Genre",
    "Publisher", "Developer", "Critic_Score", "User_Score",
    "NA_Sales", "PAL_Sales", "JP_Sales", "Other_Sales", "Global_Sales"
]]

df.to_csv("vgsales.csv", sep=",", encoding="utf-8", index=False)
print("Saved to vgsales.csv")
