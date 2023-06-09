
# ChessSpider

ChessSpider is a short script which will automatically browse through your chess.com Live games archive and analyse all games, given start and end page numbers.

The archive page used by ChessSpider: https://www.chess.com/games/archive?gameOwner=my_game&gameType=live

## Prerequisites

- You have the Unlimited Game Review feature enabled (Platinum or Diamond subscription) on chess.com.
- You are logged in your chess.com account via Chrome.
- You have the Selenium WebDriver package (v4.10.0 or above) in your Python environment.
- You have ChromeDrive on your machine (https://chromedriver.chromium.org/downloads).
    Download the driver version that matches your Chrome version. To check your version, go to chrome://version.

## Configurations

Before you execute *spider.py*, you need to add a *config.json* file to the src directory containing the following values:

- `"start-page"`: The page number from which you want the script to start browsing and analyzing games. (Games archive link from the introduction above)

- `"end-page"`: The page number at which you want the script to stop browsing and analyzing games. (Games archive link from the introduction above)

- `"driver-path"`: The file path to the ChromeDriver executable on your machine.

- `"user-data-dir"`: The file path to the user data directory of your Chrome profile. See `Profile Path` at chrome://version, excluding the last directory from the path.

- `"profile-directory"`: The name of the Chrome profile directory to use. This is the directory you have excluded from `"user-data-dir"`.

Example *config.json* file:
```json
{
  "start-page": 1,
  "end-page": 100,
  "driver-path": "C:/Drivers/ChromeDriver/chromedriver.exe",
  "user-data-dir": "C:/Users/username/AppData/Local/Google/Chrome/User Data",
  "profile-directory": "Default"
}
```

## How to use

The script can be executed successfully only if all Prerequisites are fulfilled, and a *config.json* containing the correct values is present in the src directory.

Make sure Chrome is closed before you run the script, otherwise, it won't work.

After you run *spider.py*, it will open Chrome and do its job. You should see some logs in the terminal which started the script.

Keep in mind the process might take a while, depending on how many pages you requested.
The spider uses timeout before each action intentionally, to (pseudo) mimic human behaviour.
Even with this speed, some small percentage of your games might not be analysed.
In this case, I would recommend running the script several times while looking at the terminal logs. (Each time will be faster because there would be fewer and fewer games left to analyse).
