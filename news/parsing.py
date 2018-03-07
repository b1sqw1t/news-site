# -*- coding: utf-8 -*-
#Парсинг новостных сайта(ов)
import requests
from bs4 import BeautifulSoup

def get_html(url): #Тут мы получаем ссылку и отправляем в ответ html код страницы
    r = requests.get(url)   #Response
    return r.text           #Response html code url Возвращает html код страницы

def get_out(title):#Функция ищет в тексте начала тега < и конец > и удаляет их и все что в них и возвращает текст
    try:
        while True:
            if '<' in title:
                title = title[:title.index('<')]+title[title.index('>')+1:]
            else:
                break
    except:
        pass
    return title

def get_url_image(text):#Функция будет вытаскивать из текста ссылку на изображение
    try:
        text = text[text.index('src="')+5:]
        text = text[:text.index('"')]
    except:
        pass
    return text




def get_all_category(html): #получаем html код и оттуда выискиваем ШАПКУ МЕНЮ САЙТА и оттуда берем категории для ссылок
    soup = BeautifulSoup(html, 'lxml')
    # Находим блок div с классом b-main-nav и извлекаем из него все li с классом b-main_nav__main-item в переменную lis (<li>'s)
    lis = soup.find('div', class_='b-main-nav').find_all('li', class_='b-main-nav__main-item')
    links = []
    for li in lis:
        #собераем все категории для ссылок
        a =li.find('a').get('href') # уже строка
        # в нескольких вариантах выводит полные ссылки.а нам нужны лишь категории страниц. по этому отсекает эти ссылки
        if 'http' in a:
            a = None
        if a and len(a)>1:
            links.append(a)
    return links


def get_all_links(html): #получаем все категории новостей для ссылок на их страницы
    soup = BeautifulSoup(html, 'lxml')
    #НА сайте для вывода списков новостей категоий используются 2 вида шаблонов
    #Первый шаблон исользуют категории (politics, ociety,economy,world,incidents)
    #второй шаблон используют категории (science,culture,radio)

    try:
        # берем ссылки с первого шаблона
        lis = soup.find('div', class_='b-list').find_all('div', class_='b-list__item')
        links = []
        for li in lis:
            #собераем все ссылки
            a =li.find('a').get('href') # уже строка
            links.append(a)
        return links
    except:
        pass

    try:
        # берем ссылки со второго шаблона
        lis = soup.find('div', class_='owl-carousel').find_all('div', class_='b-themespec__tiles-item')
        links = []
        for li in lis:
            # собераем все ссылки
            a = li.find('a').get('href')  # уже строка
            links.append(a)
        return links
    except:
        pass


def get_context_links(html,url):
    try:
        soup = BeautifulSoup(html, 'lxml')
        result = dict()
        title = soup.find('h1', class_='b-article__title').get_text() #Избавится от тега <span>

        result['title'] = title
        result['dt'] = get_out(str(soup.find('div', class_='b-article__info-date').find_all('span'))) #Избавится от тегов
        result['text'] = str(soup.find('div',class_='b-article__body js-mediator-article mia-analytics').find_all('p'))
        result['text'] = result['text'].replace(u'\xa0', u' ')
        result['image'] = get_url_image(str(soup.find('div', class_='b-media__size').find_all('img')))
        result['url'] = url
        #result['copyright'] = str(soup.find('div', class_='b-media-copyright__copy').find('a').get_text())


        print('ГОТОВО')
        return result

    except:
        print('ОШИБКА')



    #КАКИЕ ДАННЫЕ НУЖНЫ ИЗ НОВОСТЕ
    #1.Заголовок статьи! тег - h1, class_ = b-article__title.
    #2.Текст статьи
    #3.Изображение статьи
    #4.Автор статьи
    #5.Дата и время публикации! тег - div, class_ = b-article__info-date
    #6.Ссылка на статью





def main():
    url = 'https://ria.ru'
    all_category = get_all_category(get_html(url))
    all_links=[]
    context=[] #Тут хранятся все новости

    for category in all_category:
        print(url+category)
        all_links.append(get_all_links(get_html(url+category)))
    context = []
    for list in all_links:
        for urls in list:
            print(url+urls)
            context.append(get_context_links(get_html(url+urls),url+urls))
    return context
main()



