#!/usr/bin/env python

import re
import sys
import json
import urllib2


def make_url(settings, service, path):
    """Convert parts into a complete URL (with path) for a Spinnaker service"""

    hostname = service
    if "all.namespace" in settings:
        hostname += "-%s" % settings['all.namespace']

    url = "http://%s.%s%s" % (hostname, settings['deck.domain'], path)

    return url

def process_template(artifact_file, template, service, path):
    """Merge a Spring Cloud Spinnaker JSON data file with a template."""

    settings = json.load(open(artifact_file))

    output = ""

    with open(template) as input:
        for line in input.readlines():
            new_line = line
            for key in settings:
                print "Looking for {{%s}} to swap in %s" % (key, settings[key])
                new_line = re.sub("{{%s}}" % key, str(settings[key]), new_line)
            output += new_line

    print "Updated to:"
    print
    print output

    url = make_url(settings, service, path)

    return (output, url)

def post((data_string, url)):
    """
    Post the data to the designated URL

    NOTE: Due to this being a script, can't use 3rd party modules.
    """

    request = urllib2.Request(url)
    request.add_header('Content-Type', 'application/json')

    try:
        response = urllib2.urlopen(request, data_string)
        print response.read()
    except urllib2.URLError as e:
        print "Unable to complete request to %s due to %s" % (e.url, e.read())


if __name__ == "__main__":
    if len(sys.argv) < 5:
        print
        print "Usage: %s <spinnaker.json file> <template file> <service> <path>" % sys.argv[0]
        print
    else:
        post(process_template(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]))