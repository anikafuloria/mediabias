import newspaper

cnn_paper = newspaper.build('https://edition.cnn.com/world/middle-east')
print(cnn_paper.size())
file = open('data2.txt', 'w')

for a in cnn_paper.articles:
    url = a.url
    
    article = newspaper.Article(url=url, language='en')
    article.download()
    article.parse()

    article ={
        "title": str(article.title),
        "text": str(article.text),
        "authors": article.authors,
        "published_date": str(article.publish_date),
        "top_image": str(article.top_image),
        "videos": article.movies,
        "keywords": article.keywords,
        "summary": str(article.summary)
    }


    file.write(article["title"] \
               + "\n"\
               + article["top_image"]\
               + "\n\n")

file.close()