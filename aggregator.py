from bs4 import BeautifulSoup
import requests

webpage_list = ['https://www.irishtimes.com/', 'https://www.independent.ie/', 'https://www.irishexaminer.com/', 'https://www.thejournal.ie/']

for webpage in webpage_list:
    r = requests.get(webpage)
    with open('website.txt', 'wb') as target:
        target.write(r.content)

    with open('website.txt', 'r') as html_file:
        soup = BeautifulSoup(html_file, 'lxml')

    #IRISH TIMES HEADLINE
    if webpage_list.index(webpage) == 0:
        newspaper = 'The Irish Times'
        article = soup.find('div', class_='row topspotelement')
        body = article.text.strip()
        link = 'https://www.irishtimes.com' + (article.a['href']).strip()
        print(newspaper)
        print(body)
        print(link)
        print()

    #Irish independent
    if webpage_list.index(webpage) == 1:
        newspaper = 'Irish Independent'
        article = soup.find('div', class_='n-backdrop1-wrap')
        body = article.find('h2', class_='title2').text.strip()
        link = 'https://www.independent.ie' + (article.find('figure', class_='c-card1-image').a['href']).strip()
        print(newspaper)
        print(body)
        print(link)
        print()

    #Irish Examiner
    if webpage_list.index(webpage) == 2:
        newspaper = 'Irish Examiner'
        article = soup.find('div', class_='col-lg-8 main-card')
        body = article.find('h5', class_='card-title top-main-title').text.strip()
        link = 'https://www.irishexaminer.com' + (article.a['href']).strip()
        print(newspaper)
        print(body)
        print(link)
        print()

    #The Journal
    if webpage_list.index(webpage) == 3:
        newspaper = 'The Journal'
        article = soup.find('div', class_='primary span-8')
        body = article.find('h1').text.strip()
        link = (article.find('div', class_='img').a['href']).strip()
        print(newspaper)
        print(body)
        print(link)





#print(headline)
#print(soup.prettify())
