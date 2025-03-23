import undetected_chromedriver as uc
import time
import os

home_dir = os.path.expanduser('~/')
profile_dir = home_dir + "/profileSample"
profile_image_dir = home_dir + "/profileSampleImages"
domain = "https://book-ye.com.ua"

def cloudflare_passing(arg_profile):
    options = uc.ChromeOptions()
    options.add_argument(arg_profile)
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    prefs = {
        "plugins.always_open_pdf_externally": True
    }
    options.add_argument("--disable-features=WebPImageHint")
    options.add_argument("--disable-webp-conversion")
    options.add_argument("--force-device-scale-factor=1")
    options.add_experimental_option("prefs", prefs)
    driver = uc.Chrome(options=options)
    driver.get(domain)
    time.sleep(35)
    driver.close()

def no_image_driver():
    arg_profile = "--user-data-dir=" + profile_dir
    # it's reasonable to call the cloudflare_passing just once when a profile doesn't exist yet
    cloudflare_passing(arg_profile)
    options = uc.ChromeOptions()
    options.add_argument(arg_profile)
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    prefs = {
        "download.prompt_for_download": False,  # Skip the download prompt
        "download.directory_upgrade": True,  # Allow directory change
        "safebrowsing.enabled": True,  # Disable safe browsing warning for downloads
        "plugins.always_open_pdf_externally": True
    }
    options.add_argument("--blink-settings=imagesEnabled=false")
    options.add_argument("--disable-features=WebPImageHint")
    options.add_argument("--disable-webp-conversion")
    options.add_argument("--force-device-scale-factor=1")
    options.add_experimental_option("prefs", prefs)
    driver = uc.Chrome(options=options)
    driver.set_page_load_timeout(30)
    return driver

def image_driver():
    arg_profile = "--user-data-dir=" + profile_image_dir
    # must be called to keep the cloudflare passing in profile_image_dir
    # it's reasonable to call the cloudflare_passing just once when a profile doesn't exist yet
    # cloudflare_passing(arg_profile)
    options = uc.ChromeOptions()
    options.add_argument(arg_profile)
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    prefs = {
        "download.default_directory": "/home/sdk/Downloads",
        "download.prompt_for_download": False,  # Skip the download prompt
        "download.directory_upgrade": True,  # Allow directory change
        "safebrowsing.enabled": True,  # Disable safe browsing warning for downloads
        "plugins.always_open_pdf_externally": True
    }
    options.add_argument("--disable-features=WebPImageHint")
    options.add_argument("--disable-webp-conversion")
    options.add_argument("--force-device-scale-factor=1")
    options.add_experimental_option("prefs", prefs)
    driver = uc.Chrome(options=options)
    return driver


def scraping_in_action():
    driver = no_image_driver()
    url = domain + "/catalog/nekhudozhnya-literatura-inozemnymy-movamy/thinking-fast-and-slow"
    driver.get(url)
    driver.implicitly_wait(5)
    html_content = driver.page_source
    print(html_content)
    driver.quit()
    print('finished')

scraping_in_action()
