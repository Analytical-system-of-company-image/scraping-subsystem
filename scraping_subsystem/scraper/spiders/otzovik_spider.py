from scrapy.spiders.sitemap import Spider
from scraping_subsystem.scraper.items import Review
from scrapy.exceptions import CloseSpider


class OtzovikSpider(Spider):
    """Скраппер для сайта otzovik.ru

    Args:
        SitemapSpider (SitemapSpider): Класс Краулера

    Raises:
        ValueError: Нет доступа к otzovik.ru
    """

    name = 'otzovik_spider'

    handle_httpstatus_list = [507]

    page_number = 1

    def parse(self, response):
        root_reviews = response.xpath(
            "//*[@id='content']/div/div/div/div/div[3]/div[1]/div[1]")
        reviews = root_reviews.xpath(
            "//*[@id='content']/div/div/div/div/div[3]/div[1]/div[1]/div")

        if len(reviews) == 0:
            raise CloseSpider('No reviews in response')
        del root_reviews
        for review in reviews:
            tmp_review = Review()
            tmp_review['review_url'] = review.xpath("./meta[1]/@content").get()
            tmp_review['author'] = review.xpath(
                "./div[@itemprop='author']/div/div/a/span/text()").get()
            tmp_review['review_date'] = review.xpath(
                "./div[@class='item-right']/div[@class='review-postdate']/span/@title").get()
            tmp_review['text_data'] = review.xpath(
                "./div[@class='item-right']/div[@class='review-teaser']/text()").get()
            yield tmp_review
        self.page_number += 1
        next_page = f"http://otzovik.com/reviews/set_sportivnih_magazinov_sportmaster_russia_moscow/{self.page_number}/"
        yield response.follow(next_page, callback=self.parse)
