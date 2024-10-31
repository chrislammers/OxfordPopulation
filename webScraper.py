# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 16:41:50 2024

@author: chris
"""


import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

# A sample website (replace with one that allows scraping)
url = "https://www.booking.com/"

# Headers to simulate a real browser visit
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}

# Define a list to hold hotel price data by State
hotel_data = []

# Define a list of cities or states to search (mock list for this example)
# states = ["New+York+State", "California", "Arkansas", "Texas", "Arizona",]
states = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", 
    "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", 
    "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", 
    "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", 
    "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", 
    "New+Hampshire", "New+Jersey", "New+Mexico", "New+York+State", 
    "North+Carolina", "North+Dakota", "Ohio", "Oklahoma", "Oregon", 
    "Pennsylvania", "Rhode+Island", "South+Carolina", "South+Dakota", 
    "Tennessee", "Texas", "Utah", "Vermont", "Virginia", 
    "Washington", "West+Virginia", "Wisconsin", "Wyoming"
]
# states = ["New York"]

for state in states:
    # Add a delay to avoid overloading the server (rate limiting)
    time.sleep(1)
    
    # Prepare the search URL
    # https://www.booking.com/searchresults.en-gb.html?&sb=1&sb_lp=1&src=region&ss=New+York+State&ssne=New+York+State&ssne_untouched=New+York+State&region=2469&checkin_year=2025&checkin_month=1&checkin_monthday=5&checkout_year=2025&checkout_month=1&checkout_monthday=6&flex_window=0&efdco=1&group_adults=2&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1
    search_url = f"{url}/searchresults.html?ss={state}&checkin=2025-01-20&checkout=2025-01-21&group_adults=1&no_rooms=1&group_children=0&flex_window=20&order=price"
    # search_url = f"{url}/search?location={state}"
    
    # print(search_url)
    
    # Request the page
    response = requests.get(search_url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        # print(response.text)
        # Parse the page content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # print(soup)
        
        # Extract hotel prices - Adjust the selector based on the website's HTML structure
        # <div style="--bui_stack_spaced_gap--s: 2;" class="c624d7469d a0e60936ad a3214e5942 b0db0e8ada"><div style="--bui_stack_spaced_gap--s: 6;" class="c624d7469d f034cf5568 a937b09340 a3214e5942 f02fdbd759"><div class="dc5041d860 c72df67c95"><div style="--bui_stack_spaced_gap--s: 1;" class="c624d7469d a0e60936ad a3214e5942"><div><div class="d6767e681c"><h3 class="aab71f8e4e"><a href="https://www.booking.com/hotel/us/bellissimo-grande.en-gb.html?label=gplus-20130805&amp;aid=345379&amp;ucfs=1&amp;arphpl=1&amp;checkin=2024-12-21&amp;checkout=2024-12-22&amp;dest_id=2994&amp;dest_type=region&amp;group_adults=1&amp;req_adults=1&amp;no_rooms=1&amp;group_children=0&amp;req_children=0&amp;hpos=1&amp;hapos=1&amp;sr_order=popularity&amp;srpvid=9a3a4b98cfb503b9&amp;srepoch=1730373110&amp;all_sr_blocks=7667508_201546946_2_2_0&amp;highlighted_blocks=7667508_201546946_2_2_0&amp;matching_block_id=7667508_201546946_2_2_0&amp;sr_pri_blocks=7667508_201546946_2_2_0__24413&amp;from=searchresults" class="a78ca197d0" target="_blank" rel="noopener noreferrer" data-testid="title-link"><div data-testid="title" class="f6431b446c a15b38c233">Bellissimo Hotel, Trademark by Wyndham Near Foxwoods Casino</div><div class="ac4a7896c7">Opens in new window</div></a></h3><div class="d8c86a593f"><span class="f419a93f12"><div class="b3f3c831be" tabindex="0" aria-label="3 out of 5"><div data-testid="rating-stars" aria-hidden="true" class="a455730030" role="img"><span aria-hidden="true" class="fcd9eec8fb d31eda6efc c25361c37f"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="50px"><path d="M23.555 8.729a1.505 1.505 0 0 0-1.406-.98h-6.087a.5.5 0 0 1-.472-.334l-2.185-6.193a1.5 1.5 0 0 0-2.81 0l-.005.016-2.18 6.177a.5.5 0 0 1-.471.334H1.85A1.5 1.5 0 0 0 .887 10.4l5.184 4.3a.5.5 0 0 1 .155.543l-2.178 6.531a1.5 1.5 0 0 0 2.31 1.684l5.346-3.92a.5.5 0 0 1 .591 0l5.344 3.919a1.5 1.5 0 0 0 2.312-1.683l-2.178-6.535a.5.5 0 0 1 .155-.543l5.194-4.306a1.5 1.5 0 0 0 .433-1.661"></path></svg></span><span aria-hidden="true" class="fcd9eec8fb d31eda6efc c25361c37f"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="50px"><path d="M23.555 8.729a1.505 1.505 0 0 0-1.406-.98h-6.087a.5.5 0 0 1-.472-.334l-2.185-6.193a1.5 1.5 0 0 0-2.81 0l-.005.016-2.18 6.177a.5.5 0 0 1-.471.334H1.85A1.5 1.5 0 0 0 .887 10.4l5.184 4.3a.5.5 0 0 1 .155.543l-2.178 6.531a1.5 1.5 0 0 0 2.31 1.684l5.346-3.92a.5.5 0 0 1 .591 0l5.344 3.919a1.5 1.5 0 0 0 2.312-1.683l-2.178-6.535a.5.5 0 0 1 .155-.543l5.194-4.306a1.5 1.5 0 0 0 .433-1.661"></path></svg></span><span aria-hidden="true" class="fcd9eec8fb d31eda6efc c25361c37f"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="50px"><path d="M23.555 8.729a1.505 1.505 0 0 0-1.406-.98h-6.087a.5.5 0 0 1-.472-.334l-2.185-6.193a1.5 1.5 0 0 0-2.81 0l-.005.016-2.18 6.177a.5.5 0 0 1-.471.334H1.85A1.5 1.5 0 0 0 .887 10.4l5.184 4.3a.5.5 0 0 1 .155.543l-2.178 6.531a1.5 1.5 0 0 0 2.31 1.684l5.346-3.92a.5.5 0 0 1 .591 0l5.344 3.919a1.5 1.5 0 0 0 2.312-1.683l-2.178-6.535a.5.5 0 0 1 .155-.543l5.194-4.306a1.5 1.5 0 0 0 .433-1.661"></path></svg></span></div></div></span></div><span class="f419a93f12"><span tabindex="0" role="button" data-testid="preferred-badge"><span role="img" class="fcd9eec8fb c2a6770498 c2cc050fb8 e410954d4b" aria-label="This property is part of our Preferred Partner Programme. It is committed to providing commendable service and good value. It will pay us a higher commission if you make a booking."><svg viewBox="0 0 128 128" width="1em" height="1em"><path d="M112 8H16a8 8 0 0 0-8 8v96a8 8 0 0 0 8 8h96a8 8 0 0 0 8-8V16a8 8 0 0 0-8-8zM48 96H24V58h24zm56-25a8.7 8.7 0 0 1-2 6 8.9 8.9 0 0 1 1 4 6.9 6.9 0 0 1-5 7c-.5 4-4.8 8-9 8H56V58l10.3-23.3a5.4 5.4 0 0 1 10.1 2.7 10.3 10.3 0 0 1-.6 2.7L72 52h23c4.5 0 9 3.5 9 8a9.2 9.2 0 0 1-2 5.3 7.5 7.5 0 0 1 2 5.7z"></path></svg></span></span></span></div></div><div><div class="abf093bdfe ecc6a9ed89"><a target="_blank" rel="noopener noreferrer" href="https://www.booking.com/hotel/us/bellissimo-grande.en-gb.html?label=gplus-20130805&amp;aid=345379&amp;ucfs=1&amp;arphpl=1&amp;checkin=2024-12-21&amp;checkout=2024-12-22&amp;dest_id=2994&amp;dest_type=region&amp;group_adults=1&amp;req_adults=1&amp;no_rooms=1&amp;group_children=0&amp;req_children=0&amp;hpos=1&amp;hapos=1&amp;sr_order=popularity&amp;srpvid=9a3a4b98cfb503b9&amp;srepoch=1730373110&amp;all_sr_blocks=7667508_201546946_2_2_0&amp;highlighted_blocks=7667508_201546946_2_2_0&amp;matching_block_id=7667508_201546946_2_2_0&amp;sr_pri_blocks=7667508_201546946_2_2_0__24413&amp;from=searchresults&amp;map=1" class="a83ed08757 f88a5204c2 a1ae279108 b98133fb50"><span><span class="aee5343fdb def9bc142a" data-testid="address">North Stonington</span><span class="aee5343fdb def9bc142a">Show on map</span></span></a></div></div></div></div><div class=""><div style="--bui_stack_spaced_gap--s: 4;" class="c624d7469d a0e60936ad a3214e5942 a0ff1335a1"><div style="--bui_stack_spaced_gap--s: 1;" class="c624d7469d a0e60936ad a3214e5942"><a target="_blank" rel="noopener noreferrer" data-testid="review-score-link" href="https://www.booking.com/hotel/us/bellissimo-grande.en-gb.html?label=gplus-20130805&amp;aid=345379&amp;ucfs=1&amp;arphpl=1&amp;checkin=2024-12-21&amp;checkout=2024-12-22&amp;dest_id=2994&amp;dest_type=region&amp;group_adults=1&amp;req_adults=1&amp;no_rooms=1&amp;group_children=0&amp;req_children=0&amp;hpos=1&amp;hapos=1&amp;sr_order=popularity&amp;srpvid=9a3a4b98cfb503b9&amp;srepoch=1730373110&amp;all_sr_blocks=7667508_201546946_2_2_0&amp;highlighted_blocks=7667508_201546946_2_2_0&amp;matching_block_id=7667508_201546946_2_2_0&amp;sr_pri_blocks=7667508_201546946_2_2_0__24413&amp;from=searchresults" class="a83ed08757 f88a5204c2 c057617e1a b98133fb50"><span><div data-testid="review-score" style="--bui_stack_spaced_gap--s: 2;" class="c624d7469d eb03ae5461 dab7c5c6fa a937b09340 a3214e5942 d5fd510f01 dc7f26e57f"><div class="a3b8729ab1 d86cee9b25"><div class="ac4a7896c7">Scored 7.9 </div>7.9</div><div class="dc5041d860 c72df67c95 a29749fd9f"><div class="a3b8729ab1 e6208ee469 cb2cbb3ccb">Good </div><div class="abf093bdfe f45d8e4c32 d935416c47">2,601 reviews</div></div></div></span></a></div></div></div></div><div class="b1037148f8 c730b02848" tabindex="0" data-testid="availability-single"><div class="c19beea015"><div data-testid="recommended-units" class="ccdd44706b"><div class="ccbf515d6e c07a747311" role="none"><div class="c59cd18527"><h4 role="link" tabindex="0" class="abf093bdfe e8f7c070a7">Queen Room with Two Queen Beds, Non-Smoking</h4><ul class="ba51609c35"><li class="a6a38de85e"><div class="fc367255e6"><div class="abf093bdfe">2 large double beds</div></div></li></ul></div></div></div></div><div class="a4b53081e1"><div data-testid="availability-rate-wrapper" style="--bui_stack_spaced_gap--s: 2;" class="c624d7469d a0e60936ad a3214e5942 b23caa1645"><div class="c5ca594cb1 f19ed67e4b" data-testid="availability-rate-information"><div data-testid="price-for-x-nights" class="abf093bdfe f45d8e4c32">1 night, 1 adult</div><span data-testid="price-and-discounted-price" aria-hidden="true" class="f6431b446c fbfd7c1165 e84eb96b1f">£188</span><div class="ac4a7896c7">Price £188</div><div data-testid="taxes-and-charges" class="abf093bdfe f45d8e4c32">Includes taxes and charges</div></div><div class="da8b337763" data-testid="availability-cta"><a data-testid="availability-cta-btn" target="_blank" href="https://www.booking.com/hotel/us/bellissimo-grande.en-gb.html?label=gplus-20130805&amp;aid=345379&amp;ucfs=1&amp;arphpl=1&amp;checkin=2024-12-21&amp;checkout=2024-12-22&amp;dest_id=2994&amp;dest_type=region&amp;group_adults=1&amp;req_adults=1&amp;no_rooms=1&amp;group_children=0&amp;req_children=0&amp;hpos=1&amp;hapos=1&amp;sr_order=popularity&amp;srpvid=9a3a4b98cfb503b9&amp;srepoch=1730373110&amp;all_sr_blocks=7667508_201546946_2_2_0&amp;highlighted_blocks=7667508_201546946_2_2_0&amp;matching_block_id=7667508_201546946_2_2_0&amp;sr_pri_blocks=7667508_201546946_2_2_0__24413&amp;from=searchresults" class="a83ed08757 c21c56c305 a4c1805887 d691166b09 ab98298258 c082d89982 ff33faec5f"><span class="e4adce92df">See availability</span><span class="eedba9e88a d7eef963fa"><span class="fcd9eec8fb bf9a32efa5" aria-hidden="true"><span data-testid="availability-cta-icon" class="fcd9eec8fb bf9a32efa5" aria-hidden="true"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="50px" data-rtl-flip="true"><path d="M8.913 19.236a.9.9 0 0 0 .642-.266l6.057-6.057a1.3 1.3 0 0 0 .388-.945c.008-.35-.123-.69-.364-.945L9.58 4.966a.91.91 0 0 0-1.284 0 .896.896 0 0 0 0 1.284l5.694 5.718-5.718 5.718a.896.896 0 0 0 0 1.284.88.88 0 0 0 .642.266"></path></svg></span></span></span></a></div></div></div></div></div>
        hotels = soup.find_all("div", class_="c624d7469d a0e60936ad a3214e5942 b0db0e8ada")
        
        # print(hotels)
        
        for hotel in hotels:
            try:
                # Extract hotel name
                # <div data-testid="title" class="f6431b446c a15b38c233">Bellissimo Hotel, Trademark by Wyndham Near Foxwoods Casino</div>
                # <div data-testid="title" class="f6431b446c a15b38c233">Hotel Indigo NYC Financial District, an IHG Hotel</div>
                name = hotel.find("div", class_="f6431b446c a15b38c233").text.strip()
                
                # Extract hotel price
                # <span data-testid="price-and-discounted-price" aria-hidden="true" class="f6431b446c fbfd7c1165 e84eb96b1f">£188</span>
                price = hotel.find("span", class_="f6431b446c fbfd7c1165 e84eb96b1f").text.strip()
                
                # Save the data
                hotel_data.append({"State": state, "Hotel Name": name, "Price": price})
            except AttributeError:
                continue  # Skip if data is missing or malformed
            
    else:
        print(f"Failed to retrieve data for {state} with status code: {response.status_code}")

# Convert to a DataFrame and calculate average price per state
df = pd.DataFrame(hotel_data)


# df["Price"] = df["Price"].replace("[\$,]", "", regex=True).astype(float)  # Clean and convert prices to float
# average_prices = df.groupby("State")["Price"].mean().sort_values()

# print("Average hotel prices by state:")
# print(average_prices)

df.to_csv("out.csv")