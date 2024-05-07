# Data Management Project

This repository contains a project developed during the course of the Master's degree in Data Science

## Description

This project aims, from a generic point of view, to acquire data from different sources, primarly with the implementation of scraping techniques or APIs, and store it in a database in order to perform queries. More specifically, this project wants to identify the most popular anime productions between Italy and the rest of the world, as well as evaluating their common characteristics and their differences.
\
To reach this goal, it has been developed the following workflow:  

* **Data collection**: three main sources have been taking into account, two popular italian streaming websites, AnimeWorld and AnimeUnity, and one popular international website,
  i.e. MyAnimeList; scraping and APIs haver been used to acquire data from this sources.
* **Data preparation**: some data cleaning operations to remove errors and inconsistencies.
* **Database design**: given the nature of the data, which is constant through time, a RDBMS has been chosen (MySQL); in this phase, moreover, the structure of the tables
  has been set, as well as the internal and external keys.
* **Data cleaning**: others data cleaning operations, this time managing missing values and incorrect data.
* **Results**: once the clean data is stored into the database, we proceed to formulate queries to answer the question proposed at the beginning of the project.

## Repository structure

This repository is structured as follows:

```
.
├── README.md
├── data integration                    # scripts used to integrate data collected from different sources
│   ├── dataIntegrationAnimeUnity.py     # integration between AnimeUnity data and the record created from the integration between AnimeWorld and MyAnimeList 
│   └── dataIntegrationAnimeWorld.py     # integration between AnimeWorld and MyAnimeList scraped data
├── progettoDatabase.sql                # database obtained as results of the scraping and data integration operations
├── project presentation.pdf            # slides explaining briefly the results and the solutions implemented
├── project report.pdf                  # detailed LaTex report about the work done                  
└── scraping scripts                    # scripts about the scraping code implemented
    ├── ScrapyAnimeWorld.py              # scraping script for AnimeWorld
    ├── ScrapyMyAnimeList.py             # scraping script for MyAnimeList
    └── apiAnimeUnity.py                 # scraping script for AnimeUnity
```

