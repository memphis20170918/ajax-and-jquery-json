import urllib2


def application(env, start_response):
    start_response('200 OK', [
        ('Content-Type','text/plain'),
        ('Access-Control-Allow-Origin', '*'),
        ('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type')
    ])
    res = urllib2.urlopen('https://wtfismyip.com/json').read()
    return [res]
