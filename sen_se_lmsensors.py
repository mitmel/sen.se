#!/usr/bin/env python

# publish your lmsensors data straight to sen.se
# 
# create a config file called sen_se_lmsensors.cfg
# and populate it with:
# [sen_se]
# api_key = YOUR_API_KEY
# [lmsensors]
# LMSENSOR = FEED_ID

from sen_se import SenseDevice
import ConfigParser
import sensors
import urllib2

if __name__=='__main__':
    config = ConfigParser.SafeConfigParser({})
    config.read('sen_se_lmsensors.cfg')

    api_key = config.get('sen_se', 'api_key')

    sensors.init()

    dev = SenseDevice(api_key)

    features = {}
    for chip in sensors.iter_detected_chips():
        for feature in chip:
            id = config.get('lmsensors', feature.label)
            features[id] = feature

    import time
    res = None
    try:
        while True:
            try:
                for id, feature in features.iteritems():
                    print id, feature.get_value()
                    dev.add_value(id, feature.get_value())
                res = dev.publish()
            except urllib2.HTTPError, e:
                print "".join(e.readlines())
                print "waiting for next event..."

            time.sleep(30)
    finally:
        sensors.cleanup()

