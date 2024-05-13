"""
Dev : @DF_GD_D
Ch : @T62RS
In :- 2024/5/2
"""
import telebot, requests, re
from requests.structures import CaseInsensitiveDict as CID
t0k3n = "6904212187:AAGcd407_vNUXcC0IxVpgLnJxpoM6e2_BxU"
b0t = telebot.TeleBot(t0k3n)
l4ng = {}
@b0t.message_handler(commands=["start"])
def st4rt(m3ss4g3):
    if m3ss4g3.chat.id not in l4ng:
        l4ng[m3ss4g3.chat.id] = "ar"
    pr1v4t3l1n3 = telebot.types.InlineKeyboardMarkup()
    pr1v4t3l1n3.add(telebot.types.InlineKeyboardButton("🔄 تبديل اللغة", callback_data="l4ng"))
    if l4ng[m3ss4g3.chat.id] == "ar":
        b0t.send_message(m3ss4g3.chat.id, """
🎥 | مرحبا بك عزيزي في بوت  Cam-Hackers لاختراق كاميرات المراقبه 
🇮🇶 | ارسل رمز الدولة التي تود اختراق كاميرات مراقبه منها :
📝 | على سبيل المثال : (السعودية : SA) 
📞 | المطور : @DF_GD_D 
""", reply_markup=pr1v4t3l1n3)
    else:
        b0t.send_message(m3ss4g3.chat.id, """
🎥 | Welcome to Cam bot, surveillance cameras 
🇮🇶 | Send the country code you want to fetch from :
📝 | For example : (Saudi Arabia : SA) 
📞 | Developer : @DF_GD_D 
""", reply_markup=pr1v4t3l1n3)

@b0t.callback_query_handler(func=lambda c4ll: True)
def c4llb4ck(c4ll):
    if c4ll.data == "l4ng":
        pr1v4t3l1n3 = telebot.types.InlineKeyboardMarkup()
        pr1v4t3l1n3.add(telebot.types.InlineKeyboardButton("🇮🇶 العربية ", callback_data="ar"),
                   telebot.types.InlineKeyboardButton("🇬🇧 English", callback_data="en"))
        b0t.send_message(c4ll.message.chat.id, """
🇮🇶 | اختر لغة الادخال :
🇬🇧 | Select Input Language :
""", reply_markup=pr1v4t3l1n3)
    elif c4ll.data == "ar":
        l4ng[c4ll.message.chat.id] = "ar"
        pr1v4t3l1n3 = telebot.types.InlineKeyboardMarkup()
        pr1v4t3l1n3.add(telebot.types.InlineKeyboardButton("🔄 تبديل اللغة", callback_data="l4ng"))
        b0t.send_message(c4ll.message.chat.id, """
🎥 | مرحبا بك عزيزي في بوت Cam كاميرات المراقبه 
🇮🇶 | ارسل رمز الدولة التي تود جلب   منها :
📝 | على سبيل المثال : (السعودية : SA) 
📞 | المطور : @DF_GD_D 
""", reply_markup=pr1v4t3l1n3)
    elif c4ll.data == "en":
        l4ng[c4ll.message.chat.id] = "en"
        pr1v4t3l1n3 = telebot.types.InlineKeyboardMarkup()
        pr1v4t3l1n3.add(telebot.types.InlineKeyboardButton("Change Language 🔄", callback_data="l4ng"))
        b0t.send_message(c4ll.message.chat.id, """
🎥 | Welcome to Cam bot, surveillance cameras 
🇮🇶 | Send the country code you want to fetch from :
📝 | For example : (Saudi Arabia : SA) 
📞 | Developer : @DF_GD_D 
""", reply_markup=pr1v4t3l1n3)

@b0t.message_handler(func=lambda m3ss4g3: True)
def c0untr13s(m3ss4g3):
    c0untry_c0d3 = m3ss4g3.text.upper()
    url = f"http://www.insecam.org/en/bycountry/{c0untry_c0d3}"
    h34d3rs = CID()
    h34d3rs["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
    h34d3rs["Cache-Control"] = "max-age=0"
    h34d3rs["Connection"] = "keep-alive"
    h34d3rs["Host"] = "www.insecam.org"
    h34d3rs["Upgrade-Insecure-Requests"] = "1"
    h34d3rs["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    r3sp = requests.get(url, headers=h34d3rs)
    if r3sp.status_code == 200:
        l4st_p4g3 = re.findall(r'pagenavigator\("\?page=", (\d+)', r3sp.text)[0]
        ipl4st = []
        for p4g3 in range(int(l4st_p4g3)):
            r3s = requests.get(f"http://www.insecam.org/en/bycountry/{c0untry_c0d3}/?page={p4g3}", headers=h34d3rs)
            f1nd_1p = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", r3s.text)
            ipl4st.extend(f1nd_1p)
        with open(f"{c0untry_c0d3}.txt", 'w') as f:
            for ip in ipl4st:
                f.write(f"{ip}\n")
        if l4ng[m3ss4g3.chat.id] == "ar":
            b0t.send_message(m3ss4g3.chat.id, """
💻 | تم إيجاد 
⚜️ | العدد :  {len(ipl4st)}
""")
        else:
            b0t.send_message(m3ss4g3.chat.id, """
💻 | Found 
⚜️ | Number :  {len(ipl4st)}
""")
        b0t.send_document(m3ss4g3.chat.id, open(f"{c0untry_c0d3}.txt", 'rb'))
    else:
        if l4ng[m3ss4g3.chat.id] == "ar":
            b0t.send_message(m3ss4g3.chat.id, """
⛔ | حدث خطأ 
👁️ | يرجى التاكد من رمز الدولة
""")
        else:
            b0t.send_message(m3ss4g3.chat.id, """
⛔ | Error occurred 
👁️ | Please check the country code
""")
mFg = " Running.... /start " 
print(mFg)
b0t.polling(True)
"""
Dev : @DF_GD_D
Ch : @T62RS
In :- 2024/5/2
"""