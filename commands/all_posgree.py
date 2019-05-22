import scrapy
from scrapy.commands import ScrapyCommand
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess


class All_posgreeCommand(ScrapyCommand):

    def run(self, args, opts):
        '''
        the comand for srawls all spiders
        '''

        setting = get_project_settings()

        setting.set('ITEM_PIPELINES',
                    {'hrfoecast.pipelines.PosgreePipeline': 300})

        process = CrawlerProcess(setting)

        for spider_name in process.spiders.list():
            print("Running spider %s" % (spider_name))
            process.crawl(
                spider_name)

        process.start()
