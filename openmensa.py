#!/usr/bin/env python3
import json
import os
import urllib.request
import urllib.parse


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
            param_string += urllib.parse.urlencode(params)
        print(url + param_string)
        req = urllib.request.urlopen(
            url + param_string
        )

        return json.loads(
            req.read().decode('utf-8')
        )

    @staticmethod
    def canteens(near_lat_lng=None, near_dist=None, ids=None, has_coords=None):
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
    def canteen(ident):
        return OpenMensa.make_json_request(
            'canteens/{}'.format(ident)
        )

    @staticmethod
    def canteen_days(ident, start_date=None):
        params = {}
        if start_date:
            params['start'] = start_date

        return OpenMensa.make_json_request(
            'canteens/{}/days'.format(ident),
            params
        )

    @staticmethod
    def canteen_day(ident, date):
        return OpenMensa.make_json_request(
            'canteens/{}/days/{}'.format(
                ident,
                date
            ),
        )

    @staticmethod
    def meals_per_day(ident, date):
        return OpenMensa.make_json_request(
            'canteens/{}/days/{}/meals'.format(
                ident,
                date
            ),
        )

    @staticmethod
    def meal(canteen_id, date, meal_id):
        return OpenMensa.make_json_request(
            'canteens/{}/days/{}/meals/{}'.format(
                canteen_id,
                date,
                meal_id
            ),
        )