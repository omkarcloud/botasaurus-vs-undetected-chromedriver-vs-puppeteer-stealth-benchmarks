import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from time import sleep

def scrape_g2():
    options = uc.ChromeOptions()
    driver = uc.Chrome(options=options, version_main=120) # Replace with your Chrome Version
    driver.get("https://www.google.com/")
    driver.execute_script(f"""
                window.location.href = "https://www.g2.com/products/atom/reviews";
            """)
    sleep(5)
    heading = driver.find_element(By.CSS_SELECTOR, 'h1').text
    
    driver.quit()

    return heading

def scrape_nowsecure():
    options = uc.ChromeOptions()
    driver = uc.Chrome(options=options, version_main=120)
    driver.get("https://www.google.com/")
    driver.execute_script(f"""
                window.location.href = "https://nowsecure.nl/";
            """)
    sleep(5)
    heading = driver.find_element(By.CSS_SELECTOR, 'h1').text
    
    driver.quit()

    return heading

def scrape_g2_reviews():
    options = uc.ChromeOptions()
    driver = uc.Chrome(options=options, version_main=120)
    driver.get("https://www.google.com/")
    driver.execute_script(f"""
                window.location.href = "https://www.g2.com/products/atom/reviews?page=5";
            """)
    sleep(5)
    heading = driver.find_element(By.CSS_SELECTOR, 'h1').text
    
    driver.quit()

    return heading


if __name__== "__main__":
    print(scrape_g2())
    print(scrape_nowsecure())
    print(scrape_g2_reviews())
