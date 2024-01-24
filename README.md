# Botasaurus vs. Undetected-Chromedriver vs. Puppeteer-Stealth Benchmarks

In the rapidly evolving world of web scraping and bot automation, staying ahead of detection technologies is crucial. This document aims to compare the stealth features of three popular open-source libraries, each renowned for their ability to circumvent bot detection mechanisms:

1. **Botasaurus**: A complete web scraping framework developed by the Omkar team.
2. **Undetected-Chromedriver**: An awesome and strongly undetected Python library created by [Leon](https://github.com/ultrafunkamsterdam).
3. **Puppeteer-Stealth**: An amazing JavaScript library with stealth, blocking, and captcha-solving capabilities, developed by [berstend](https://github.com/berstend).

As of this writing, Cloudflare is the top choice for websites seeking bot detection solutions. Therefore, our tests focus on Cloudflare-protected websites, specifically:
- [g2.com](https://www.g2.com/products/atom/reviews)
- [nowsecure.nl](https://nowsecure.nl/)
- [g2.com reviews page](https://www.g2.com/products/atom/reviews?page=5)

## Test Environment
- **Hardware**: Standard Windows PC
- **Network**: Clean IP for each test
- **Benchmark Sites**: Cloudflare-protected websites

## Testing Methodology
The libraries were tested on their ability to access and interact with the selected websites. The key areas of focus were JavaScript challenge handling and CAPTCHA bypass capabilities.

## Code Snippets
Below are the code snippets used for each library:

### Botasaurus Code
```python
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
```

### Undetected-Chromedriver Code
```python
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
```

### Puppeteer-Stealth Code
```js
const puppeteer = require('puppeteer-extra');
const StealthPlugin = require('puppeteer-extra-plugin-stealth');
puppeteer.use(StealthPlugin());

async function scrapeG2() {
    const browser = await puppeteer.launch({ headless: false });
    const page = await browser.newPage();
    await page.goto('https://www.g2.com/products/atom/reviews', {'referer': 'https://www.google.com/'});
    await page.waitForTimeout(5000); // Wait for 5 seconds
    const heading = await page.$eval('h1', el => el.textContent);
    await browser.close();
    return heading;
}

async function scrapeNowsecure() {
    const browser = await puppeteer.launch({ headless: false });
    const page = await browser.newPage();
    await page.goto('https://nowsecure.nl/', {'referer': 'https://www.google.com/'});
    await page.waitForTimeout(5000);
    const heading = await page.$eval('h1', el => el.textContent);
    await browser.close();
    return heading;
}

async function scrapeG2Reviews() {
    const browser = await puppeteer.launch({ headless: false });
    const page = await browser.newPage();
    await page.goto('https://www.g2.com/products/atom/reviews?page=5',{'referer': 'https://www.google.com/'});
    await page.waitForTimeout(5000);
    const heading = await page.$eval('h1', el => el.textContent);
    await browser.close();
    return heading;
}

(async () => {
    console.log(await scrapeG2());
    console.log(await scrapeNowsecure());
    console.log(await scrapeG2Reviews());
})();
```

## Test Results
All three libraries successfully accessed g2.com. However, Botasaurus stood out by being the only framework capable of accessing both nowsecure.nl and the g2.com reviews page. This demonstrates Botasaurus's ability to handle both JavaScript and CAPTCHA challenges presented by Cloudflare.

## Conclusion
Based on our benchmarks, Botasaurus is the recommended choice for accessing websites with robust bot protection measures. Its performance in circumventing Cloudflare's defenses is particularly noteworthy.

## Further Exploration
For those interested in conducting their own tests, the code and dependencies are available in this repository itself. We believe in transparency and encourage feedback and discussion. Share your thoughts and experiences on our dedicated discussion page [here](https://github.com/omkarcloud/botasaurus/discussions/43), and contribute to the community's collective knowledge.