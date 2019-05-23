# -*- coding: utf-8 -*-
import xlwt

from hrfoecast.items import HrfoecastItem

from sqlalchemy.orm import sessionmaker
from hrfoecast.models import Deals, db_connect, create_deals_table


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class HrfoecastPipeline(object):
    def process_item(self, item, spider):
        return item


class XlsxPipeline(object):
    """
    ctreate xlsx file in spiders folder
    """
    row = 0
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('vacancy', cell_overwrite_ok=True)
    call_1 = 0

    def __init__(self):
        col = 0
        for item_col in HrfoecastItem.fields:
            XlsxPipeline.worksheet.write(0, col, item_col)
            col += 1

    def process_item(self, item, spider):
        """
        save data to xlsx file
        """
        XlsxPipeline.row += 1
        XlsxPipeline.worksheet.write(XlsxPipeline.row, 0, item['company_name'])
        XlsxPipeline.worksheet.write(XlsxPipeline.row, 1, item['crawled_date'])
        XlsxPipeline.worksheet.write(XlsxPipeline.row, 2,
                                     item['job_description'])
        XlsxPipeline.worksheet.write(XlsxPipeline.row, 3, item['job_title'])
        XlsxPipeline.worksheet.write(XlsxPipeline.row, 4, item['location'])
        XlsxPipeline.worksheet.write(XlsxPipeline.row, 5, item['posted_date'])

        return item

    def __del__(self):
        XlsxPipeline.workbook.save('vacancy.xlsx')


class PosgreePipeline(object):
    """
    write info to posgree database
    """

    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates deals table.
        """
        engine = db_connect()
        create_deals_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """
        Save deals in the database.
        This method is called for every item pipeline component.
        """
        session = self.Session()
        deal = Deals(**item)

        try:
            session.add(deal)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item
