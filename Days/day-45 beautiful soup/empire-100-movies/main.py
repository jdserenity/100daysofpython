import requests, bs4

res = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
res.raise_for_status()
data = res.text

soup = bs4.BeautifulSoup(data, 'html.parser')

# print(soup.prettify())

titles = [title.text + '\n' for title in soup.find_all('h3', class_='title')]

titles.reverse()

print(titles)

with open('/Users/angelorg/Documents/Serenity, Inc./Coding/100 Days Python Course/Days/day-45 beautiful soup/empire-100-movies/movies.txt', 'w') as file:
    file.writelines(titles)