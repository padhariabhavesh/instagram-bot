from instabot import Bot
bot=Bot()

bot.login(username="enter username", password="password")
#upload min 10 tags
tags=['padharia','python']

for i in tags:
    bot.like_hashtag(i,amount=5)