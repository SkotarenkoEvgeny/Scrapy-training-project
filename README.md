The program hrforecast can scrapy the information from:
 	HRForecast's job vacancies (https://www.hrforecast.de/career/)
	and Gazprom's job vacancies (https://www.gazpromvacancy.ru/jobs/)

In this program used user agent and proxy pool

For the inctallation you can download this repositori and run in curent folder the comand:

	pip install -r requirements.txt

After succesful instalation you can use folloving commands in the bash:
	
	scrapy all_posgree   -  save the data to PSQL table 'vacancy' forom hrforecast and gazprom at the same time

	scrapy all_xlsx   -  save the data to xlsx file 'vacancy' forom hrforecast and gazprom at the same time

You can use the in-build scrapy commends for exporting to following formats: JSON, JSON lines, CSV, XML
For example: scrapy crawl gazprom -o temp.csv
