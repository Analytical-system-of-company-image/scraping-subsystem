# ScrapingSubsystem
Airflow with Scrapy

This library for [DAG's Apache Airflow](https://github.com/Analytical-system-of-company-image/asci-airflow) with little crawlers for scarping reviews from some websites about companies.

## Pull of websites

Пул источников можно разделить на три категории в зависимости от источников создания этих отзывов (курсивом выделены наиболее интересные):

1. Сайт с отзывами клиентов;

2. Сайт с отзывывами работников;

3. Сайт со смешанными отзывами.

Сайты с отзывами клиентов:

1. otzovik.com

2. market.yandex.ru

3. zoon.ru

4. pravogolosa.net

5. nanegative.ru (сайт интересен тем что там только негативные отзывы)

6. flamp.ru (проект от 2GIS, отзывы в основном про места и заведения. Отзыв публикуется после регистрации и модерируется без особого пристрастия)

7. spr.ru/

8. be-in.ru 

9. yell.ru (сервис с отзывами о местах, но с регистрацией и достаточно сложной модерацией. На сегодняшний момент июль 2018, в каталоге отсутствует много крупных городов)

10. otzyvov.net

11. migreview.com

Сайты с отзывами работников:

1. pravda-sotrudnikov.ru

2. ru.indeed.com

3. ne.orabote.net

4. правда-работников.рф

5. www.vnutri.org

Сайты со смешанными отзывами:

1. irecommend.ru (в целом большинство отзывов от клиентов, но также встречаются отзывы от работников)


***

## How deploy dev environment

```bash
poetry install
pip install dostoevsky==0.6.0
python3 -m nltk.downloader all
python -m dostoevsky download fasttext-social-network-model
```

## How to public to Pypi
First you need create api on pypi

```bash
poetry config pypi-token.pypi $(cat .token)
poetry publish --build
```