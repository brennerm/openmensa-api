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
    def __make_json_request(path, params=None):
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
    def get_all(method, *args, **kwargs):
        res = []
        kwargs['page'] = 1

        while True:
            response = method(*args, **kwargs)

            if not response:
                break

            res.extend(response)
            kwargs['page'] += 1

        return res

    @staticmethod
    def canteens(near_lat_lng=None, near_dist=None, canteen_ids=None, has_coords=None, page=None, limit=None):
        """Get a list of canteens
        :param near_lat_lng: position 2 tuple to define search center, example (52.39, 13.12)
        :param near_dist: search distance in km for near_lat_lng, default: 10
        :param canteen_ids: list of canteen ids to query
        :param has_coords: whether to return canteens with or without coordinations
        :param page: page index to query
        :param limit: restrict response to this amount of results
        """
        params = {}

        if near_lat_lng:
            params['near[lat]'], params['near[lng]'] = near_lat_lng

        if near_dist:
            params['near[dist]'] = near_dist

        if canteen_ids:
            params['ids'] = ','.join([str(ident) for ident in canteen_ids])

        if has_coords is not None:
            params['hasCoordinates'] = has_coords

        if page:
            params['page'] = page

        if limit:
            params['limit'] = limit

        return OpenMensa.__make_json_request('canteens', params)

    @staticmethod
    def canteen(canteen_id):
        """Get a single canteen identified by canteen_id

        :param canteen_id: id of canteen to query
        """
        return OpenMensa.__make_json_request(
            'canteens/{}'.format(canteen_id)
        )

    @staticmethod
    def canteen_days(canteen_id, start_date=None, page=None, limit=None):
        """Get all canteen days

        :param canteen_id: id of canteen to query
        :param start_date: the date to begin with
        :param page: page index to query
        :param limit: restrict response to this amount of results
        """

        params = {}
        if start_date:
            params['start'] = start_date

        if page:
            params['page'] = page

        if limit:
            params['limit'] = limit

        return OpenMensa.__make_json_request(
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
    def meals_per_day(canteen_id, date, page=None, limit=None):
        """Get all meals
        :param canteen_id: id of canteen to query
        :param date: date to get the meals for, format: YYYY-MM-DD
        :param page: page index to query
        :param limit: restrict response to this amount of results
        """
        params = {}

        if page:
            params['page'] = page

        if limit:
            params['limit'] = limit

        return OpenMensa.__make_json_request(
            'canteens/{}/days/{}/meals'.format(
                canteen_id,
                date
            ),
            params
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
