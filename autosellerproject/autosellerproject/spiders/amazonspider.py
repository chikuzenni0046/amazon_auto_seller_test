
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class AmazonSpider(CrawlSpider):
    name = "new_amazon_spider"

    allowed_domains = ['amazon.co.jp']
    start_urls = ['https://www.amazon.co.jp/gp/product/4047300845/ref=s9u_simh_gw_i1?ie=UTF8&pd_rd_i=4047300845&pd_rd_r=BCCWCJJQYJ6HGCNKGDJ0&pd_rd_w=Td36m&pd_rd_wg=RYLO9&pf_rd_m=AN1VRQENFRJN5&pf_rd_s=&pf_rd_r=108ZENEHSVNWP8V03Y0E&pf_rd_t=36701&pf_rd_p=d4802771-73ad-49b1-a154-90aaec384d3e&pf_rd_i=desktop']

    rules = (Rule(LinkExtractor(allow=r'https://www.amazon.co.jp/gp/product/4047300845/ref=s9u_simh_gw_i1?ie=UTF8&pd_rd_i=4047300845&pd_rd_r=BCCWCJJQYJ6HGCNKGDJ0&pd_rd_w=Td36m&pd_rd_wg=RYLO9&pf_rd_m=AN1VRQENFRJN5&pf_rd_s=&pf_rd_r=108ZENEHSVNWP8V03Y0E&pf_rd_t=36701&pf_rd_p=d4802771-73ad-49b1-a154-90aaec384d3e&pf_rd_i=desktop'), callback = 'parse_topics'),)
    
    def parse_topics(self, response):
    
        item = headline()
        item['title'] = response.xpath('//span[@id="productTitle"]').extract_first()
        item['value'] = response.xpath('//a[@class="a-size-mini a-link-normal"]').extract_first()
        yield item
        print(item['title'])



