#!/usr/bin/env python

import json
import urllib2

class SenseDevice:
    base_url = 'http://api.sen.se/events/'
    def __init__(self, api_key):
        self.api_key = api_key

    def publish(self, feed_id, value):
        req = urllib2.Request(self.base_url)
        req.add_header('sense_key', self.api_key)
        req.add_header('content-type', 'application/json')

        data = {
                'feed_id': feed_id,
                'value': value
                }
        req.add_data(json.dumps(data).encode('utf-8'))
        res = urllib2.urlopen(req)
        return res

