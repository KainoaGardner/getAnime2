from selenium import webdriver
from selenium.webdriver.common.by import By
from app.functions.cache import save_cache

from app.env import LIVECHART_URL


def webscrape(week):
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    driver = webdriver.Remote(
        options=options,
        command_executor="http://chrome:4444/wd/hub",
    )

    driver.get(LIVECHART_URL)
    driver.find_element(By.XPATH, '//*[@title="Full Layout"]').click()

    weekly_object = get_weekly_object(week, driver)
    save_cache("app/cache/weekly.json", weekly_object)
    driver.quit()


def get_weekly_object(
    week, driver
):  # webscrape website for id ep and air day create dict of all entries
    weekly_object = {"week": week, "data": {}}
    days = driver.find_elements(By.CLASS_NAME, "text-2xl")
    day_blocks = driver.find_elements(By.CLASS_NAME, "lc-grid-template-anime-cards")
    for count, day in enumerate(days[1:]):
        day_block = day_blocks[count]
        anime_lists = day_block.find_elements(By.CLASS_NAME, "lc-anime-card")

        for anime in anime_lists:
            try:
                anime_title = anime.find_element(By.CLASS_NAME, "lc-anime-card--title")
                mal_id = anime.find_element(By.CLASS_NAME, "mal")
                mal_id = int(mal_id.get_attribute("href").split("/")[-1])
                ep_count = anime.find_element(By.CLASS_NAME, "font-medium")

                weekly_object["data"].update(
                    {
                        mal_id: {
                            "title": anime_title.text,
                            "airing_day": day.text,
                            "episode": ep_count.text,
                        }
                    }
                )
            except:
                continue
    return weekly_object
