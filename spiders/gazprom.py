# -*- coding: utf-8 -*-
import scrapy
import datetime
from hrfoecast.items import HrfoecastItem


class GazpromSpider(scrapy.Spider):
    name = 'gazprom'
    allowed_domains = ['gazpromvacancy.ru']
    start_urls = ['https://www.gazpromvacancy.ru/jobs/']
    g = 0

    def vacancy_data(self, response):

        main_selector = '//*[@class="job-container"]'
        raw_data = response.xpath(main_selector)

        scraped_info = HrfoecastItem()

        # data for job_title info
        scraped_info['job_title'] = raw_data.xpath(
            '//*[@id="content-normal"]/article/h1/text()').extract()[0]

        # data for company_name info
        scraped_info['company_name'] = response.xpath(
            '//*[@id="content-normal"]/article/dl/dd[1]/a/text()').extract()[0]

        # data for crawled_date
        scraped_info['crawled_date'] = str(datetime.date.today())

        # data for posted_date
        raw_data = response.xpath(
            '//*[@id="content-normal"]/article/dl/dd[5]/time/text()').extract()[
            0].replace('\n', '').split()

        month = {'января': '01', 'февраля': '02', 'марта': '03', 'апреля': '04',
                 'мая': '05', 'июня': '06', 'июля': '07', 'августа': '08',
                 'сентября': '09', 'октября': '10', 'ноября': '11',
                 'декабря': '12'}

        scraped_info['posted_date'] = "{2}-{1}-{0}".format(raw_data[0],
                                                           month[raw_data[1]],
                                                           raw_data[2])

        # data for location
        scraped_info['location'] = response.xpath(
            '//*[@id="content-normal"]/article/dl/dd[2]/text()').get()

        # data for  job_description
        temporaly_data = ''
        for item in response.xpath('//*[@id="content-normal"]/article/div[1]'):
            temporaly_data += item.xpath('h2/text()').get() + '\n'
            temporaly_data += item.xpath('p').get().replace('<br>',
                                                            '\n').replace('<p>',
                                                                          '').replace(
                '</p>', '') + '\n'
        for item in response.xpath('//*[@id="content-normal"]/article/div[2]'):
            temporaly_data += item.xpath('h2/text()').get() + '\n'
            temporaly_data += item.xpath('p').get().replace('<br>',
                                                            '\n').replace('<p>',
                                                                          '').replace(
                '</p>', '')
        scraped_info['job_description'] = temporaly_data

        # print(scraped_info['job_description'])
        yield scraped_info

    def parse(self, response):

        vacancy_selector = '//*[@class="job-list-item"]/h3/a/@href'

        for link in response.xpath(vacancy_selector):
            vacancy_url = 'https://www.gazpromvacancy.ru/' + link.get()
            # print(vacancy_url)
            yield scrapy.Request(url=vacancy_url, callback=self.vacancy_data)

        page_link = response.xpath(
            '//li[@class="current"]/following::li[1]/a/@href')

        if page_link:
            print('next page = ', page_link.get())
            yield scrapy.Request(
                url='https://www.gazpromvacancy.ru/' + page_link.get(),
                callback=self.parse)
