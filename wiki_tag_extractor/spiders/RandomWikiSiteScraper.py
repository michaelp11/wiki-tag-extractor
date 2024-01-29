from typing import Iterable

import scrapy
from scrapy import Request
from bs4 import BeautifulSoup

import wiki_tag_extractor
import random


class RandomWikiSiteScraper(scrapy.Spider):
    name = 'wiki-tag-extractor'

    def __init__(self):
        super(RandomWikiSiteScraper, self).__init__()
        self.numberOfSamples = 10

    def start_requests(self) -> Iterable[Request]:
        for i in range(self.numberOfSamples):
            yield scrapy.Request('https://de.wikipedia.org/wiki/Spezial:Zuf%C3%A4llige_Seite', dont_filter=True)

    def parse(self, response):
        paragraphs = response.css('.mw-content-ltr')

        paragraphs = paragraphs.xpath('//p').getall()

        print(paragraphs)

        # Selecting a random paragraph
        paragraph = random.choice(paragraphs)
        content = BeautifulSoup(paragraph, 'html.parser').get_text().strip().replace('\n', ' ')

        yield wiki_tag_extractor.WikiTagExtractorItem(
            title=response.css('.mw-page-title-main::text').get(),
            paragraph=content,
            tags=response.css('.mw-normal-catlinks ul a::text').getall()
        )

