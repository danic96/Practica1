#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :

import sys
import json
import requests
from time import sleep

import sys

api_key = None
time = 0


class MoviesClient(object):
    """docstring for MoviesClient."""

    url_base = "http://comicvine.gamespot.com/api/characters/?api_key="
    sufix = "&format=json&offset="

    def __init__(self, api_key):
        """Inicialitzar la clau."""
        super(MoviesClient, self).__init__()
        self.api_key = api_key
        self.offset = 0

    def requestData(self, situation, url):
        u"""Baixar-se la web."""
        base_urls = {
            "movies": "http://comicvine.gamespot.com/api/movies/?api_key=",
            "characters": "http://comicvine.gamespot.com/api/characters/?api_key=",
            "publishers": "http://comicvine.gamespot.com/api/publishers/?api_key=",
            "character": "",
            "movie": ""
        }
        correcte = False
        while not correcte:
            user_agent = {'User-agent': 'Mozilla/5.0'}
            if situation != "character" and situation != "movie":
                url = base_urls[situation] + self.api_key + self.sufix + str(self.offset)
            else:
                url = url + "?api_key=" + self.api_key + "&format=json"
            try:
                resultat = requests.get(url, headers=user_agent)
                codi = resultat.status_code
            except:
                codi = -1
                print "ERROR AL CARREGAR!!!"
                print sys.exc_info()
            if codi == 200:
                correcte = True
            elif codi == -1:
                sleep(time)
            elif codi == 504:
                print "GATEWAY TIME-OUT"
                return None
            else:
                print "ERROR!!!"
                self.offset += 10
                sleep(time)

        return resultat.text

    def movies(self):
        u"""Baixar-se la informació de hourly."""
        final = False
        while not final:
            print self.offset
            data = self.requestData("movies", "")

            jsondata = json.loads(data)
            limit = jsondata["number_of_total_results"]

            resultat = []
            results = jsondata["results"]
            for result in results:
                if result["studios"] is not None:
                    print "   " + result["name"].encode("utf-8")
                    for studio in result["studios"]:
                        print "     " + str(studio["name"])
                        sleep(time)
                    
                    new_url = result["api_detail_url"]
                    data2 = self.requestData("movie", new_url)
                    
                    if data2 is not None:
                        jsondata2 = json.loads(data2)
                        characters = jsondata2["results"]["characters"]
                        if characters is not None:
                            for character in characters:
                                print "       " + character["name"].encode("utf-8") + " - " + str(character["id"])

                            print self.offset
            if self.offset >= limit:
                final = True
            else:
                sleep(time)
                self.offset += 100

        return resultat
        
    def publishers(self):
        u"""Baixar-se la informació de hourly."""
        final = False
        while not final:
            print self.offset
            data = self.requestData("publishers", "")

            jsondata = json.loads(data)
            limit = jsondata["number_of_total_results"]

            resultat = []
            results = jsondata["results"]
            for result in results:
                if result["name"] is not None:
                    print "   "  +  result["name"].encode("utf-8")
                    """
                    for studio in result["studios"]:
                        print "     " + str(studio["name"])
                        sleep(time)
                    
                    new_url = result["api_detail_url"]
                    data2 = self.requestData("movie", new_url)
                    
                    if data2 is not None:
                        jsondata2 = json.loads(data2)
                        characters = jsondata2["results"]["characters"]
                        if characters is not None:
                            for character in characters:
                                print "       " + character["name"].encode("utf-8") + " - " + str(character["id"])

                            print self.offset
                        """
            if self.offset >= limit:
                final = True
            else:
                sleep(time)
                self.offset += 100

        return resultat

    def characters(self):
        u"""Baixar-se la informació de hourly."""
        final = False
        while not final:
            print self.offset
            print "DEMANAT"
            data = self.requestData("characters", "")
            print "  REBUT"

            jsondata = json.loads(data)
            limit = jsondata["number_of_total_results"]

            resultat = []
            results = jsondata["results"]
            for result in results:
                print "   " + result["name"]
                print "   " + str(result["id"])

                new_url = result["api_detail_url"]
                
                data2 = self.requestData("character", new_url)

                if data2 is not None:
                    jsondata2 = json.loads(data2)
                    movies = jsondata2["results"]["movies"]
                    if movies is not None:
                        for movie in movies:
                            print "     " + movie["name"]

                        if self.offset >= limit:
                            final = True
                        else:
                            sleep(time)
            self.offset += 100
        
        return resultat


if __name__ == "__main__":
    if not api_key:
        try:
            api_key = sys.argv[1]
        except IndexError:
            key_file = open('api_key', 'r')
            api_key = key_file.read().replace('\n', '')

    mc = MoviesClient(api_key)
    print api_key
    
    numero = int(input("Donam 1 per movies, 2 per characters o 3 per publishers: "))
    if numero == 1:
        result = mc.movies()
    elif numero == 2:
        result = mc.characters()
    elif numero == 3:
        result = mc.publishers()
