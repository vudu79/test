import time
import sys
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.common.by import By


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

driver = webdriver.Chrome(executable_path="chromdrv/chromedriver", options=chrome_options)

url = "https://www.ozon.ru/product/ekshn-kamera-gopro-hero11-black-725415003/?advert=pQJnG6AZS5IeCyqDxnQIQB_doXOgvQzHGIlUj54Jc3TyeIaJTmnC-VW3mHvdXQBlpHrSutYmqGs45-EBFWH3C9LYKsGhWnaONMxp6mMZh3IvFkr14zW8EyRu72JkcVrxPpPbDa35o8LWZ9zOvdmm87RfaaSl6Iq5xZyQqbkzGhX6vspnpzO_9v0ZofuZ0_29afB3qF7FpmMoMqzCIEYR4H_Jp6dTpygMmnYXjS4VcN_Fs61y9dmORln576Hg6uerLY_Lf-C9A12LaTkhjEJOu3FdDVDl81LxqW28vB2J6FGGhi3NlSPSCwwWnZX_sRydj4cqR_yh4echVNxTYEEqF2BNRdVGaoYmSgYoxGtDGc7XUgJO9ph6jxETzVXei9orcvZp_zby5G2PsFdcfndwIDT-RnEDyYEpW6oTpuxZNIchJmKYAjsedyZnt3iAL04j2ol8KsTrmezHZnSkI08dOnXdzS57oZuUzX8wTeNnxrj4Pc2CG9_RKLnhchi15jEbCEy90CZBSx85rIqN4_DOdh92yes_p_X5EX7dv3MvD-jpkyr2dFTqgU7Bkp_5qff7Hjh_o8KDCaOWvqpPRiGhwod6zzcG6Ko0OJp_EoUAvAZTZmcROX7ViISEsR9EvrVUxCzS7HHviRTqUkJcLYV8-KgO1HezJLoDpU-8iG2bb9Y&avtc=1&avte=2&avts=1666419967&sh=h6B8DuOlnQ"

def main():
    try:
        pass
        driver.get(url=url)
        time.sleep(20)

        title = driver.find_element(By.CLASS_NAME, "n9v")
        print(title.text)
        # div_price = driver.find_element(By.XPATH, '//*[@id="layoutPage"]/div[1]/div[3]/div[3]/div[2]/div[2]/div/div/div/div[1]/div')
        current_price = driver.find_element(By.XPATH, '//*[@id="layoutPage"]/div[1]/div[3]/div[3]/div[2]/div[2]/div/div/div/div[1]/div/div/div/div/span[1]/span')

        prev_price = driver.find_element(By.XPATH, '//*[@id="layoutPage"]/div[1]/div[3]/div[3]/div[2]/div[2]/div/div/div/div[1]/div/div/div/div/span[2]')

        image = driver.find_element(By.XPATH, '//*[@id="layoutPage"]/div[1]/div[3]/div[3]/div[1]/div/div[2]').find_elements(By.TAG_NAME, "img")

        print(current_price.text)
        print(prev_price.text)
        print(image)

        #
        # driver.get_screenshot_as_file("1.png")
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == "__main__":
    main()

# url = "https://www.ozon.ru/api/composer-api.bx/page/json/v2?url=/product/stiralnaya-mashina-atlant-sma-60s1010-00-belyy-257776483"
#
# headers = {
#     "authority": "www.ozon.ru",
#     "path": "/api/composer-api.bx/page/json/v2?url=/product/stiralnaya-mashina-atlant-sma-60s1010-00-belyy-257776483",
#     "scheme": "https",
#     "cache-control": "max-age=0",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
#     "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#     "accept-encoding": "gzip, deflate, br",
#     "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
#     'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": "Windows",
#     "sec-fetch-dest": "document",
#     "sec-fetch-mode": "navigate",
#     "sec-fetch-site": "none",
#     "sec-fetch-user": "?1",
#     "upgrade-insecure-requests": "1",
#
# }
#
