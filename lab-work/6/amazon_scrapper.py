import scrapy


class AmazonSpider(scrapy.Spider):
    name = "amazon"
    start_urls = [
        "https://www.amazon.in/s?k=laptop&ref=nb_sb_noss_2",
        "https://www.amazon.in/s?k=laptop&page=3&qid=1617433079&ref=sr_pg_3",
        "https://www.amazon.in/s?k=laptop&page=6&qid=1617433116&ref=sr_pg_6",
    ]

    def parse(self, response):
        for data in response.css("div.s-result-item"):
            print(data)
            yield {
                "title": data.css("span.a-size-medium::text").get(),
                "discountedPrice": data.css("span.a-price-whole::text").get(),
                "imgUrl": data.css("div.a-section img.s-image::attr('src')").get(),
                "actualPrice": data.css("span.a-offscreen::text").get(),
                "rating": data.css("span.a-icon-alt::text").get(),
            }
        next_page = response.css("li.a-last a::attr('href')").get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
