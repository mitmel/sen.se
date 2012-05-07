#!/usr/bin/env python

import json
import urllib2

class SenseDevice:
    base_url = 'http://api.sen.se/events/'
    data = []

    def __init__(self, api_key):
        self.api_key = api_key

    def add_value(self, feed_id, value):
        self.data.append({
                'feed_id': feed_id,
                'value': value
                })


    def publish(self):
        req = urllib2.Request(self.base_url)
        req.add_header('sense_key', self.api_key)
        req.add_header('content-type', 'application/json')

        req.add_data(json.dumps(self.data).encode('utf-8'))
        res = urllib2.urlopen(req)
        return res

