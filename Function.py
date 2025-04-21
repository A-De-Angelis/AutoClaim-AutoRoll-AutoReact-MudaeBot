import discum  # pip install discum
import json
import time
import requests
import Vars
import os
from discum.utils.slash import SlashCommander

botID = '432610292342587392'
auth = {'authorization': Vars.token}
bot = discum.Client(token=Vars.token, log=False)
url = f'https://discord.com/api/v8/channels/{Vars.channelId}/messages'


def log_roll(cardName, cardSeries, cardPower, claimed=False, reason=None):
    with open("rolls.log", "a", encoding="utf-8") as log_file:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        status = "CLAIMED" if claimed else "ROLLED"
        line = f"[{timestamp}] {status} - {cardName} ({cardSeries}) | Kakera: {cardPower}"
        if reason:
            line += f" | Reason: {reason}"
        log_file.write(line + "\n")


def get_claim_emoji(message):
    reactions = message[0].get("reactions", [])
    for r in reactions:
        emoji = r["emoji"]
        if emoji.get("name") in ['💖', '💘', '❤️', '💕', '💞', '💗', '💓']:
            return requests.utils.quote(emoji["name"])
        elif emoji.get("id") is not None:
            return f"{emoji['name']}:{emoji['id']}"
    return None


def simpleRoll():
    print(time.strftime("Rolling at %H:%M - %d/%m/%y", time.localtime()))
    i = 1
    x = 0
    claimed = '❤️'
    unclaimed = '🤍'
    kakera = '💎'
    rollCommand = SlashCommander(bot.getSlashCommands(botID).json()).get([Vars.rollCommand])
    continueRolling = True
    claimedThisCycle = False

    try:     # Convert kakeraClaim to int safely
        kakeraThreshold = int(Vars.kakeraClaim)
    except:
        kakeraThreshold = 0

    while continueRolling and not claimedThisCycle and x < 4:
        bot.triggerSlashCommand(botID, Vars.channelId, Vars.serverId, data=rollCommand)
        time.sleep(1.8)
        r = requests.get(url, headers=auth)
        jsonCard = json.loads(r.text)

        if len(jsonCard[0]['content']) != 0:
            x += 1
            continueRolling = False
            continue

        idMessage = jsonCard[0]['id']
        try:
            cardName = jsonCard[0]['embeds'][0]['author']['name']
            cardSeries = jsonCard[0]['embeds'][0]['description'].replace('\n', '**').split('**')[0]
            cardPower = int(jsonCard[0]['embeds'][0]['description'].split('**')[1])
        except (IndexError, KeyError, ValueError):
            cardName = 'null'
            cardSeries = 'null'
            cardPower = 0

        footer = jsonCard[0]['embeds'][0].get('footer', {}).get('text', '')

        if 'Claim Rank' in footer:
            print(i, ' - ' + claimed + ' ---- ', cardPower, ' - ' + cardName + ' - ' + cardSeries)
            log_roll(cardName, cardSeries, cardPower)
        else:
            print(i, ' - ' + unclaimed + ' ---- ', cardPower, ' - ' + cardName + ' - ' + cardSeries)

            claim_emoji = get_claim_emoji(jsonCard)
            if claim_emoji:
                # Always claim desired series
                if cardSeries in Vars.desiredSeries:
                    print(f'Claiming {cardName} from desired series: {cardSeries}')
                    requests.put(
                        f'https://discord.com/api/v8/channels/{Vars.channelId}/messages/{idMessage}/reactions/{claim_emoji}/%40me',
                        headers=auth
                    )
                    log_roll(cardName, cardSeries, cardPower, claimed=True, reason="Desired Series")
                    claimedThisCycle = True

                # Claim if above kakera threshold
                elif kakeraThreshold > 0 and cardPower >= kakeraThreshold:
                    print(f'Kakera value {cardPower} >= {kakeraThreshold}. Claiming {cardName}')
                    requests.put(
                        f'https://discord.com/api/v8/channels/{Vars.channelId}/messages/{idMessage}/reactions/{claim_emoji}/%40me',
                        headers=auth
                    )
                    log_roll(cardName, cardSeries, cardPower, claimed=True, reason="High Kakera")
                    claimedThisCycle = True
            else:
                print('No valid claim emoji found in reactions.')
                log_roll(cardName, cardSeries, cardPower)

        try:
            cardsKakera = jsonCard[0]['components'][0]['components'][0]['emoji']['name']
            components = jsonCard[0]["components"][0]['components']
            for index in range(len(components)):
                if cardsKakera in Vars.desiredKakeras:
                    x -= 1
                    print(kakera + ' - ' + kakera + ' - Trying to react to ' + cardsKakera + ' of ' + cardName)
                    bot.click(
                        jsonCard[0]['author']['id'],
                        channelID=jsonCard[0]['channel_id'],
                        guildID=Vars.serverId,
                        messageID=jsonCard[0]['id'],
                        messageFlags=jsonCard[0]['flags'],
                        data={'component_type': 2, 'custom_id': components[index]['custom_id']}
                    )
                    time.sleep(0.5)
        except (IndexError, KeyError, TypeError):
            pass

        i += 1

    print('Rolling ended')

    if Vars.pokeRoll:
        print('\nTrying to roll Pokeslot')
        requests.post(url=url, headers=auth, data={'content': '$p'})
