
import requests
import json
import os


def download_img(url, file_path):
    try:
        session = requests.Session()

        resp = session.get(url, stream=True)

        name = url.split("/")[-1]

        file_name = os.path.join(file_path, name)
        print(resp.status_code)
        if resp.status_code == 200:
            print(f'Начал запись файла {file_name} в папку {file_path} \n')
            with open(file_name, 'wb') as f:
                for chunk in resp.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
            print(f'Записал файл {file_name} в папку {file_path} \n')
            print("------------------------------------------------")
    except Exception as e:
        print(f'Сработало исключение {e}')



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

    monthes_list = calendar_dict.keys()

    for month in monthes_list:
        month_events_list = calendar_dict[month].keys()

        for event in month_events_list:
            if not os.path.isdir(os.path.join(base_image_dir, month, event)):
                snake_event = event.replace(" ", "_").replace(".", "_")
                os.makedirs(os.path.join(os.getcwd(), base_image_dir, words[month], snake_event))

                files_path = os.path.join(os.getcwd(),base_image_dir, words[month], snake_event)
                for url in calendar_dict[month][event]:
                    download_img(url, files_path)




if __name__ == "__main__":
    main()
