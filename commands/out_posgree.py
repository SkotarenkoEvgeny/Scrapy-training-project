import xlwt

from sqlalchemy.orm import sessionmaker
from hrfoecast.models import db_connect

from scrapy.commands import ScrapyCommand
from scrapy.utils.project import get_project_settings

class Out_posgreeCommand(ScrapyCommand):

    def run(self, args, opts):
        '''
        the comand for crawls all spiders
        '''

        engine = db_connect()
        Session = sessionmaker(bind=engine)

        row_xlsx = 0
        col_xlsx = 0
        workbook = xlwt.Workbook()
        worksheet = workbook.add_sheet('vacancy', cell_overwrite_ok=True)
        heading = ('namber', 'job_title', 'company_name', 'location', 'crawled_date', 'posted_date', 'job_description')
        for item_col in heading:
            worksheet.write(0, col_xlsx, item_col)
            col_xlsx += 1

        result = engine.execute("select * from vacancy")

        for row in result:
            row_xlsx += 1
            worksheet.write(row_xlsx, 0, row[0])
            worksheet.write(row_xlsx, 1, row[1])
            worksheet.write(row_xlsx, 2, row[2])
            worksheet.write(row_xlsx, 3, row[3])
            worksheet.write(row_xlsx, 4, row[4])
            worksheet.write(row_xlsx, 5, row[5])
            worksheet.write(row_xlsx, 6, row[6])
            print(row)
            print(type(row))
            print(len(row))

        workbook.save('vacancy_from_DB.xlsx')