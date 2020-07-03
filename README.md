# Data Project README file

![Image](https://techsalesgroup.files.wordpress.com/2016/10/ironhack-logo-negro1.jpg?w=200)

#### Ivan Company

#### Data Analytics Bootcamp - Project module 1


## **Overview**
With this pipeline you can find out the job and the age group to which the people who participated in the survey on "the minimum vital income" belong. 
You also get the percentage of each age group and job over the total.


## **Data**

* [.db Dataset](http://www.potacho.com/files/ironhack/raw_data_project_m1.db)

The dataset is the raw_data_project_m1.db file, with four tables where you can see all the information about the survey. 
The m_aquisiton.py module is responsible for selecting the necessary information in this dataset.


* [API](http://dataatwork.org/data/)

For some reason, the data in some columns is encoded or does not have the same structure, so it is necessary to correct the data first. 
The m_wrangling.py module has this purpose.

For this we will use this API to be able to name the titles of the jobs of the people who participated in the survey.


* [Web Scraping](https://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:Country_codes)

We also need to enrich our database by changing the country code for its full name, for this we will do web scraping 
from the link above in order to obtain a complete list of the names of each country.


## **Insructions**

In order to run it, you will have to indicate:

-p / --path: the path where you have the .db file

-c / --country: the country you want to get results from. You can also put 'All' to get the results of all the countries together.

-u / --unknown: a large number of people whose profession is unknown have participated in the survey. You can include them or not, in the final result.


## **Requirements**
You need to have Python installed with the following libraries:
   - Pandas
    
   - Requests

   - Beautifulsoup4
    
   - Sqlalchemy

You have more information in the file: requirements.txt


### **Folder structure**
```
└── project
    ├── __trash__
    ├── .gitignore
    ├── .env
    ├── requeriments.txt
    ├── README.md
    ├── main_script.py
    ├── notebooks
    │   └──data_1.ipynb
    ├── p_acquisition
    │   ├── __init__.py
    │   └── m_acquisition.py
    ├── p_wrangling
    │   ├── __init__.py
    │   └── m_wrangling.py
    ├── p_analysis
    │   ├── __init__.py
    │   └── m_analysis.py
    ├── p_reporting
    │   ├── __init__.py
    │   └── m_reporting.py
    └── data
        ├── raw
        └── results
```


## **Next steps:**
- We can analyze the results and group them by other values, such as the gender or the location of the person (city or town).

- We can obtain the main reasons for or against the minimum vital income and group them by age, gender, location ...
