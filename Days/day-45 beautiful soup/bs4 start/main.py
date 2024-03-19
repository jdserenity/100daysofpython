import requests; from bs4 import BeautifulSoup;

response = requests.get('https://news.ycombinator.com/news')
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')

article_titles = [title.text for title in soup.select('.titleline a')]
article_titles = [item for idx, item in enumerate(article_titles) if idx % 2 == 0]

# print(article_titles)
# print(len(article_titles))

article_links = [link.get('href') for link in soup.select('.titleline a')]
article_links = [item for idx, item in enumerate(article_links) if idx % 2 == 0]

# print(article_links)
# print(len(article_links))

sublines = soup.find_all(class_='subline')

print(len(sublines))

indexes_with_no_score = []
for i, item in enumerate(sublines):
    print('score' in str(item))
    if 'score' not in str(item):
        indexes_with_no_score.append(i)

print(indexes_with_no_score)

article_upvotes = [int(upvotes.text.split(' ')[0]) for upvotes in soup.find_all(class_='score')]

if indexes_with_no_score:
    for i in indexes_with_no_score:
        article_upvotes.insert(i, -100000000000000)


# print(article_upvotes)
print(len(article_upvotes))

highest_upvote = -100000000000000
highest_upvote_index = 0
for i, upvote in enumerate(article_upvotes):
    if upvote > highest_upvote:
        highest_upvote_index = i

# print(highest_upvote_index)

# print(article_titles[highest_upvote_index])
# print(article_links[highest_upvote_index])
# print(article_upvotes[highest_upvote_index])