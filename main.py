import requests
import datetime

from bothandler import BotHandler

token = ""

jokes_bot = BotHandler(token)
greetings = ('hello', 'hi', 'greetings', 'sup')
now = datetime.datetime.now()


def main():
    new_offset = None
    today = now.day
    hour = now.hour

    while True:
        jokes_bot.get_updates(new_offset)

        last_update = jokes_bot.get_last_update()
        get_joke = jokes_bot.get_jokes()

        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['from']['first_name']

        if last_chat_text.lower() in greetings and today == now.day and 6 <= hour < 12:
            jokes_bot.send_message(last_chat_id, 'Good Morning  {}'.format(last_chat_name))
            today += 1

        elif last_chat_text.lower() in greetings and today == now.day and 12 <= hour < 17:
            jokes_bot.send_message(last_chat_id, 'Good Afternoon {}'.format(last_chat_name))
            today += 1

        elif last_chat_text.lower() in greetings and today == now.day and 17 <= hour < 23:
            jokes_bot.send_message(last_chat_id, 'Good Evening  {}'.format(last_chat_name))
            today += 1

        elif last_chat_text.lower() == "/jokes" or last_chat_text.lower() == "/jokes":

            jokes_bot.send_message(last_chat_id, get_joke)

        elif hour == 11:
            jokes_bot.send_message(last_chat_id, get_joke)

        new_offset = last_update_id + 1


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
