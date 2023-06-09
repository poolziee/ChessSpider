from config import config
import chrome_driver
from random import randrange
from time import sleep
from selenium.webdriver.common.by import By

def randsleep ():
    """
    Delay execution with 2 or 3 seconds.
    """
    sleep(randrange(2, 4))

username = config['chess-username']
page_nr = config['start-page']
last_page_nr = config['end-page']

driver = chrome_driver.start()
driver.maximize_window()

while page_nr <= last_page_nr :
    print(f"Crawling page number {page_nr}...")
    driver.get(f"https://www.chess.com/games/archive/{username}?gameOwner=my_game&gameTypes%5B0%5D=chess960&gameTypes%5B1%5D=daily&gameType=live&page={page_nr}")
    overview_tab = driver.current_window_handle
    games = driver.find_elements(By.XPATH, '//a[contains(@class,"archive-games-link") and contains(text(), "Review")]')
    if len(games) > 0:
        print (f"Begin analysing {len(games)} games...")
        for idx, game in enumerate(games):
            game_url = game.get_attribute('href')
            driver.switch_to.new_window('tab')
            driver.get(game_url)
            randsleep()
            driver.close()
            print(f"Analysed game {idx + 1}: {game_url}")
            randsleep()
            driver.switch_to.window(overview_tab)
    else:
        print("No games found on the current page.")
    page_nr = page_nr + 1
    randsleep()

print("Analysis complete.")