
def MainScrapper(url):

    # import logging

    # logging.basicConfig(filename='crawler.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def parse_content(response):
        from string import punctuation
        from bs4 import BeautifulSoup
        from nltk.corpus import stopwords
        from nltk.tokenize import word_tokenize, sent_tokenize
        from nltk.probability import FreqDist
        # Parse HTML content using BeautifulSoup
        soup = BeautifulSoup(response, 'html.parser')
        # Extract text content from parsed HTML
        text_content = soup.get_text()
        relevant_info=""
        for tag in soup.find_all(['p', 'div']):
            text_content = tag.get_text().strip()
            if text_content:
                relevant_info=relevant_info+text_content
        # Tokenize the text into words    
        tokens = word_tokenize(relevant_info)
        # Get English stopwords
        stop_words = set(stopwords.words('english'))
        # Remove stopwords and punctuation from tokens
        cleaned_tokens = [word.lower() for word in tokens if word.lower() not in stop_words and word.lower() not in punctuation ]
        cleaned_tokens = FreqDist(cleaned_tokens)
        return cleaned_tokens
    
    def extract_urls(response):
        from bs4 import BeautifulSoup
        import urllib.parse
        # Extract URLs from the response
        extracted_urls = []
        soup = BeautifulSoup(response, 'html.parser')
        for link in soup.find_all('a', href=True):
            url = link['href']
            # Normalize and validate the URL
            parsed_url = urllib.parse.urljoin(response, url)
            if parsed_url.startswith("http://") or parsed_url.startswith("https://"):
                extracted_urls.append(parsed_url)
        return extracted_urls
    
    def torSearcher(url):
        import requests
        import random
        def get_tor_session():
            session = requests.session()
            # Tor uses the 9050 port as the default socks port
            session.proxies = {'http':  'socks5h://127.0.0.1:9050',
                            'https': 'socks5h://127.0.0.1:9050'}
            return session

        # Make a request through the Tor connection
        # IP visible through Tor
        session = get_tor_session()

        # User-Agents
        ua_list = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19577"
        ,"Mozilla/5.0 (X11) AppleWebKit/62.41 (KHTML, like Gecko) Edge/17.10859 Safari/452.6", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2656.18 Safari/537.36"
        ,"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/44.0.2403.155 Safari/537.36", "Mozilla/5.0 (Linux; U; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13","Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27"
        ,"Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_8; zh-cn) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27"]
        ua = random.choice(ua_list)
        headers = {'User-Agent': ua}
        print("Getting ...", url)
        result = session.get(url)
        
        #print(requests.get("http://httpbin.org/ip").text)

        # Extract Keywords From webpage
        Keyword_list=parse_content(result.text)
        # Extract Links From webpage
        Link_list=extract_urls(result.text)

        # import string
        # filename = ''.join(random.choice(string.ascii_lowercase) for i in range(16))
        filename = input("\nEnter File name to save Scraped Items: ")
        # Save The HTML 
        with open(f"{filename}.txt","w+", encoding="utf-8") as newthing:
            newthing.write(result.text)
        # Save The Keywords
        with open(f"keyword-{filename}.txt", "w+", encoding="utf-8") as file:
            for keyword, freq in Keyword_list.items():
                file.write(f"{keyword}: {freq}\n")
        # Save The Links
        with open(f"link-{filename}.txt", "w+", encoding="utf-8") as file:
            for link in Link_list:
                file.write(f"{link}\n")
        
        # carry=int(input("\n\n1.Continue to Menu\n2.Exit\n"))
        # if carry==1:
        #     import ScrapEngine
        #     ScrapEngine.Scrapengine()
        # else:
        #     pass

            
    if not url.startswith("http://"):
        url="http://"+url
    torSearcher(url)

