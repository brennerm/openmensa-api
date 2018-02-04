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
    """Python wrapper for OpenMensa API v2"""

    __ENDPOINT = 'http://openmensa.org/api/v2'

    @staticmethod
    def __make_json_request(path, params=None):
        url = os.path.join(
            OpenMensa.__ENDPOINT,
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
        """Gets all results for given query method

        # Arguments

        method (callable): OpenMensa method, one of: get_canteens, get_canteen_days, get_meals_by_day
        args (list): positional arguments for method
        kwargs (dict): keyword arguments for method
        """
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
    def get_canteens(near_lat_lng=None, near_dist=None, canteen_ids=None, has_coords=None, page=None, limit=None):
        """Get a list of canteens

        # Arguments

        near_lat_lng (tuple): position 2 tuple to define search center, example (52.39, 13.12)
        near_dist (float): search distance in km for near_lat_lng, default: 10
        canteen_ids (list): list of canteen ids to query
        has_coords (bool): whether to return canteens with or without coordinations
        page (int): page index to query
        limit (int): restrict response to this amount of results
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
    def get_canteen(canteen_id):
        """Get a single canteen identified by canteen_id

        # Arguments

        canteen_id (int): id of canteen to query
        """
        return OpenMensa.__make_json_request(
            'canteens/{}'.format(canteen_id)
        )

    @staticmethod
    def get_canteen_days(canteen_id, start_date=None, page=None, limit=None):
        """Get all canteen days

        # Arguments

        canteen_id (int): id of canteen to query
        start_date (str): the date to begin with
        page (int): page index to query
        limit (int): restrict response to this amount of results
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
    def get_canteen_day(canteen_id, date):
        """Get single canteen day

        # Arguments

        canteen_id (int): id of canteen to query
        date (str): the date to query
        """
        return OpenMensa.__make_json_request(
            'canteens/{}/days/{}'.format(
                canteen_id,
                date
            ),
        )

    @staticmethod
    def get_meals_by_day(canteen_id, date, page=None, limit=None):
        """Get all meals for a specific day

        # Arguments

        canteen_id (int): id of canteen to query
        date (str): date to get the meals for, format: YYYY-MM-DD
        page (int): page index to query
        limit (int): restrict response to this amount of results
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
    def get_meal(canteen_id, date, meal_id):
        """Get single meal

        # Arguments

        canteen_id (int): id of canteen to query
        date (str): date to get the meal for, format: YYYY-MM-DD
        meal_id (int): id of meal to query
        """
        return OpenMensa.__make_json_request(
            'canteens/{}/days/{}/meals/{}'.format(
                canteen_id,
                date,
                meal_id
            ),
        )
