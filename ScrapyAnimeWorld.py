# -*- coding: utf-8 -*-
from typing import Any, Union

import scrapy

class ListAnimeWorld(scrapy.Spider):
    name = "listAnimeWorld"
    allowed_domains = ["www.animeworld.tv"]
    start_urls = [
        'https://www.animeworld.tv/az-list',
    ]

    def parse(self, response):
        for anime_link in response.css(".items .item a ::attr(href)").extract():
            yield scrapy.Request(response.urljoin(anime_link), callback=self.parse_list_anime_page)

        next_page = response.css("#go-next-page.disabled").extract_first()
        if not next_page:
            next_page = response.css("#go-next-page ::attr(href)").extract_first()
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    def parse_link_url(self, response):
        p = response.css("#player video source").get()
        return p

    def parse_list_anime_page(self, response):
        item: dict[str, Union[Union[list[Any], list[dict[Any, Union[str, Any]]]], Any]] = {}
        array_episodi = []
        array_genere = []

        for anime in response.css("#animeId .widget-body div.server.active  li.episode a "):
            id_anime = anime.attrib['data-id']
            episodio = {anime.attrib['data-episode-num']: "https://www.animeworld.tv/api/episode" 
                                                          "/serverPlayerAnimeWorld?id=" + id_anime}
            array_episodi.append(episodio)

        for genere in response.css("#main div  div.widget.info  div  div:nth-child(1)  div.info.col-md-9  div.row  "
                                   "dl:nth-child(1)  dd:nth-child(12) a ::text"):
            array_genere.append(genere.get())

        item["Data_uscita"] = response.css("#main div div.widget.info div div:nth-child(1) div.info.col-md-9 div.row "
                                           "dl:nth-child(1) dd:nth-child(6)").get()
        item["Image_url"] = response.css("#thumbnail-watch img").get()
        item["MyAnimeList"] = response.css("#mal-button ::attr(href)").extract_first()
        item["AniList"] = response.css("#anilist-button ::attr(href)").extract_first()
        item["Stagione"] = response.css("#main div div.widget.info div div:nth-child(1) div.info.col-md-9 div.row "
                                        "dl:nth-child(1) dd:nth-child(8) a ::text").get()
        item["Categoria"] = response.css("#main  div  div.widget.info  div  div:nth-child(1) div.info.col-md-9 "
                                         "div.row dl:nth-child(1) dd:nth-child(2)").get()
        item["Generi"] = array_genere
        item["Rating"] = response.css("#main div  div.widget.info  div  div:nth-child(1)  div.info.col-md-9  div.row  "
                                      "dl:nth-child(2) dd.rating #average-vote ::text").get()
        item["Visualizzazioni"] = response.css("#main div  div.widget.info  div  div:nth-child(1)  div.info.col-md-9  div.row  "
                                      "dl:nth-child(2) dd:nth-child(10) ::text").get()
        item['Description'] = response.css('#main .desc ::text').extract_first()
        item["Link-ep"] = array_episodi
        item["Title"] = response.css('#main div.widget.info div.head h2 ::text').extract_first()
        item["Keywords"] = response.css("#tagsReload ::text").extract_first()
        yield item
