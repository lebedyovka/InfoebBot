# Nessesary part
import telebot
token = '8090315181:AAHrrn765Z5xf92KHQP26l2CtGtyx6BtKaw'
bot = telebot.TeleBot(token)
from urllib.parse import urlparse
from responds import IncorrectLink, SslDone, SslWrong, WafDone, WafFail, KukiDone, KukiFail
from responds import CSPDone, HTTPDone, XFOdone, AllDone, Helloy, Info

# Start reaction
@bot.message_handler(commands = ['start'])
def hello(message):
    bot.send_message(message.chat.id, Helloy)

# Information
@bot.message_handler(commands = ['info'])
def info(message):
    bot.send_message(message.chat.id, Info)

# MAIN CHECK
@bot.message_handler(commands = ['url'])
def sslchekout(message):
    user_message = message.text
    user_message = user_message.replace('/url', '').strip()

    try:
        domain = urlparse(user_message).netloc
        if domain:
            random_variable = 5
        else:
            bot.send_message(message.chat.id, IncorrectLink)
    except Exception as e:
        bot.send_message(message.chat.id, IncorrectLink)
    
    # SSL CHECK
    from sslchecker import check_cert
    if check_cert(domain):
        bot.send_message(message.chat.id, SslDone)
    else:
        bot.send_message(message.chat.id, SslWrong)

    #WAF CHECK
    from wafchecker import check_waf
    if check_waf(user_message):
        bot.send_message(message.chat.id, WafDone) 
    else:
        bot.send_message(message.chat.id, WafFail)
    
    #COOKIES CHECK
    from cookiecheck import cookies_security
    res = cookies_security(user_message)
    if res == 2:
        bot.send_message(message.chat.id, KukiDone)
    if res == 3:
        bot.send_message(message.chat.id, KukiFail)

    #HEADERS CHECK
    from headerscheck import security_headers
    present_headers = security_headers(user_message)
    if present_headers["Content-Security-Policy"]:
        bot.send_message(message.chat.id, CSPDone)
    if present_headers["Strict-Transport-Security"]:
        bot.send_message(message.chat.id, HTTPDone)
    if present_headers["X-Frame-Options"]:
        bot.send_message(message.chat.id, XFOdone)

    bot.send_message(message.chat.id, AllDone)

# Nessesary part
# venv\Scripts\activate
# python checkoutbot.py

if __name__ == '__main__':
    bot.infinity_polling()