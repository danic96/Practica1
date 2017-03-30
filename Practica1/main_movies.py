#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :

import sys
import json
import requests
from time import sleep

from Aplicacio.models import Pelicula, Personatge, Relacions

api_key = None
time = 0


class MoviesClient(object):
    """docstring for MoviesClient."""

    url_base = "http://comicvine.gamespot.com/api/characters/?api_key="
    sufix = ("&format=json" +
             "&field_list=id,name,release_date,runtime,api_detail_url&offset=")

    def __init__(self, api_key):
        """Inicialitzar la clau."""
        super(MoviesClient, self).__init__()
        self.api_key = api_key
        self.offset = 0

    def requestData(self, situation, url):
        u"""Baixar-se la web."""
        base_urls = {
            "movies": "http://comicvine.gamespot.com/api/movies/?api_key=",
            "characters": "http://comicvine.gamespot.com/api/characters/" +
                          "?api_key=",
            "publishers": "http://comicvine.gamespot.com/api/publishers/" +
                          "?api_key=",
            "character": "",
            "movie": ""
        }
        correcte = False
        while not correcte:
            user_agent = {'User-agent': 'Mozilla/5.0'}
            if situation != "character" and situation != "movie":

                url = base_urls[situation] + self.api_key + self.sufix + \
                     str(self.offset)

            elif situation == "character":
                url = url + "?api_key=" + self.api_key + "&format=json" + "&field_list=id,name,gender,description"
            else:
                url = url + "?api_key=" + self.api_key + "&format=json"

            resultat = requests.get(url, headers=user_agent)
            codi = resultat.status_code

            if codi == 200:
                correcte = True
            elif codi == -1:
                sleep(time)
            elif codi == 504:
                print "GATEWAY TIME-OUT"
                print url
                return None
            elif codi == 401:
                print "PROBLEMA DE AUTENTIFICACIO"
            else:
                print codi
                print "ERROR!!!"
                print sys.exc_info()
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
                try:
                    str(result["runtime"])
                    if result["release_date"] is None:
                        print "Release_date es None"
                        print result["id"]
                        result["release_date"] = "null"
                    pelicula = Pelicula(id=result["id"],
                                        nom=result["name"].encode("utf-8"),
                                        productors='null',
                                        data=result["release_date"].encode("utf-8"),
                                        durada=result["runtime"],
                                        detail_url=result["api_detail_url"])
                    pelicula.save()
                except:
                    if result["release_date"] is None:
                        print "Release_date es None"
                        print result["id"]
                        result["release_date"] = "null"

                    pelicula = Pelicula(id=result["id"],
                                        nom=result["name"].encode("utf-8"),
                                        productors='null',
                                        data=result["release_date"].encode("utf-8"),
                                        durada=0)
                    pelicula.save()

            if self.offset >= limit:
                final = True
            else:
                sleep(time)
                self.offset += 100

        return resultat

    def characters(self):
        lista = Pelicula.objects.values('detail_url', 'id')
        for elemento in lista:
            print elemento
            # sleep(60)
            # print elemento["detail_url"]
            data = self.requestData("movie", elemento["detail_url"])
            jsondata = json.loads(data)

            print jsondata["results"]["name"].encode('utf-8')
            # print jsondata["results"]["characters"][0].keys()
            i = 1
            for character in jsondata["results"]["characters"]:
                # print "   " + character["name"].encode('utf-8')
                character_data = self.requestData("character", character["api_detail_url"])
                character_jsondata = json.loads(character_data)
                # print character_jsondata["results"]["id"]
                result = character_jsondata["results"]
                if result["description"] is None:
                    character = Personatge(id=result["id"],
                                           nom=result["name"].encode("utf-8"),
                                           genere=result["gender"],
                                           descripcio="null",
                                           id_pelicula=elemento["id"])
                                 
                else:
                    character = Personatge(id=result["id"],
                                           nom=result["name"].encode("utf-8"),
                                           genere=result["gender"],
                                           descripcio=result["description"].encode("utf-8"),
                                           id_pelicula=elemento["id"])
                character.save()
                relacions = Relacions(id_pelicula=elemento["id"],
                                      id_personatge=result["id"])
                relacions.save()
                print "   " + str(i) + "-ESCRITO"
                i += 1

def menu_inicial(api_key):

    key_file = open('api_key', 'r')
    api_key = key_file.read().replace('\n', '')

    mc = MoviesClient(api_key)
    print api_key

    numero = int(input("Donam 1 per movies, 2 per characters o 3 " +
                       "per publishers: "))
    if numero == 1:
        mc.movies()
    elif numero == 2:
        mc.characters()
    elif numero == 3:
        mc.publishers()


if __name__ == "__main__":
    menu_inicial(api_key)

else:
    menu_inicial(api_key)
