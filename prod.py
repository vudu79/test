import datetime
import time
import psutil
import requests
import json
import os
import logging


# def download_img(url, file_path):
#     try:
#         begin = time.time()
#         session = requests.Session()
#
#         resp = session.get(url, stream=True)
#
#         name = url.split("/")[-1]
#
#         file_name = os.path.join(file_path, name)
#         print(resp.status_code)
#         if resp.status_code == 200:
#             print(f'Начал запись файла {file_name}. Ответ сервера {resp.status_code}')
#             logging.info(f'Начал запись файла {file_name}. Ответ сервера {resp.status_code}')
#             with open(file_name, 'wb') as f:
#                 for chunk in resp.iter_content(chunk_size=1024):
#                     if chunk:
#                         f.write(chunk)
#             proc_time = time.time() - begin
#             file_stats = os.stat(file_name)
#             logging.info(
#                 f'Записал файл {file_name} за {proc_time:.3f} сек. Размер файла -  {file_stats.st_size / 1024:.2f} kb.')
#             logging.info(f'Осталось места на диске {psutil.disk_usage("/")[2] / (1024 * 1024):.3f} Mb.')
#             logging.info(f'Общее время загрузки - {datetime.datetime.now() - total_begin_time} сек')
#             print("------------------------------------------------")
#
#     except Exception as e:
#         print(f'Сработало исключение {e}')
#         logging.error(f'сработало исключение - {e}')


def main():
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

    base_image_dir = "images"

    with open('calendar.json', 'r', encoding='utf-8') as f:
        js = f.read()

    calendar_dict = json.loads(js)
    months_list = calendar_dict.keys()

    calendar_storage_dict = dict()
    month_storage_dict = dict()
    events_storage_list = list()

    for month in months_list:
        month_events_list = calendar_dict[month].keys()

        for event in month_events_list:
            event_storage = event.replace(" ", "_").replace(".", "=")
            for img_url in calendar_dict[month][event]:
                file_name = img_url.split("/")[4]
                events_storage_list.append(str(os.path.join(base_image_dir, words[month], event_storage, file_name)))
            bufer_list = events_storage_list.copy()
            month_storage_dict[event_storage] = bufer_list
            events_storage_list.clear()


        calendar_storage_dict[month] = month_storage_dict

    with open("calendar_storage.json", "w", encoding='utf-8') as file:
        json.dump(calendar_storage_dict, file, indent=4, ensure_ascii=False)

    print(calendar_storage_dict)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w",
                        format="%(asctime)s %(levelname)s %(message)s")
    main()
