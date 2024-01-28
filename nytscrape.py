from pynytimes import NYTAPI
from datetime import datetime

api_key = "XXXXXXXXXX" # make sure to X this out before committing code


#Set up start and end date objects

begin = datetime(2023, 1, 1)

end = datetime(2024, 1, 31)

# Set the beginning and end dates for the search.
date_dict = {"begin":begin, "end":end}

nyt = NYTAPI(api_key, parse_dates=True)

file = open('readdata.txt', 'w')

articles = nyt.article_search(query = "Israel Palestine", 
                              results = 25,
                              dates = date_dict)

for article in articles:
    weburl = article["web_url"]
    abstract = article["abstract"]

    file.write(weburl + "\n")
    file.write(abstract + "\n")
    
    multimedia = article["multimedia"]
    for m in multimedia:
        mediatype = m["type"]
        caption = m["caption"]
        url = "https://www.nytimes.com/" + m["url"]

        if mediatype == "image":
            file.write(url + "\n")
            if caption != None:
                file.write(caption, "\n")
            else:
                file.write("no caption\n")
    file.write("\n")