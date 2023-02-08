import scrapy
import requests
class AmazonSpider(scrapy.Spider):
    name = "amazon"
    allowed_domains = ["amazon.in"]
    start_urls = ['https://api.scraperapi.com?api_key=3b346420584fa10531d7669b9c8a04a5&url=https://www.amazon.in/s?k=books&crid=1S8ZOBLT8TBJ2&sprefix=bo%2Caps%2C413&ref=nb_sb_noss_2']

    def parse(self, response):
        for product in response.css("div.ssg-col-20-of-24.s-result-item.s-asin.sg-col-0-of-12.sg-col-16-of-20.sg-col.s-widget-spacing-small.sg-col-12-of-16"):
            yield {
                'url': product.css("a.a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal::attr(href)").get(),
            }

        next_page = response.css("li.a-last a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
