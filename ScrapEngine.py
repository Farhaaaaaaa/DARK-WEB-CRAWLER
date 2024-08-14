def Scrapengine():
    def is_tor_running(): # Check if TOR running
        import psutil
        app_name="tor.exe"
        # Iterate over all running processes
        for process in psutil.process_iter(['pid', 'name']):
            try:
                # Check if process name contains tor.exe
                if process.info['name'].lower() == app_name.lower():
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return False

    def run_tor(path,result): # Run TOR
        import subprocess
        try:
            subprocess.Popen([path])
            result['status'] = 1
            print("\nTor.exe is Online...")
        except FileNotFoundError:
            print(f"Tor.exe at path: {path} was not found.")
            result['status'] = 0
        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e}")
            result['status'] = 0
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            result['status'] = 0

    def main_program():
        #Main Program Stimulated
        for i in range(10):
            print(f"Main program is running... {i}")
            time.sleep(1)

    import pyfiglet
    name = "DW Crawler"
    figlet = pyfiglet.Figlet(font='slant')
    ascii_art = figlet.renderText(name)
    print(ascii_art)
    print("Made by Team - Deep Diver")
    print("\nTOR must be running in Background\nVPN must be connected\n\n")

    # Menu For Scraping 
    Option=input("Enter which service you want\n 1. Scrap Tor Website\n 2. Search Tor links by Keywords\n(1 or 2):")

    if Option == '1':
        import threading    # To start tor.exe in Background
        import time 

        run=0
        print("Checking tor.exe ...\n")
        tor=is_tor_running()
        if tor==False:
            print("Tor is Offline...\n")
            # Get the path to the Tor application from the user
            # Path = "D:\Tor Browser\Browser\TorBrowser\Tor\tor.exe"
            tor_path = input("Please enter the full path to tor.exe: ")

            # Dictionary to store the result from the thread
            result = {'status': None}

            # Start the thread to run the Tor application
            tor_thread = threading.Thread(target=run_tor, args=(tor_path, result))
            tor_thread.start()

            # Run the main program
            main_program()

            # Wait for the Tor thread to complete
            tor_thread.join()

            if result['status']==1:
                run=1
        else:
            print("Tor.exe is Online...\n")
            run=1

        if run==1:
            Vote = input("\nDo you want to scrap particular website (Type 1) or List of Links (Type 2):")
            if Vote =='1':
                # Put URL to Scrap 
                url=input("\nInput the Url of the Website you want to scrap: ")
                # Importing Scraper
                import TorSearcher
                TorSearcher.MainScrapper(url)
            elif Vote =='2':
                list=input("\nEnter List Name: ")
                # Importing Scraper to Scrap list of Links
                import VastScrap
                VastScrap.LinksScrap(list)
            else:
                print("\nEnter a Valid Option...")
        else:
            print("\nProgram stopped because TOR is not online.")

    elif Option == '2':
        # Scrap for Links
        keyword=input("\nEnter Your Keyword or Phrase: ")
        import Scrapper
        Scrapper.ScrapperVPN(keyword)
    else :
        print("\nEnter a Valid Option...")

Scrapengine()        
