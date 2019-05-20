# -*- coding: utf-8 -*-
import xlsxwriter
from hrfoecast.items import HrfoecastItem


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
    workbook = xlsxwriter.Workbook('Expenses01.xlsx')
    worksheet = workbook.add_worksheet()

    def __init__(self):
        col = 0
        for item_col in HrfoecastItem.fields:
            XlsxPipeline.worksheet.write(XlsxPipeline.row, col, item_col)
            col += 1

    def process_item(self, item, spider):
        print(item)
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
        XlsxPipeline.workbook.close()
