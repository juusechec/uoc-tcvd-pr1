import requests
import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# First we want to check the robots.txt file of our objective website
# A function get_robot_txt is constructed to check any url


def get_robot_txt(url):
    if url.endswith('/'):
        path = url
    else:
        path = url + '/'
    req = requests.get(path + "robots.txt", data=None)
    return req.text


# Objective website
URL = "https://www.mercadolibre.com.co"

# Read robots.txt file
print('robots.txt:', get_robot_txt(URL))

sites = [
    {
        'country': 'Argentina',
        'url': 'https://listado.mercadolibre.com.ar'
    },
    {
        'country': 'Bolivia',
        'url': 'https://listado.mercadolibre.com.bo'
    },
    {
        'country': 'Brasil',
        'url': 'https://lista.mercadolivre.com.br'
    },
    {
        'country': 'Chile',
        'url': 'https://listado.mercadolibre.cl'
    },
    {
        'country': 'Colombia',
        'url': 'https://listado.mercadolibre.com.co'
    },
    {
        'country': 'Costa Rica',
        'url': 'https://listado.mercadolibre.co.cr'
    },
    {
        'country': 'Dominicana',
        'url': 'https://listado.mercadolibre.com.do'
    },
    {
        'country': 'Ecuador',
        'url': 'https://listado.mercadolibre.com.ec'
    },
    {
        'country': 'Guatemala',
        'url': 'https://listado.mercadolibre.com.gt'
    },
    {
        'country': 'Honduras',
        'url': 'https://listado.mercadolibre.com.hn'
    },
    {
        'country': 'México',
        'url': 'https://listado.mercadolibre.com.mx'
    },
    {
        'country': 'Nicaragua',
        'url': 'https://listado.mercadolibre.com.ni'
    },
    {
        'country': 'Panamá',
        'url': 'https://listado.mercadolibre.com.pa'
    },
    {
        'country': 'Paraguay',
        'url': 'https://listado.mercadolibre.com.py'
    },
    {
        'country': 'Perú',
        'url': 'https://listado.mercadolibre.com.pe'
    },
    {
        'country': 'El Salvador',
        'url': 'https://listado.mercadolibre.com.sv'
    },
    {
        'country': 'Uruguay',
        'url': 'https://listado.mercadolibre.com.uy'
    },
    {
        'country': 'Venezuela',
        'url': 'https://listado.mercadolibre.com.ve'
    },
]

products = [
    {
      'name': 'playstation',
      'uri': 'playstation-5#D[A:playstation%205]',
    },
    {
      'name': 'macbook pro',
      'uri': 'macbook-pro-13#D[A:macbook%20pro%2013]',
    },
    {
      'name': 'iphone',
      'uri': 'iphone-11-512#D[A:iphone%2011%20512]',
    },
    {
      'name': 'bmw s1000rr',
      'uri': 'bmw-s1000rr#D[A:bmw%20s1000rr]',
    },
    {
      'name': 'alexa echo',
      'uri': 'alexa-echo-4#D[A:alexa%20echo%204]',
    },
]

# Setting options for the webdriver
option = webdriver.ChromeOptions()
option.add_argument(" — incognito")  # open incognito mode
# set our UserAgent name, in this case AcademicCrawler
option.add_argument("user-agent=AcademicCrawler")

# Getting current folder path
#My_path = os.path.dirname(os.path.abspath(__file__))

# Delay/Pause of download Throttling
TimeOut = 2  # sec

# Looking for the chromedriver file (Download from http://chromedriver.chromium.org/downloads)
#browser = webdriver.Chrome(executable_path=My_path + '/chromedriver', chrome_options=option)
browser = webdriver.Chrome(ChromeDriverManager().install(), options=option)

# Check if our UseraAgent is OK
agent = browser.execute_script("return navigator.userAgent")
print('agent:', agent)


def get_items_names():
    elements = browser.find_elements_by_css_selector(
        '#root-app > div > div > section > ol > li > div > div > div.ui-search-result__content-wrapper > div.ui-search-item__group.ui-search-item__group--title > a > h2')

    if len(elements) == 0:
        print('Caso 2')
        elements = browser.find_elements_by_css_selector(
            '#root-app > div > div.ui-search-main.ui-search-main--exhibitor.ui-search-main--only-products > section > ol > li > div > div > a > div > div.ui-search-item__group.ui-search-item__group--title > h2')

    if len(elements) == 0:
        print('Caso 3')
        elements = browser.find_elements_by_css_selector(
            '#root-app > div > div > section > ol > li > div > div > a > div > div.ui-search-item__group.ui-search-item__group--title > h2')

    return elements


def get_items_prices():
    prices = browser.find_elements_by_css_selector(
        '.ui-search-price:not(.ui-search-price--size-x-tiny) .ui-search-price__second-line')
    return prices


filename = "MercadoLibreData.csv"
current_path = os.path.dirname(os.path.abspath(__file__))
# print('current_path:', current_path)


def write_file(text):
    filename_path = current_path + '/' + filename
    with open(filename_path, 'a') as file:
        file.write(text)
        file.close()


try:
    write_file('product,country,url,item,precio\n')
    for product in products:
        for site in sites:
            print('looking:', site['country'], ', product:', product['name'])

            write_file(product['name'] + ',')

            write_file(site['country'] + ',')

            # Get content from objective website
            url = site['url'] + '/' + product['uri']
            browser.get(url)

            write_file(url + ',')

            # Apply delay
            browser.implicitly_wait(TimeOut)

            items_names = get_items_names()

            items_prices = get_items_prices()

            if len(items_prices) > 0:
                item_name = items_names[0].text
                print('item_name:', item_name)
                write_file(item_name + ',')

                item_price = items_prices[0].text.split("\n")[0]
                print('item_price:', item_price)
                write_file(item_price + '\n')
            else:
                write_file(',\n')

except Exception as e:
    print(e)
finally:
    browser.quit()


# # Search all the urls for the top 50 streamers
# elements = browser.find_elements_by_xpath(
#     """//*[@id="tblControl"]/tbody/tr/td[1]/a""")
# links = []
# for element in elements:
#     links.append(element.get_attribute("href"))

# # Navigate through the links
# dictlist = []
# for link in links:
#     browser.get(link)
#     browser.implicitly_wait(TimeOut)
#     userStatsDict = {}

#     # Data for Scraping
#     followers = browser.find_elements_by_css_selector(
#         "body > div.RightContent > div.MainContent > div.PageContentContainer > div.StandardPageContainer > div > div:nth-child(1) > div:nth-child(1) > div > div.PageBackgroundColor.InfoPanelMiddle > div:nth-child(3) > div.InfoPanelRowRight.BoldText")
#     streams = browser.find_elements_by_css_selector(
#         "body > div.RightContent > div.MainContent > div.PageContentContainer > div.StandardPageContainer > div > div:nth-child(1) > div:nth-child(1) > div > div.PageBackgroundColor.InfoPanelMiddle > div:nth-child(5) > div.InfoPanelRowRight.BoldText > span:nth-child(1)")
#     averageViews = browser.find_elements_by_css_selector(
#         "body > div.RightContent > div.MainContent > div.PageContentContainer > div.StandardPageContainer > div > div:nth-child(1) > div:nth-child(2) > div > div.PageBackgroundColor.InfoPanelMiddle > div:nth-child(1) > div.InfoPanelRowRight.BoldText")
#     watchTime = browser.find_elements_by_css_selector(
#         "body > div.RightContent > div.MainContent > div.PageContentContainer > div.StandardPageContainer > div > div:nth-child(1) > div:nth-child(2) > div > div.PageBackgroundColor.InfoPanelMiddle > div:nth-child(3) > div.InfoPanelRowRight.BoldText")
#     peakViewers = browser.find_elements_by_css_selector(
#         "body > div.RightContent > div.MainContent > div.PageContentContainer > div.StandardPageContainer > div > div:nth-child(1) > div:nth-child(2) > div > div.PageBackgroundColor.InfoPanelMiddle > div:nth-child(5) > div.InfoPanelRowRight.BoldText")
#     streamTime = browser.find_elements_by_css_selector(
#         "body > div.RightContent > div.MainContent > div.PageContentContainer > div.StandardPageContainer > div > div:nth-child(1) > div:nth-child(2) > div > div.PageBackgroundColor.InfoPanelMiddle > div:nth-child(7) > div.InfoPanelRowRight.BoldText")
#     topGame = browser.find_elements_by_xpath(
#         """//*[@id="combinedPanel"]/div/div[2]/div/div[2]/div[8]/div[1]/a""")

#     # Saving variables into a dictionary
#     userStatsDict['User'] = link
#     userStatsDict['Followers'] = followers[0].text
#     userStatsDict['Streams'] = streams[0].text
#     userStatsDict['AverageViews'] = averageViews[0].text
#     userStatsDict['WatchTime'] = watchTime[0].text
#     userStatsDict['PeakViewers'] = peakViewers[0].text
#     userStatsDict['StreamTime'] = streamTime[0].text
#     userStatsDict['topGameLink'] = topGame[0].get_attribute("href")

#     dictlist.append(userStatsDict)

# # Overwrite to the specified file.
# # Create it if it does not exist.
# filename = "/TwitchData.csv"
# file = open(My_path + filename, "w+")

# # Get the keys of the dictionary
# keys = []
# for key in userStatsDict:
#     keys.append(key)

# # Dump all the data with CSV format
# for i in range(len(keys)):
#     file.write(str(keys[i]) + ";")
# file.write("\n")

# for i in range(len(dictlist)):
#     for j in range(len(keys)):
#         file.write(str(dictlist[i][keys[j]]) + ";")
#     file.write("\n")

# file.close()

# browser.quit()
