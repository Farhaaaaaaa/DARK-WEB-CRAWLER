def LinksScrap(list):
    import TorSearcher

    try:
        thelist = list
        print("Opening ...", thelist)
        with open(thelist, "r", encoding="utf-8") as newfile:
            data = newfile.readlines()
            try:
                for k in data:
                    try:
                        k = k.replace("\n","")
                        k = "http://" + k
                        TorSearcher.MainScrapper(k)
                    except Exception as Er:
                        print("\nWebsite Showing Error Or Not Responding, Moving Forward...")
            except Exception as E:
                print(E)
    except:
        print("Usage : Enter File Name For Processing...")