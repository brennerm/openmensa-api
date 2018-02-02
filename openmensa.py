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
    def canteen(canteen_id):
        return OpenMensa.make_json_request(
            'canteens/{}'.format(canteen_id)
        )

    @staticmethod
    def canteen_days(canteen_id, start_date=None):
        params = {}
        if start_date:
            params['start'] = start_date

        return OpenMensa.make_json_request(
            'canteens/{}/days'.format(canteen_id),
            params
        )

    @staticmethod
    def canteen_day(canteen_id, date):
        return OpenMensa.make_json_request(
            'canteens/{}/days/{}'.format(
                canteen_id,
                date
            ),
        )

    @staticmethod
    def meals_per_day(canteen_id, date):
        return OpenMensa.make_json_request(
            'canteens/{}/days/{}/meals'.format(
                canteen_id,
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