import xlwt

from sqlalchemy.orm import sessionmaker
from hrfoecast.models import db_connect

from scrapy.commands import ScrapyCommand
from scrapy.utils.project import get_project_settings


class Out_posgreeCommand(ScrapyCommand):

    def run(self, args, opts):
        '''
        the comand for import data from DB to xlsx file
        '''

        engine = db_connect()
        Session = sessionmaker(bind=engine)

        row_xlsx = 0
        col_xlsx = 0
        workbook = xlwt.Workbook()
        worksheet = workbook.add_sheet('vacancy', cell_overwrite_ok=True)
        heading = (
        'number', 'job_title', 'company_name', 'location', 'crawled_date',
        'posted_date', 'job_description', 'job_url')
        for item_col in heading:
            worksheet.write(0, col_xlsx, item_col)
            col_xlsx += 1

        result = engine.execute("select * from vacancy")

        for row in result:
            row_xlsx += 1
            for i in range(len(heading)):
                worksheet.write(row_xlsx, i, row[i])

        workbook.save('vacancy_from_DB.xlsx')
