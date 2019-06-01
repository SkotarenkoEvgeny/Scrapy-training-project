#! -*- coding: utf-8 -*-

"""
save to a database (postgres).
Database models part - defines table for storing scraped data.
Direct run will create the table.
"""

from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from scrapy.utils.project import get_project_settings

settings = get_project_settings()

DeclarativeBase = declarative_base()


def db_connect():
    """Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance.
    """
    return create_engine(URL(**settings.getdict('DATABASE')))


def create_deals_table(engine):
    """"""
    DeclarativeBase.metadata.create_all(engine)


class Deals(DeclarativeBase):
    """Sqlalchemy deals model"""
    __tablename__ = "vacancy"

    id = Column(Integer, primary_key=True)
    job_title = Column('job_title', String, nullable=True)
    company_name = Column('company_name', String, nullable=True)
    location = Column('location', String, nullable=True)
    crawled_date = Column('crawled_date', String, nullable=True)
    posted_date = Column('posted_date', String, nullable=True)
    job_description = Column('job_description', String, nullable=True)
    job_url = Column('job_url', String, nullable=True)
