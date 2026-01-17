from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Function to scrape crypto prices
def parse_data():
    try:
        # Setup Chrome options
        chrome_options = Options()
        # chrome_options.add_argument("--headless")  # Uncomment for headless mode

        # Create WebDriver instance
        driver = webdriver.Chrome(options=chrome_options)

        # Open Binance page and wait for the element
        driver.get('https://www.binance.com/en')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#top_crypto_table-1-BTC_USDT > div:nth-child(2) > div')))
        crypto_binance = driver.find_element(By.CSS_SELECTOR, '#top_crypto_table-1-BTC_USDT > div:nth-child(2) > div').text
        
        # Open Capital page and wait for the element
        driver.get('https://capital.com/lp-trade-ga-bah?utm_medium=cpc&utm_source=google&utm_campaign=web_bah_search_google_asia-t2_en_troas_ftd_ua&utm_term=trading%20market&adgroupid=178874722965&matchtype=p&creative=756209432843&device=c&loc_physical=9070053&gad_source=1&gad_campaignid=22634253029&gbraid=0AAAAADQE_stGU9YV5XCCC7IgD3ZQOIwcZ&gclid=EAIaIQobChMI_eKNi-3nkAMVk2xBAh12jjCgEAAYASAAEgIGw_D_BwE')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'body > div.wrap.grid.gXl.lpWrap > section:nth-child(4) > div > table > tbody > tr:nth-child(3) > td.sell.textRight > a')))
        crypto_okx = driver.find_element(By.CSS_SELECTOR, 'body > div.wrap.grid.gXl.lpWrap > section:nth-child(4) > div > table > tbody > tr:nth-child(3) > td.sell.textRight > a').text

        # Open Bybit page and wait for the element
        driver.get('https://www.bybit.com/en/')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#landing-page-container > section:nth-child(2) > div > div > div.Market_market-wrapper__sWABf > div.Market_left-box__Bb_gh > div > div.Section_content__vRLFD > div.Market_show__mbuU9 > div > div.SectionList_tbody__PocYe > ul > li:nth-child(1) > a > span')))

        crypto_bybit = driver.find_element(By.CSS_SELECTOR, '#landing-page-container > section:nth-child(2) > div > div > div.Market_market-wrapper__sWABf > div.Market_left-box__Bb_gh > div > div.Section_content__vRLFD > div.Market_show__mbuU9 > div > div.SectionList_tbody__PocYe > ul > li:nth-child(1) > a > span').text

        # Return the list of scraped values
        return [crypto_binance, crypto_bybit, crypto_okx]
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        driver.quit()  # Ensure the driver is closed even if an error occurs
