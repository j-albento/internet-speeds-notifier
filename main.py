import os
from internet_speed_bot import InternetSpeedBot

CHROME_DRIVER_PATH = os.environ["CHROME_DRIVER_PATH"]

bot = InternetSpeedBot()
bot.get_internet_speed()
bot.send_message()

print(f"Download speed: {bot.down} Mbps\n Upload speed: {bot.up} Mbps")

