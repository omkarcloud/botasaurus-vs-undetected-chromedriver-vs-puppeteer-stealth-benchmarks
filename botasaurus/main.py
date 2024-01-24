from botasaurus import *
from botasaurus.create_stealth_driver import create_stealth_driver

@browser()
def scrape_g2(driver: AntiDetectDriver, data):
    driver.google_get("https://www.g2.com/products/atom/reviews")
    heading = driver.text('h1')
    return heading

@browser(
    create_driver=create_stealth_driver(
        start_url="https://nowsecure.nl/",
    ),
)
def scrape_nowsecure(driver: AntiDetectDriver, data):
    heading = driver.text('h1')
    return heading


@browser(
    create_driver=create_stealth_driver(
        start_url="https://www.g2.com/products/atom/reviews?page=5",
        wait=None
    ),
)
def scrape_g2_reviews(driver: AntiDetectDriver, data):
    heading = driver.text('h1')
    return heading

scrape_g2()    
scrape_nowsecure()    
scrape_g2_reviews()    
