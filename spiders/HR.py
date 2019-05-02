# -*- coding: utf-8 -*-
import scrapy
import datetime


class HrSpider(scrapy.Spider):
    name = 'hrforecast'
    allowed_domains = ['hrforecast.de']
    start_urls = ['https://www.hrforecast.de/company/career/']
    # '//h3[@class="grid-entry-title entry-title"]/a/@href'
    i = 0
    # setting the location of the output csv file
    custom_settings = {
        'FEED_FORMAT' : 'csv',
        'FEED_URI': 'temp/hrforecast.csv'
    }

    #rules = (Rule(LinkExtractor(restrict_xpaths=('//h3[@class="grid-entry-title entry-title"]/a/@href')), 'parse'), )

    def vacancy_data (self, response):
        print('In vacancy_data ', response.url)


        main_selector = '//*[@id="av_section_1"]/div/main/div/div/div[1]/section/div'
        raw_data = response.xpath(main_selector)
        job_title_selector = 'p[1]/strong/text()'

        # data for job_title info
        job_title = raw_data.xpath(job_title_selector).extract()
        print(job_title)
        # data for company_name info
        company_name = HrSpider.name
        # data for crawled_date
        crawled_date = str(datetime.date.today())
        # data for posted_date
        posted_date = str(datetime.date.today())
        # data for location
        location = response.xpath('//*[@id="av_section_1"]/div/main/div/div/div[2]/section/div/p/strong/text()').get()
        # data for  job_description
        job_description = ''
        for item in raw_data.xpath('p/text()|p/strong/text()')[1:]:
            job_description += item.get() + '\n'

        #print((job_title, company_name, crawled_date, posted_date, location, job_description))


        scraped_info = {
                'job_title' : job_title,
                'company_name' : company_name,
                'crawled_date' : crawled_date,
                'posted_date' : posted_date,
                'location' : location,
                'job_description' : job_description
                        }
        #print(scraped_info)
        # yield scraped_info
        return scraped_info




    def parse (self, response):

        vacancy_selector = '//h3[@class="grid-entry-title entry-title"]/a/@href'

        for link in response.xpath(vacancy_selector):
            # print('i= ', HrSpider.i + 1)
            # print(link.get())
            yield scrapy.Request(url=link.get(), callback=self.vacancy_data)


