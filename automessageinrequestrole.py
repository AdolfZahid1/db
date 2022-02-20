from discord_webhook import DiscordWebhook, DiscordEmbed
import schedule,time

webhook = DiscordWebhook(url='https://discord.com/api/webhooks/818409835590058035/D9hfMGeb7-YOGgD5av4qwWHtTGY66OdFpaNfgGmolnPzU5CdvOwl_deuS6VB2vJqhzwG')
embed = DiscordEmbed(title='', description='''
Для того чтобы получить доступ к другим каналам и стать частью юнита, вам для начала нужно ознакомиться с правилами (<#620337566671044688>)и сменить ник: ["CR-"Номер" "Позывной" [88th]"], после запросить роль <@&608564553835479061>

Если вы не можете играть, но хотите дальше участвовать в юните, доступна роль - <@&751443638227042345>
Если вы не участвуете в жизни юнита более месяца вас переводят на роль - <@&751443638227042345>

-Выглядеть это будет примерно так: CR-3361 Koov  [88th]''', color='0099ff')
webhook.add_embed(embed)

def messagesend():
    response = webhook.execute()

schedule.every().monday.at("13:00").do(messagesend)
print("started!")
while True:
    schedule.run_pending()
    time.sleep(1)