## About

The program hrforecast can scrapy the information from:
 	HRForecast's job vacancies (https://www.hrforecast.de/career/)
	and Gazprom's job vacancies (https://www.gazpromvacancy.ru/jobs/)

In this program used user agent and proxy pool

## Installation

For the installation you can download this repository and run in a curent folder the command:

	pip install -r requirements.txt

## Usage

#### Basic commands:

After successful installation you can use following commands in the bash:

	scrapy all_posgree   -  will save the data to PSQL table 'vacancy' from hrforecast and gazprom at the same time\

	scrapy all_xlsx   -  will save the data to xlsx file 'vacancy' from hrforecast and gazprom at the same time

You can use the in-build scrapy commends for exporting to following formats: JSON, JSON lines, CSV, XML
For example: scrapy crawl gazprom -o temp.csv

For the viewing the data from Postgres database you can use following commands in the bash:

	scrapy out_posgree  -  will create vacancy_from_DB.xlsx file