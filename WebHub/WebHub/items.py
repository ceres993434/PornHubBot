# -*- coding: utf-8 -*-

from scrapy import Item, Field


class PornVideoItem(Item):
    video_title = Field()
    image_url = Field()
    video_duration = Field()
    quality_480p = Field()
    video_views = Field()
    video_rating = Field()
    link_url = Field()
