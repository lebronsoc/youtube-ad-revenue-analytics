from bs4 import BeautifulSoup, element
import urllib.request
from urllib.request import Request
import pandas as pd
import numpy as np
import time

# -----------------------------
# SETTINGS
# -----------------------------
pages = 200  # increase as needed
sleep_time = 0.3

headers = {
    "User-Agent": "Mozilla/5.0"
}

# -----------------------------
# STORAGE
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
# URL
# -----------------------------
base_url = "http://www.vgchartz.com"
urlhead = base_url + "/gamedb/?page="
urltail = "&console=&region=All&developer=&publisher=&genre=&boxart=Both&ownership=Both"
urltail += "&results=1000&order=Sales&sort=GL"

# -----------------------------
# FETCH FUNCTION
# -----------------------------
def fetch(url):
    req = Request(url, headers=headers)
    return urllib.request.urlopen(req).read()

# -----------------------------
# MAIN LOOP
# -----------------------------
for page in range(1, pages):
    try:
        surl = urlhead + str(page) + urltail
        r = fetch(surl)
        soup = BeautifulSoup(r, "lxml")

        print(f"Page: {page}")

        # ✅ FIXED href handling (keeps original logic)
        game_tags = list(filter(
            lambda x: 'href' in x.attrs and '/game/' in x.attrs['href'],
            soup.find_all("a")
        ))[10:]

        for tag in game_tags:
            try:
                name = " ".join(tag.get_text().split())
                if not name:
                    continue

                print(f"{rec_count + 1} Fetch data for {name}")

                data = tag.parent.parent.find_all("td")
                if len(data) < 14:
                    continue

                # -----------------------------
                # CORE DATA
                # -----------------------------
                gname.append(name)
                rank.append(np.int32(data[0].get_text(strip=True)))

                img = data[3].find('img')
                platform.append(img.attrs['alt'] if img else None)

                publisher.append(data[4].get_text(strip=True))
                developer.append(data[5].get_text(strip=True))

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

                # -----------------------------
                # YEAR
                # -----------------------------
                release_year = data[13].get_text(strip=True).split()[-1]

                if release_year.startswith('N/A'):
                    year.append('N/A')
                else:
                    if len(release_year) == 2:
                        if int(release_year) >= 80:
                            year.append(np.int32("19" + release_year))
                        else:
                            year.append(np.int32("20" + release_year))
                    else:
                        year.append(np.int32(release_year))

                # -----------------------------
                # GENRE (kept intact but safer)
                # -----------------------------
                href = tag.attrs['href']
                if href.startswith("/"):
                    url_to_game = base_url + href
                else:
                    url_to_game = href

                try:
                    site_raw = fetch(url_to_game)
                    sub_soup = BeautifulSoup(site_raw, "html.parser")

                    info_box = sub_soup.find("div", {"id": "gameGenInfoBox"})

                    if info_box:
                        h2s = info_box.find_all('h2')
                        temp_tag = None

                        for h2 in h2s:
                            if h2.string == 'Genre':
                                temp_tag = h2

                        if temp_tag and temp_tag.next_sibling:
                            genre.append(temp_tag.next_sibling.string)
                        else:
                            genre.append(None)
                    else:
                        genre.append(None)

                except:
                    genre.append(None)

                rec_count += 1

                # -----------------------------
                # 💾 BACKUP EVERY 200 ROWS
                # -----------------------------
                if rec_count % 200 == 0:
                    df_temp = pd.DataFrame({
                        'Rank': rank,
                        'Name': gname,
                        'Platform': platform,
                        'Year': year,
                        'Genre': genre,
                        'Critic_Score': critic_score,
                        'User_Score': user_score,
                        'Publisher': publisher,
                        'Developer': developer,
                        'NA_Sales': sales_na,
                        'PAL_Sales': sales_pal,
                        'JP_Sales': sales_jp,
                        'Other_Sales': sales_ot,
                        'Global_Sales': sales_gl
                    })
                    df_temp.to_csv("vgsales_backup.csv", index=False)
                    print("💾 Backup saved")

                time.sleep(sleep_time)

            except Exception as e:
                print("Skipping row:", e)
                continue

    except Exception as e:
        print(f"Page failed: {e}")
        continue

# -----------------------------
# FINAL SAVE
# -----------------------------
df = pd.DataFrame({
    'Rank': rank,
    'Name': gname,
    'Platform': platform,
    'Year': year,
    'Genre': genre,
    'Critic_Score': critic_score,
    'User_Score': user_score,
    'Publisher': publisher,
    'Developer': developer,
    'NA_Sales': sales_na,
    'PAL_Sales': sales_pal,
    'JP_Sales': sales_jp,
    'Other_Sales': sales_ot,
    'Global_Sales': sales_gl
})

print(f"Total records scraped: {rec_count}")

df.to_csv("vgsales.csv", index=False)
print("Saved to vgsales.csv")
