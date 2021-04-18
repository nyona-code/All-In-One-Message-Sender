from instabot import Bot

filename = ""
def instagram(filename, msg):
  bot = Bot()
  bot.login(username = "cs321testgroup3", 
          password = "Pass!word")
  bot.upload_photo(filename, caption = msg)
  
      
                                                                                                  