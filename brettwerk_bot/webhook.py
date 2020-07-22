__author__ = "Asiri Amal"
__copyright__ = "Copyright 2020, Brettwerk Discord Bot Project"
__version__ = "1.0.1"
__maintainer__ = "Rob Knight"
__email__ = "asiri.15@cse.mrt.ac.lk"
__status__ = "Production"

"""
This uses "https://www.brettwerk.com/" scrapping using beautifulsoup and uses proxies from https://sslproxies.org/
The bot will send a notification with the desired period and while the program is running only new items will be sent to
the user through given webhook URL
"""

"""
Dies verwendet das Verschrotten von "https://www.brettwerk.com/" mit beautifulsoup und verwendet Proxys von https://sslproxies.org/
Der Bot sendet eine Benachrichtigung mit dem gewünschten Zeitraum und während das Programm ausgeführt wird, werden nur neue Elemente an gesendet
der Benutzer über die angegebene Webhook-URL
"""

from bs4 import BeautifulSoup
import time
import requests

from random import choice
from discord_webhook import DiscordWebhook, DiscordEmbed

from datetime import datetime

webhook_url = "Your Discord webhook Url"
# Here is how to create a discord webhook
# https://medium.com/@asiriamalk/how-to-create-discord-webhook-and-test-using-postman-926a1f846aafwebhook_url = "https://discordapp.com/api/webhooks/729952839379582997/tVvW77hGEAo1HrKegS2mWzlOXdCiqe2994w7i762NZnHD_iZPenHlq-gAI6NXE61SCpR"
BASE_URL = target_url = "https://www.brettwerk.com/search?sSearch={:s}"


def get_soup(target_url):
    proxy = proxy_generator()
    proxies = {'http': 'https://51.161.62.120:8080'}
    proxies['http'] = f"https://{proxy['https']}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    soup = BeautifulSoup(requests.get(target_url, headers=headers, proxies=proxies).text, 'lxml')
    return soup


def get_dunk_urls(target_url, filter_tag='dunk '):
    parsed_html = get_soup(target_url)

    items = parsed_html.find_all('div', {'class': 'product--info'})
    dunk_urls = []

    for item in items:
        title = item.find('a')['title'].lower()
        if filter_tag.lower() in title:
            dunk_urls.append(item.find('a')['href'])

    return dunk_urls


def get_product_details(dunk_item):
    product_title = dunk_item.find_all('h1', {'class': "product--title"})[0].text
    product_image = dunk_item.find_all('span', {'class': "image--media"})[0].find('img')['srcset'].split(',')[0]
    product_price = dunk_item.find_all('span', {'class': "price--content content--default"})[0].find('meta')[
                        'content'] + " €"
    properties_values = dunk_item.find_all('td', {'class': "product--properties-value"})
    properties_list = [x.text for x in properties_values]

    item_details = [product_title,
                    product_image,
                    product_price,
                    properties_list]
    return item_details


def proxy_generator():
    response = requests.get("https://sslproxies.org/")
    soup = BeautifulSoup(response.content, 'html5lib')
    proxy = {'https': choice(list(map(lambda x: x[0] + ':' + x[1], list(zip(map(lambda x: x.text,
                                                                                soup.findAll('td')[::8]),
                                                                            map(lambda x: x.text,
                                                                                soup.findAll('td')[1::8]))))))}
    return proxy


def send_notification(webhook_url,
                      product_title,
                      product_image,
                      product_price,
                      properties_list,
                      product_url,
                      search_term="Dunk"):
    proxy = proxy_generator()
    proxies = {'http': 'https://51.161.62.120:8080'}
    proxies['http'] = f"https://{proxy['https']}"

    webhook = DiscordWebhook(url=webhook_url)
    webhook.set_proxies(proxies)

    # create embed object for webhook
    embed = DiscordEmbed(title=product_title, description=f"Price: {product_price}", color=242424)

    # set author
    embed.set_author(name=search_term, url=product_url, icon_url=product_image)

    # set image
    embed.set_image(url=product_image)

    # set thumbnail
    #     embed.set_thumbnail(url=product_url)

    # set footer
    embed.set_footer(text="Available 🐱‍🏍")

    # set timestamp (default is now)
    embed.set_timestamp()

    # add fields to embed
    try:
        embed.add_embed_field(name='Farbe', value=properties_list[0])
        embed.add_embed_field(name='Geschlecht', value=properties_list[1])
        embed.add_embed_field(name='Herren', value=properties_list[2])
    except:
        pass

    # add embed object to webhook
    webhook.add_embed(embed)

    print("{:s} is available now Notification sent to Discord".format(product_title))
    response = webhook.execute()


def run_app_dunk(webhook_url,
                 target_url='https://www.brettwerk.com/search?sSearch=dunk',
                 search_term="Dunk",
                 filter_tag="dunk "):
    dunk_urls = get_dunk_urls(target_url, filter_tag)

    for dunk_url in dunk_urls:
        dunk_item = get_soup(dunk_url)
        product_url = dunk_url
        product_title, product_image, product_price, properties_list = get_product_details(dunk_item)
        send_notification(webhook_url, search_term=search_term,
                          product_title=product_title,
                          product_image=product_image,
                          product_price=product_price,
                          properties_list=properties_list,
                          product_url=product_url)


def run_app_by_search(webhook_url,
                      search_term="Dunk",
                      filter_tag=" "):
    target_url = BASE_URL.format(search_term)
    dunk_urls = get_dunk_urls(target_url, filter_tag)

    for dunk_url in dunk_urls:
        dunk_item = get_soup(dunk_url)
        product_url = dunk_url
        product_title, product_image, product_price, properties_list = get_product_details(dunk_item)
        send_notification(webhook_url, search_term=search_term,
                          product_title=product_title,
                          product_image=product_image,
                          product_price=product_price,
                          properties_list=properties_list,
                          product_url=product_url)


def run_app_by_url(webhook_url,
                   target_url="https://www.brettwerk.com/detail/index/sArticle/2730/number/BV2078-002",
                   filter_tag=" "):
    search_term = "Custom URL Search"
    dunk_urls = get_dunk_urls(target_url, filter_tag)

    for dunk_url in dunk_urls:
        dunk_item = get_soup(dunk_url)
        product_url = dunk_url
        product_title, product_image, product_price, properties_list = get_product_details(dunk_item)
        send_notification(webhook_url, search_term=search_term,
                          product_title=product_title,
                          product_image=product_image,
                          product_price=product_price,
                          properties_list=properties_list,
                          product_url=product_url)


# recurrent methods

def run_app_dunk_recurrent(webhook_url,
                           target_url='https://www.brettwerk.com/search?sSearch=dunk',
                           search_term="Dunk",
                           filter_tag="dunk ",
                           sleep_seconds=60,
                           first_loop=True,
                           url_set=set(), ):
    dunk_urls = set(get_dunk_urls(target_url, filter_tag))

    # print(first_loop)
    if first_loop:
        url_set = dunk_urls.copy()
        first_loop = False
    else:
        dunk_urls = dunk_urls - set(url_set)

    for dunk_url in dunk_urls:
        dunk_item = get_soup(dunk_url)
        product_url = dunk_url
        product_title, product_image, product_price, properties_list = get_product_details(dunk_item)
        send_notification(webhook_url, search_term=search_term,
                          product_title=product_title,
                          product_image=product_image,
                          product_price=product_price,
                          properties_list=properties_list,
                          product_url=product_url)
    #     print(first_loop)
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print("Automated Bot Executed at 🐱‍🚀: ", current_time)
    time.sleep(sleep_seconds)
    return run_app_dunk_recurrent(webhook_url,
                                  target_url,
                                  search_term,
                                  filter_tag,
                                  sleep_seconds,
                                  first_loop,
                                  url_set)


def run_app_by_search_recurrent(webhook_url,
                                search_term="Dunk",
                                filter_tag=" ",
                                sleep_seconds=60,
                                first_loop=True,
                                url_set=set()):
    target_url = BASE_URL.format(search_term)
    dunk_urls = set(get_dunk_urls(target_url, filter_tag))

    print(first_loop)
    if first_loop:
        url_set = dunk_urls.copy()
        first_loop = False
    else:
        dunk_urls = dunk_urls - set(url_set)

    for dunk_url in dunk_urls:
        dunk_item = get_soup(dunk_url)
        product_url = dunk_url
        product_title, product_image, product_price, properties_list = get_product_details(dunk_item)
        send_notification(webhook_url, search_term=search_term,
                          product_title=product_title,
                          product_image=product_image,
                          product_price=product_price,
                          properties_list=properties_list,
                          product_url=product_url)

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    time.sleep(sleep_seconds)

    return run_app_by_search_recurrent(webhook_url,
                                       search_term,
                                       filter_tag,
                                       sleep_seconds,
                                       first_loop,
                                       url_set)


def run_app_by_url_recurrent(webhook_url,
                             target_url="https://www.brettwerk.com/detail/index/sArticle/2730/number/BV2078-002",
                             filter_tag=" ",
                             sleep_seconds=60,
                             first_loop=True,
                             url_set=set()):
    search_term = "Custom URL Search"
    #     target_url="https://www.brettwerk.com/detail/index/sArticle/2730/number/BV2078-002"
    dunk_urls = set(get_dunk_urls(target_url, filter_tag))

    # print(first_loop)
    if first_loop:
        url_set = dunk_urls.copy()
        first_loop = False
    else:
        dunk_urls = dunk_urls - set(url_set)

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    time.sleep(sleep_seconds)

    for dunk_url in dunk_urls:
        dunk_item = get_soup(dunk_url)
        product_url = dunk_url
        product_title, product_image, product_price, properties_list = get_product_details(dunk_item)
        send_notification(webhook_url, search_term=search_term,
                          product_title=product_title,
                          product_image=product_image,
                          product_price=product_price,
                          properties_list=properties_list,
                          product_url=product_url)

    return run_app_by_url_recurrent(webhook_url,
                                    target_url,
                                    filter_tag,
                                    sleep_seconds,
                                    first_loop,
                                    url_set)
