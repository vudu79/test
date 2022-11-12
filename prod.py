<<<<<<< HEAD
import asyncio
import time
import sys
=======
import datetime
import hashlib
import asyncio
import shutil
import time
import sys
import aiohttp
import asyncio
import requests
import json
import os
>>>>>>> dev
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
<<<<<<< HEAD
from bs4 import BeautifulSoup


async def get_page(url: str) -> str:
    useragent = UserAgent()

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    if ("iPad" in chrome_options.arguments[4]) or ("Android" in chrome_options.arguments[4]):
        chrome_options.arguments[:] = []
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        print(chrome_options.arguments[4])

    print(chrome_options.arguments)

    driver = webdriver.Chrome(executable_path="/home/andrey/python/selenium_test/chromedriver", options=chrome_options)

    try:
        driver.get(url=url)
        html = driver.find_element(By.TAG_NAME, "html")
        for i in range(2):
            html.send_keys(Keys.PAGE_DOWN)
            time.sleep(3)

        page_source = driver.page_source
        return page_source
    except Exception as ex:
        print(f'Не сработал Selenium - {ex}')
        return ""
    finally:
        driver.close()
        driver.quit()


async def get_product(url: str) -> dict:
    product = {
        "title": "",
        "curr_price": "",
        "prev_price": "",
        "image_url": "",
        "product_code": "",

    }
    page_source = await get_page(url)

    try:
        soup = BeautifulSoup(page_source, "html.parser")

        title = soup.find("h1", class_="n9v")
        curr_price = soup.find("span", class_="tn5 t5n").find("span")
        prev_price = soup.find("span", class_="n6t")
        image_url = soup.find("img", class_="m5l _24-a").get("src")
        product_code = soup.find("span", class_="v9m wm")
        description = soup.find("div", class_="ra-a1")
        product["title"] = title.text
        product["curr_price"] = curr_price.text
        product["prev_price"] = prev_price.text
        product["image_url"] = image_url
        product["product_code"] = product_code.text
        product["description"] = description.text
    except Exception as e:
        print(f'Не сработал BeautifulSoup - {e}')

    print(product)
    return product


def parse_url(url: str) -> str:
    result = ""
    list = url.split("/")

    for i in range(5):
        result = result + list[i] + "/"

    print(result)

    return result


if __name__ == "__main__":
    sys.path.append("/home/andrey/python/selenium_test/")
    url = parse_url("https://www.ozon.ru/product/planshet-s-klaviaturoy-wuya-podderzhka-gps-navigatsii-podhodit-dlya-igr-kino-i-749429137/?advert=LO76fZ6RQAxLfIGlFx2TK6SLdOmyvvlR_gIG8g6c7pnEi9I2EhnpuVy2QWNQDElfRo3FAyCOr3R9nBj7ca_qKqAHR1kMQWo5fabX8KYQRgSMFW72btB8pNDRVKvys8Ud5cVZ76TgnNnuybJCmxNL_4k5x6DNkkkf4St2xOGK_-g0zE25O53v8DxcTvqESnLEOGFDOqJ_cGlBxhOGN7a7cA7g-XofdZiiXocQMVjqgyV0AIGmnEOrKqn9kJda-wLh9a3kqDpYpKRYL9kCiNPcJrRLLaIBI06lAjSeCco3XdNpbNhNP0xubZ2KtMNhNkLGzyn2-vOeEPUaBE7DAn7AXrC_Q12umW-QcmtKqnH9BLq9gA2PCWj1SzwLcKA0tuaQMr4_FD1w-w1Y9ljBXts_YgyHwtWVxFa_k_0VRZIpB3JjQTpb6FJQvrTfVXc33stWehYBGzlDU0c-fwBkPTS-LAJJ0STBDbEyz22Q5CtKxBdsj4Ou_SaJdbUIAeUkjB6Jotk-dHT_ofwIfLHmT3jVrNIJkQFr7rMXBPWIlHCpGBxejDQ3-tVBWk6xS-3WOOU9AIOPE3E8oB0ldXZs7OZXoCQ-rKCwuzVKWl8_7oxcj-kfchi5GpmW7rUlBuKzvbOOWlQ-ziV6oO-t6O1g3YIiTs-TUj5ZpQpOHMqn6Yemb9c&avtc=1&avte=2&avts=1666429096&sh=h6B8Dgt9jw")
    asyncio.run(get_product(url))
=======

from bs4 import BeautifulSoup

#
# async def get_page(url: str) -> str:
#     useragent = UserAgent()
#
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument('--no-sandbox')
#     chrome_options.add_argument('--headless')
#     chrome_options.add_argument('--disable-gpu')
#     chrome_options.add_argument(
#         "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36")
#     chrome_options.add_argument("--disable-blink-features=AutomationControlled")
#     chrome_options.add_argument("--disable-blink-features=AutomationControlled")
#     if ("iPad" in chrome_options.arguments[4]) or ("Android" in chrome_options.arguments[4]):
#         chrome_options.arguments[:] = []
#         chrome_options = webdriver.ChromeOptions()
#         chrome_options.add_argument('--no-sandbox')
#         chrome_options.add_argument('--headless')
#         chrome_options.add_argument('--disable-gpu')
#         chrome_options.add_argument(
#             "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36")
#         chrome_options.add_argument("--disable-blink-features=AutomationControlled")
#         print(chrome_options.arguments[4])
#
#     print(chrome_options.arguments)
#
#     driver = webdriver.Chrome(executable_path="chromdrv/chromedriver", options=chrome_options)
#
#     try:
#         driver.get(url=url)
#         html= driver.find_element(By.TAG_NAME, "html")
#         for i in range(2):
#             html.send_keys(Keys.PAGE_DOWN)
#             time.sleep(3)
#
#         page_source = driver.page_source
#         return page_source
#     except Exception as ex:
#         print(f'Не сработал Selenium - {ex}')
#         return ""
#     finally:
#         driver.close()
#         driver.quit()
#
# async def get_product(url: str) -> dict:
#     product = {
#         "title": "",
#         "curr_price": "",
#         "prev_price": "",
#         "image_url": "",
#         "product_code": "",
#
#     }
#     page_source = await get_page(url)
#
#     try:
#         soup = BeautifulSoup(page_source, "html.parser")
#
#         title = soup.find("h1", class_="n9v")
#         curr_price = soup.find("span", class_="tn5 t5n").find("span")
#         prev_price = soup.find("span", class_="n6t")
#         image_url = soup.find("img", class_="m5l _24-a").get("src")
#         product_code = soup.find("span", class_="v9m wm")
#         description = soup.find("div", class_="ra-a1")
#         product["title"] = title.text
#         product["curr_price"] = curr_price.text
#         product["prev_price"] = prev_price.text
#         product["image_url"] = image_url
#         product["product_code"] = product_code.text
#         product["description"] = description.text
#     except Exception as e:
#         print(f'Не сработал BeautifulSoup - {e}')
#
#     print(product)
#     return product
#
#
# def parse_url(url: str) -> str:
#     result = ""
#     list = url.split("/")
#
#     for i in range(5):
#         result = result + list[i] + "/"
#
#     print(result)
#
#     return result


import asyncio
import uuid
import aiohttp
import async_timeout


def download_img(url, file_path):
    session = requests.Session()

    resp = session.get(url, stream=True)

    name = url.split("/")[-1]

    file_name = os.path.join(file_path, name)
    if resp.status_code == 200:
        print(f'Начал запись файла {file_name} в папку {file_path} \n')
        with open(file_name, 'wb') as f:
            for chunk in resp.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        print(f'Записал файл {file_name} в папку {file_path} \n')
        print("------------------------------------------------")


#
# loop = asyncio.get_event_loop()
# results = loop.run_until_complete(as_download(urls))
#
# print('\n'.join(results))


def main():
    domen_name = "https://pozdravik.com/"

    # res = requests.get("https://pozdravik.com/prazdniki")
    #
    # with open("page.html", "w", encoding="utf-8") as file:
    #     page = file.write(res.text)
    #
    # with open("page.html", "r", encoding="utf-8") as file:
    #     page = file.read()
    #
    # soup = BeautifulSoup(page, "html.parser")
    #
    # links = soup.find("div", class_="b-cmall__dsn_center_block1_content").find("table")
    # src = []
    # for l in links.find_all("a", href=True):
    #     src.append(f'https://pozdravik.com/{l["href"]}')
    # # print(src)
    #
    # year = {}
    #
    # for m in range(len(src)):
    #     res = requests.get(src[m])
    #
    #     name = src[m].split("/")
    #     if name[-1] == "sentjabr" or name[-1] == "oktjabr":
    #         tag = "td"
    #     else:
    #         tag = "p"
    #     soup = BeautifulSoup(res.text, "html.parser")
    #
    #     p = soup.find("div", class_="b-cmall__dsn_center_block1_content").find("table").find(tag)
    #
    #     with open("month.txt", "w", encoding="utf-8") as f:
    #         f.write(p.text)
    #     with open("month.txt", "r", encoding="utf-8") as f:
    #         titles = f.readlines()
    #
    #     if titles[0] == '\n':
    #         del titles[0]
    #         titles.append("")
    #
    #     print(titles)
    #
    #     days = {}
    #
    #     for num, link in enumerate(p.find_all("a", href=True)):
    #         days[titles[num].strip()] = f'https://pozdravik.com/{link["href"]}'
    #
    #
    #     year[words[name[-1]]] = days
    # with open('year.json', 'w', encoding='utf-8') as f:
    #     json.dump(year, f, ensure_ascii=False, indent=4)
    #

    # year = dict()
    #
    # with open('year.json', 'r', encoding='utf-8') as f:
    #     js = f.read()
    #
    # year = json.loads(js)
    # monthes = year.keys()
    #
    # for month in monthes:
    #     month_dict = {}
    #     month_ivents = year[month]
    #     month_ivents_keys = month_ivents.keys()
    #     print(f'обарбатываю месяц - {month}')
    #
    #     for ivents_key in month_ivents_keys:
    #         print(f'ищу открытки из {ivents_key}')
    #
    #         res = requests.get(month_ivents[ivents_key])
    #         soup = BeautifulSoup(res.text, "html.parser")
    #
    #         div = soup.find("div", class_="b-cmall__dsn_center_block1_content")
    #
    #         img_url_list = []
    #
    #         for img in div.find_all("img"):
    #             img_url_list.append(domen_name + img["src"])
    #
    #         key_name = ivents_key.replace("-", "").replace(" ", "_")
    #         month_dict[key_name] = img_url_list
    #
    #     print(f'записываю ссылки в файл {month}.json')
    #
    #     with open(f'{month}.json', 'w', encoding='utf-8') as f:
    #         json.dump(month_dict, f, ensure_ascii=False, indent=4)

    words = {
        "Январь": "january",
        "Февраль": "february",
        "Март": "march",
        "Апрель": "april",
        "Май": "may",
        "Июнь": "june",
        "Июль": "july",
        "Август": "august",
        "Сентябрь": "september",
        "Октябрь": "october",
        "Ноябрь": "november",
        "Декабрь": "december",
    }


    month = dict()
    base_image_dir = "images"

    with open('calendar.json', 'r', encoding='utf-8') as f:
        js = f.read()

    calendar_dict = json.loads(js)

    monthes_list = calendar_dict.keys()

    for month in monthes_list:
        month_events_list = calendar_dict[month].keys()

        for event in month_events_list:
            if not os.path.isdir(os.path.join(base_image_dir, month, event)):
                snake_event = event.replace(" ", "_").replace(".", "_")
                os.mkdir(os.path.join(os.getcwd(), base_image_dir, words[month], snake_event))

                files_path = os.path.join(os.getcwd(),base_image_dir, words[month], snake_event)

                download_img(calendar_dict[month][event], files_path)



    # words = {
    #     "janvar": "january",
    #     "fevral": "february",
    #     "mart": "march",
    #     "aprel": "april",
    #     "maj": "may",
    #     "ijun": "june",
    #     "ijul": "july",
    #     "avgust": "august",
    #     "sentjabr": "september",
    #     "oktjabr": "october",
    #     "nojabr": "november",
    #     "dekabr": "december",
    # }

    #
    # with open('calendar.json', 'r', encoding='utf-8') as f:
    #     js = f.read()
    #
    # calendar_dict = json.loads(js)
    # # print(calendar_dict)
    #
    # calendar_dict_new = {}
    #
    # month_events = {}
    #
    # for rus_month,  month in words.items():
    #     month_dict_new = {}
    #     month_events = calendar_dict[month]
    #     # print(month_events)
    #     for key in month_events.keys():
    #         new_key = get_new_key(key)
    #         month_dict_new[new_key] = month_events[key]
    #         # print(month_dict_new)
    #
    #     calendar_dict_new[rus_month] = month_dict_new
    #
    #
    # with open('calendar_new.json', 'w', encoding='utf-8') as f:
    #     json.dump(calendar_dict_new, f, ensure_ascii=False, indent=4)
    #
    # # print(calendar_dict_new)


#
# def get_new_key(key):
#     month_tuple = (
#         "января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября",
#         "декабря")
#     new_key = ""
#     key_list = key.split("__")
#     date_path = key_list[0].split("_")
#
#     if len(date_path) > 1:
#         if date_path[1] in month_tuple:
#
#             match date_path[1]:
#
#                 case "января":
#                     new_key = date_path[0] + ".01" + " - " + key_list[1].replace("_", " ")
#                 case "февраля":
#                     new_key = date_path[0] + ".02" + " - " + key_list[1].replace("_", " ")
#                 case "марта":
#                     new_key = date_path[0] + ".03" + " - " + key_list[1].replace("_", " ")
#                 case "апреля":
#                     new_key = date_path[0] + ".04" + " - " + key_list[1].replace("_", " ")
#                 case "мая":
#                     new_key = date_path[0] + ".05" + " - " + key_list[1].replace("_", " ")
#                 case "июня":
#                     new_key = date_path[0] + ".06" + " - " + key_list[1].replace("_", " ")
#                 case "июля":
#                     new_key = date_path[0] + ".07" + " - " + key_list[1].replace("_", " ")
#                 case "августа":
#                     new_key = date_path[0] + ".08" + " - " + key_list[1].replace("_", " ")
#                 case "сентября":
#                     new_key = date_path[0] + ".09" + " - " + key_list[1].replace("_", " ")
#                 case "октября":
#                     new_key = date_path[0] + ".10" + " - " + key_list[1].replace("_", " ")
#                 case "ноября":
#                     new_key = date_path[0] + ".11" + " - " + key_list[1].replace("_", " ")
#                 case "декабря":
#                     new_key = date_path[0] + ".12" + " - " + key_list[1].replace("_", " ")
#     return new_key

if __name__ == "__main__":
    main()
# print(len('3.01 - День Рождения Русской Матрёшки'.encode('utf-8')))
# # url = parse_url("https://www.ozon.ru/product/planshet-s-klaviaturoy-wuya-podderzhka-gps-navigatsii-podhodit-dlya-igr-kino-i-749429137/?advert=LO76fZ6RQAxLfIGlFx2TK6SLdOmyvvlR_gIG8g6c7pnEi9I2EhnpuVy2QWNQDElfRo3FAyCOr3R9nBj7ca_qKqAHR1kMQWo5fabX8KYQRgSMFW72btB8pNDRVKvys8Ud5cVZ76TgnNnuybJCmxNL_4k5x6DNkkkf4St2xOGK_-g0zE25O53v8DxcTvqESnLEOGFDOqJ_cGlBxhOGN7a7cA7g-XofdZiiXocQMVjqgyV0AIGmnEOrKqn9kJda-wLh9a3kqDpYpKRYL9kCiNPcJrRLLaIBI06lAjSeCco3XdNpbNhNP0xubZ2KtMNhNkLGzyn2-vOeEPUaBE7DAn7AXrC_Q12umW-QcmtKqnH9BLq9gA2PCWj1SzwLcKA0tuaQMr4_FD1w-w1Y9ljBXts_YgyHwtWVxFa_k_0VRZIpB3JjQTpb6FJQvrTfVXc33stWehYBGzlDU0c-fwBkPTS-LAJJ0STBDbEyz22Q5CtKxBdsj4Ou_SaJdbUIAeUkjB6Jotk-dHT_ofwIfLHmT3jVrNIJkQFr7rMXBPWIlHCpGBxejDQ3-tVBWk6xS-3WOOU9AIOPE3E8oB0ldXZs7OZXoCQ-rKCwuzVKWl8_7oxcj-kfchi5GpmW7rUlBuKzvbOOWlQ-ziV6oO-t6O1g3YIiTs-TUj5ZpQpOHMqn6Yemb9c&avtc=1&avte=2&avts=1666429096&sh=h6B8Dgt9jw")
# # asyncio.run(get_product(url))
# s = str(hash('3.фвфвфвфцвфцвфцвфвыдлатфжылджафыажфдатщутшажфкт01 - День Рождения Русской Матрёшки'))
# print(len(s.encode('utf-8')))

# print(datetime.datetime.today().strftime("%-d.%m"))
>>>>>>> dev
