# -*- coding: utf-8 -*-
import scrapy
import datetime
from hrfoecast.items import HrfoecastItem


class HrSpider(scrapy.Spider):
    """
    scraped data from hrforecast.de
    """
    name = 'hrforecast'
    allowed_domains = ['hrforecast.de']
    start_urls = ['https://www.hrforecast.de/company/career/']

    def response_is_ban(self, request, response):
        # scrapy-proxy-pool function
        return b'banned' in response.body

    def exception_is_ban(self, request, exception):
        # scrapy-proxy-pool function
        return None

    def vacancy_data(self, response):

        main_selector = '//*[@id="av_section_1"]/div/main/div/div/div[1]/section/div'
        raw_data = response.xpath(main_selector)

        scraped_info = HrfoecastItem()

        # data for job_url info
        scraped_info['job_url'] = response.url
        # data for job_title info
        scraped_info['job_title'] = \
            raw_data.xpath('p[1]/strong/text()').extract()[0]

        # data for company_name info
        scraped_info['company_name'] = HrSpider.name
        # data for crawled_date
        scraped_info['crawled_date'] = str(datetime.date.today())
        # data for posted_date
        scraped_info['posted_date'] = str(datetime.date.today())
        # data for location
        scraped_info['location'] = response.xpath(
            '//*[@id="av_section_1"]/div/main/div/div/div[2]/section/div/p/strong/text()').get().replace(
            'Location: ', '')
        # data for  job_description
        temporaly_data = ''
        for item in raw_data.xpath('p/text()|p/strong/text()')[1:]:
            temporaly_data += item.get() + '\n'
        scraped_info['job_description'] = temporaly_data

        yield scraped_info

    def parse(self, response):

        vacancy_selector = '//h3[@class="grid-entry-title entry-title"]/a/@href'

        for link in response.xpath(vacancy_selector):
            yield scrapy.Request(url=link.get(), callback=self.vacancy_data)
