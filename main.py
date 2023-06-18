import schedule
import time
from scrapy import get_html_soup, get_next_shows_info
from what_zap import send_whatzap

url = "https://casanaturamusical.com.br/"
concert_hall = "Casa Natura"

remetents = ["whatsapp:+553188469230", "whatsapp:+5511933621832"]


def send_shows_info():
    shows_info = get_next_shows_info(get_html_soup(url))

    message = f"Próximos show na {concert_hall}\n\n"
    for info in shows_info:
        message += f"{info['artist']} {info['date']}\nlink: {info['link']}\n\n"

    send_whatzap(remetents, message)


def main():
    schedule.every(15).days.do(send_shows_info)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
