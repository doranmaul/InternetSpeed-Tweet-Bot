from InternetBot import InternetSpeedTwitterBot
import time

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider(down=bot.down, up=bot.up)

time.sleep(5)

bot.driver.quit()



