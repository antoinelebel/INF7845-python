#-*- coding: utf-8 -*-
# Creation Date : 2017-02-05
# Created by : Antoine LeBel
class nonConstructionException(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg)
