from discord_webhook import DiscordWebhook, DiscordEmbed
import time
webhook = DiscordWebhook(url='https://discord.com/api/webhooks/818410902964928544/eqUtPxushAefCUOdrbVdXuYFbK2ubeFOS2pebDFOFSYMKnW8MZzXD6Bb-ssexCXst2ff')

inputfile="errors.txt"
while True:
    with open(inputfile, "r") as f1:
        line=""
        for line in f1: pass
        print(line)
        line1=""
        if len(line)>0 and line!=line1:
            print(line)
            embed = DiscordEmbed(title='Server Error!', description=str(line), color='0099ff')
            webhook.add_embed(embed)
            webhook.execute()
            line1=line
            line=""
            print(line)
    time.sleep(5)