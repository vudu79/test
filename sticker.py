import datetime
import json
import logging

from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup


# сайт "https://chpic.su" ------------------------------------------------
# def main():
#     domen = "https://chpic.su"
#     pack_info_dict = dict()
#     results = list()
#     stickers_list = list()
#     ua = UserAgent()
#     headers = {
#         "user-agent": ua.random
#     }
#
#     print(headers["user-agent"])
#     for x in range(0, 342):
#         uri = f"/ru/stickers/?sortby=date&page={x}"
#         print(uri + " " + str(datetime.datetime.now()))
#         try:
#             res = requests.get(domen + uri, headers=headers)
#             if res.status_code == 200:
#                 logging.info(f'Рабатаю со страницей - {x}')
#                 soup = BeautifulSoup(res.text, "lxml")
#                 divs = soup.find_all("div", class_="collections_list_item clickable_area")
#
#
#                 for div in divs:
#                     pack_info_dict["name"] = div.find("div", class_="title").find("a").text
#                     pack_url = domen + div.find("div", class_="title").find("a").get("href")
#                     pack_info_dict["count"] = div.find("div", class_="subtitle").text
#                     pack_info_dict["date"] = div.find("div", class_="datetime").find("span", class_="t").text
#                     try:
#                         pack_res = requests.get(pack_url, headers=headers)
#                         if pack_res.status_code == 200:
#
#                             pack_soup = BeautifulSoup(pack_res.text, "lxml")
#                             pack_divs = pack_soup.find_all("div", class_="stickers_list_item")
#                             pack_info_dict["url"] = pack_soup.find("div", class_="collection_info").find("div",
#                                                                                                          class_="install").find(
#                                 "a").get("href")
#                             for pack_div in pack_divs:
#                                 stickers_list.append(domen + pack_div.find("a").find("img").get("src"))
#
#                             buffer_list = stickers_list.copy()
#
#                             pack_info_dict["stickers"] = buffer_list
#
#                             stickers_list.clear()
#
#                             results.append(pack_info_dict)
#                             print(pack_info_dict)
#
#                     except Exception as eee:
#                         logging.error(f"Проблеммы с requests внутри пака -  {eee}")
#         except Exception as e:
#             logging.error(f"Проблеммы с requests на странице с паками - {e}")
#
#     try:
#         with open("stickers.json", "w", encoding="utf-8") as f:
#             json.dump(results, f, indent=4)
#     except Exception as ee:
#         logging.error(f"Проблеммы с записью в файл - {ee}")
#
#
# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO, filename="stickers_log.log", filemode="w",
#                         format="%(asctime)s %(levelname)s %(message)s")
#     main()
# ---------------------------------------------------------------------------

# сайт https://combot.org/telegram/stickers
def main():
    domen = "https://combot.org"
    pack_info_dict = dict()
    results = list()
    stickers_list = list()
    ua = UserAgent()
    headers = {
        "user-agent": ua.chrome
    }

    print(headers["user-agent"])
    for x in range(1, 2):
        uri = f"/telegram/stickers?page={x}"
        print(domen + uri + " " + str(datetime.datetime.now()))
        try:
            res = requests.get(domen + uri, headers=headers)
            if res.status_code == 200:
                soup = BeautifulSoup(res.text, "lxml")
                divs = soup.find_all("div", class_="sticker-pack sticker-packs-list__item")
                # print(len(divs))
                for div in divs:
                    img_divs = div.find_all("div", class_="sticker-pack__sticker-img")
                    pack_info_dict["name"] = div.find("div", class_="sticker-pack__title").text
                    pack_info_dict["url"] = div.find("a", class_="sticker-pack__btn").get("href")
                    pack_info_dict["count"] = str(len(img_divs))
                    pack_info_dict["date"] = None

                    for img in img_divs:
                        stickers_list.append(img.get("data-src"))

                    buffer_list = stickers_list.copy()
                    pack_info_dict["stickers"] = buffer_list
                    stickers_list.clear()
                    print(f'page = {x} --- title = {pack_info_dict["name"]} ---{len(results)}')
                    results.append(pack_info_dict)

        except Exception as eee:
            logging.error(f"Проблеммы с requests  -  {eee}")

    print(results)

    # try:
    #     with open("stickers_combot.json", "w", encoding="utf-8") as f:
    #         json.dump(results, f, indent=4)
    # except Exception as ee:
    #     logging.error(f"Проблеммы с записью в файл - {ee}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filename="stickers_log.log", filemode="w",
                        format="%(asctime)s %(levelname)s %(message)s")
    main()
