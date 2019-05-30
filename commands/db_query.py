from scrapy.commands import ScrapyCommand
from scrapy.utils.project import get_project_settings


class Db_queryCommand(ScrapyCommand):

    def __init__(self):

        database_settings = get_project_settings()

