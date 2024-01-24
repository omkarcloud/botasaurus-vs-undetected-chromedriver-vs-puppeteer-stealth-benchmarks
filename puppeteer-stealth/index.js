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
