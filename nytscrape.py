from pynytimes import NYTAPI
from datetime import datetime

api_key = "XXXXXXXXXX" # make sure to X this out before committing code


#Set up start and end date objects

begin = datetime(2023, 1, 1)

end = datetime(2024, 1, 31)

# Set the beginning and end dates for the search.
date_dict = {"begin":begin, "end":end}

options_dict = {
    "type_of_material": [ "News Analysis", "News", "Article" ]
}

nyt = NYTAPI(api_key, parse_dates=True)

file = open('readdata.txt', 'w')

articles = nyt.article_search(query = "Israel Palestine", 
                              results = 25,
                              dates = date_dict,
                              options = options_dict)


for article in articles:
    weburl = article["web_url"]
    title = article["headline"]["main"]
    abstract = article["abstract"]

    file.write("URL: " + weburl + "\n")
    file.write("TITLE: " + title + "\n")
    file.write("ABSTRACT: " + abstract + "\n")
    
    multimedia = article["multimedia"]
    for m in multimedia:
        mediatype = m["type"]
        caption = m["caption"]
        url = "https://www.nytimes.com/" + m["url"]

        if mediatype == "image":
            file.write("IMAGE URL: " + url + "\n")
            if caption != None:
                file.write("CAPTION: " + caption + "\n")
            else:
                file.write("CAPTION: no caption" + "\n")
    file.write("\n")