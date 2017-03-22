# -*- coding: utf-8 -*-

import telebot
from yandex_translate import YandexTranslate

_token = '318773665:AAHVIEDqXl-j5GIzHusm1gfeb540Oz3B0JA'
translate = YandexTranslate('trnsl.1.1.20170322T195032Z.b8a59e9b139f58bf.4caf9c9f6c27097375a17a8b999126a931b018ec')

bot = telebot.TeleBot(_token)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_msg(message):
    print(message.text)
    from_lang = translate.detect(message.text)
    to_lang = '-pt' if from_lang == 'ru' else '-ru'
    trans_dir = from_lang + to_lang
    print(trans_dir)
    translated_message = translate.translate(message.text, trans_dir)

    bot.send_message(message.chat.id, translated_message['text'][0])


if __name__ == '__main__':
    bot.polling(none_stop=True)
