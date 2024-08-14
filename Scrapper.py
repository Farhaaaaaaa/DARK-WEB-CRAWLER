#System must be connected with VPN otherwise ahmia-website wouldn't work
def ScrapperVPN(keyword):
    import requests
    #Link to Fetch IP
    url = "http://ip-api.com/json/"
    key = requests.get(url)
    #Checking If Connected to VPN or not | Configured According to region
    if "India" in key.text or "Bengal" in key.text or "Kolkata" in key.text:
        print("Your VPN might not be on !!")
        safe = False
    else:
        safe = True

    #importing Scraper to Scrap out links
    if safe == True:
        import ScraperAhmia
        ScraperAhmia.Scraper(keyword)
    else:
        print("IP change failed, try again.")