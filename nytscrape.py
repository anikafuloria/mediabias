from pynytimes import NYTAPI

# Import datetime function from datetime library which allows us to create a datetime object
from datetime import datetime

api_key = "XXXXXXXXXX" # make sure to X this out before committing code


#Set up start and end date objects

begin = datetime(2023, 1, 1)

end = datetime(2024, 1, 31)

#Create dictionary containing dates data

date_dict = {"begin":begin, "end":end}

nyt = NYTAPI(api_key, parse_dates=True)

# Grab the first data item in top_stories and view it
top_stories = nyt.top_stories()

top_story = top_stories[0]

print("The top story is: ", top_story['title'])

# Retrieve the most viewed articles for today.

articles = nyt.article_search(query = "Israel Palestine", 
                              results = 10,
                              dates = date_dict)

# Assign the data in the first item of articles to a variable
article = articles[0].copy()

print(article["web_url"])
print(article["abstract"])
print(article["multimedia"])