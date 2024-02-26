Per poter Rieseguire il progetto bisognerebbe prima di tutto installare python >= 3.8

E quindi installare i requirements
pip install -r requirements.txt

dopodichè modificare il file env.env con i dati del proprio database e quindi poi salvarlo solo come .env

Poi eseguo questi script in questo ordine:

1. python3 apiAnimeUnity.py
2. scrapy runspider apiAnimeUnity.py
3. python3 dataIntegrationAnimeUnity.py
4. python3 dataIntegrationAnimeWorld.py
5. scrapy runspider scrapyMyAnimeList.py