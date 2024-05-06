# Data Management Project

This repository contains a project developed during the course of the Master's degree in Data Science

## Description

## Repository structure

This repository is structured as follows:

```
.
├── README.md
├── data integration                    # scripts used to integrate data collected from different sources
│   ├── dataIntegrationAnimeUnity.py     # integration between AnimeUnity data and the record created from the integration between AnimeWorld and MyAnimeList 
│   └── dataIntegrationAnimeWorld.py     # integration between AnimeWorld and MyAnimeList scraped data
├── env.env                             # 
├── progettoDatabase.sql                # database obtained as results of the scraping and data integration operations
├── project presentation.pdf            # slides explaining briefly the results and the solutions implemented
├── project report.pdf                  # detailed LaTex report about the work done
├── requirements.txt                    # requirements necessary to run the project
└── scraping scripts                    # scripts about the scraping code implemented
    ├── ScrapyAnimeWorld.py              # scraping script for AnimeWorld
    ├── ScrapyMyAnimeList.py             # scraping script for MyAnimeList
    └── apiAnimeUnity.py                 # scraping script for AnimeUnity
```





























Per poter eseguire nuovamente il progetto bisognerebbe prima di tutto installare python >= 3.8

E quindi installare i requisiti
pip install -r requirements.txt

dopodichè modificare il file env.env con i dati del proprio database e quindi poi salvarlo solo come .env

Poi eseguire questi script in questo ordine:

1. python3 apiAnimeUnity.py
2. scrapy runspider apiAnimeUnity.py
3. python3 dataIntegrationAnimeUnity.py
4. python3 dataIntegrationAnimeWorld.py
5. scrapy runspider scrapyMyAnimeList.py
