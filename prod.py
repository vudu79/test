import asyncio
import time
import sys
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
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
        html= driver.find_element(By.TAG_NAME, "html")
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


if __name__ == "__main__":
    sys.path.append("/home/andrey/python/selenium_test/")
    asyncio.run(get_product(
        "https://www.ozon.ru/product/planshet-s-klaviaturoy-wuya-podderzhka-gps-navigatsii-podhodit-dlya-igr-kino-i-749429137/?advert=LO76fZ6RQAxLfIGlFx2TK6SLdOmyvvlR_gIG8g6c7pnEi9I2EhnpuVy2QWNQDElfRo3FAyCOr3R9nBj7ca_qKqAHR1kMQWo5fabX8KYQRgSMFW72btB8pNDRVKvys8Ud5cVZ76TgnNnuybJCmxNL_4k5x6DNkkkf4St2xOGK_-g0zE25O53v8DxcTvqESnLEOGFDOqJ_cGlBxhOGN7a7cA7g-XofdZiiXocQMVjqgyV0AIGmnEOrKqn9kJda-wLh9a3kqDpYpKRYL9kCiNPcJrRLLaIBI06lAjSeCco3XdNpbNhNP0xubZ2KtMNhNkLGzyn2-vOeEPUaBE7DAn7AXrC_Q12umW-QcmtKqnH9BLq9gA2PCWj1SzwLcKA0tuaQMr4_FD1w-w1Y9ljBXts_YgyHwtWVxFa_k_0VRZIpB3JjQTpb6FJQvrTfVXc33stWehYBGzlDU0c-fwBkPTS-LAJJ0STBDbEyz22Q5CtKxBdsj4Ou_SaJdbUIAeUkjB6Jotk-dHT_ofwIfLHmT3jVrNIJkQFr7rMXBPWIlHCpGBxejDQ3-tVBWk6xS-3WOOU9AIOPE3E8oB0ldXZs7OZXoCQ-rKCwuzVKWl8_7oxcj-kfchi5GpmW7rUlBuKzvbOOWlQ-ziV6oO-t6O1g3YIiTs-TUj5ZpQpOHMqn6Yemb9c&avtc=1&avte=2&avts=1666429096&sh=h6B8Dgt9jw"))
