import yagmail
import pandas as pd
from news import NewsFeed
import datetime
import time


def nao_usar():
    # O jeito correto de enviar os endereços eletrónicos, porém não foi utilizado.
    # Para testar, apenas printei se estava tudo correto.
    email = yagmail.SMTP(user="a", password="b")
    email.send(to=row['email'],
               subject=f"Sua notícia sobre {row['interest']}",
               contents=f"Olá {row['name']}.\n As notícias sobre {row['interest']} de hoje:\n")


def send_email():
    news_feed = NewsFeed(interest=row['interest'],
                         fromdata=yesterday,
                         todata=today,
                         language='pt')
    print(f"Email enviado para {row['email']}, "
          f"com o interesse: {row['interest']}, "
          f"corpo do email:\n{news_feed.get()}")


while 1:
    if datetime.datetime.now().hour == 10 and datetime.datetime.now().minute == 17:
        yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y/%m/%d')
        today = datetime.datetime.now().strftime('%Y/%m/%d')
        df = pd.read_excel('people.xlsx')

        for index, row in df.iterrows():
            send_email()

    time.sleep(60)
