from internet_speed_bot import InternetSpeedBot

bot = InternetSpeedBot()
bot.get_internet_speed()
bot.send_message()

print(f"Download speed: {bot.down} Mbps\n Upload speed: {bot.up} Mbps")

