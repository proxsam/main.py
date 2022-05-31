import requests
from bs4 import BeautifulSoup
import lxml
import smtplib


URL = "https://www.amazon.in/New-Apple-iPhone-12-64GB/dp/B08L5VJYV7/ref=sr_1_6?crid=1IFCUW1AFYGGH&keywords=iphone+12" \
      "&qid=1642886923&sprefix=iphone+12%2Caps%2C234&sr=8-6 "

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/97.0.4692.99 Safari/537.36/8mqQhSuL-09 ",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.9 ",
    "Request Line": "GET / HTTP/1.1",

}

my_email = "thes14808@gmail.com"
senders_email = "samarthgaba27@gmail.com"
password = "@Sam1010g"


response = requests.get(url=URL, headers=headers)
amazon_page = response.text
soup = BeautifulSoup(amazon_page, "lxml")
element = soup.select("span .a-offscreen")
price = int(element[0].text.strip("₹,.00").replace(",", ""))
title = soup.select("#productTitle")[0].text.strip("         ")

data = f"Your {title} is now for Rs {price}"
if price < 50000:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=senders_email,
            msg=f"Subject:Price Alert\n\n {data}\n{URL}")