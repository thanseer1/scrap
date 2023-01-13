from selectorlib import Extractor
import requests 
from time import sleep
import csv

# Create an Extractor by reading from the YAML file
e = Extractor.from_yaml_file('booking.yml')

def scrape(url):    
    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'DNT': '1',
        'Upgrade-Insecure-Requests': '1',
        # You may want to change the user agent if you get blocked
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',

        'Referer': 'https://www.booking.com/searchresults.en-gb.html?label=gen173nr-1FCAEoggI46AdIM1gEaGyIAQGYAQm4ARfIAQzYAQHoAQH4AQuIAgGoAgO4Au-chZ4GwAIB0gIkNDA0MDZiZjgtZDNhYi00NDNiLWE1MGQtY2Q5ZThiMDlkN2Jm2AIG4AIB&lang=en-gb&sid=52a275ff8693a7145de30aab221433fe&sb=1&sb_lp=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.en-gb.html%3Flabel%3Dgen173nr-1FCAEoggI46AdIM1gEaGyIAQGYAQm4ARfIAQzYAQHoAQH4AQuIAgGoAgO4Au-chZ4GwAIB0gIkNDA0MDZiZjgtZDNhYi00NDNiLWE1MGQtY2Q5ZThiMDlkN2Jm2AIG4AIB%26sid%3D52a275ff8693a7145de30aab221433fe%26sb_price_type%3Dtotal%26%26&ss=Alleppey%2C+Kerala%2C+India&is_ski_area=&ssne=Tokyo&ssne_untouched=Tokyo&checkin_year=&checkin_month=&checkout_year=&checkout_month=&efdco=1&group_adults=2&group_children=0&no_rooms=2&b_h4u_keep_filters=&from_sf=1&ss_raw=alappuzha&ac_position=0&ac_langcode=en&ac_click_type=b&ac_meta=GhAxZWYwNTdiNzE1ZWQwMmMzIAAoATICZW46CWFsYXBwdXpoYUAASgBQAA%3D%3D&dest_id=-2088519&dest_type=city&place_id_lat=9.498076&place_id_lon=76.338844&search_pageview_id=1ef057b715ed02c3&search_selected=true&search_pageview_id=1ef057b715ed02c3&ac_suggestion_list_length=5&ac_suggestion_theme_list_length=0',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    # Download the page using requests
    print("Downloading %s"%url)
    r = requests.get(url, headers=headers)
    # Pass the HTML of the page and create 
    return e.extract(r.text,base_url=url)


with open("urls.txt",'r') as urllist, open('data.csv','w') as outfile:
    fieldnames = [
        "name",
        "location",
        "price",
        "price_for",
        "room_type",
        "beds",
        "rating",
        "rating_title",
        "number_of_ratings",
        "url"
    ]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames,quoting=csv.QUOTE_ALL)
    writer.writeheader()
    for url in urllist.readlines():
        data = scrape(url) 
        if data:
            for h in data['hotels']:
                writer.writerow(h)
            # sleep(5)
