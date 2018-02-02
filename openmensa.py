#!/usr/bin/env python
import json
import os

try:
    from urllib.parse import urlparse, urlencode
    from urllib.request import urlopen, Request
    from urllib.error import HTTPError
except ImportError:
    from urlparse import urlparse
    from urllib import urlencode
    from urllib2 import urlopen, Request, HTTPError


class OpenMensa:
    ENDPOINT = 'http://openmensa.org/api/v2'

    @staticmethod
    def make_json_request(path, params=None):
        url = os.path.join(
            OpenMensa.ENDPOINT,
            path
        )

        param_string = '?'
        if params:
            param_string += urlencode(params)
        req = urlopen(
            url + param_string
        )

        return json.loads(
            req.read().decode('utf-8')
        )

    @staticmethod
    def canteens(near_lat_lng=None, near_dist=None, canteen_ids=None, has_coords=None, limit=10):
        """Get a list of canteens
        :param near_lat_lng: position 2 tuple to define search center, example (52.39, 13.12)
        :param near_dist: search distance in km for near_lat_lng, default: 10
        :param canteen_ids: list of canteen ids to query
        :param has_coords: whether to return canteens with or without coordinations
        """
        params = {}

        if near_lat_lng:
            params['near[lat]'], params['near[lng]'] = near_lat_lng

        if near_dist:
            params['near[dst]'] = near_dist

        if ids:
            params['ids'] = ','.join([str(ident) for ident in ids])

        if has_coords is not None:
            params['hasCoordinates'] = has_coords

        return OpenMensa.make_json_request('canteens', params)

    @staticmethod
    def canteen(canteen_id):
        """Get a single canteen identified by canteen_id

        :param canteen_id: id of canteen to query
        """
        return OpenMensa.__make_json_request(
            'canteens/{}'.format(canteen_id)
        )

    @staticmethod
    def canteen_days(canteen_id, start_date=None):
        """Get all canteen days

        :param canteen_id: id of canteen to query
        :param start_date: the date to begin with
        """

        params = {}
        if start_date:
            params['start'] = start_date

        return OpenMensa.make_json_request(
            'canteens/{}/days'.format(canteen_id),
            params
        )

    @staticmethod
    def canteen_day(canteen_id, date):
        """Get single canteen day

        :param canteen_id: id of canteen to query
        :param date: the date to query
        """
        return OpenMensa.__make_json_request(
            'canteens/{}/days/{}'.format(
                canteen_id,
                date
            ),
        )

    @staticmethod
    def meals_per_day(canteen_id, date):
        """Get all meals
        :param canteen_id: id of canteen to query
        :param date: date to get the meals for, format: YYYY-MM-DD
        """
        return OpenMensa.__make_json_request(
            'canteens/{}/days/{}/meals'.format(
                canteen_id,
                date
            ),
        )

    @staticmethod
    def meal(canteen_id, date, meal_id):
        """Get single meal
        :param canteen_id: id of canteen to query
        :param date: date to get the meal for, format: YYYY-MM-DD
        :param meal_id: id of meal to query
        """
        return OpenMensa.__make_json_request(
            'canteens/{}/days/{}/meals/{}'.format(
                canteen_id,
                date,
                meal_id
            ),
        )