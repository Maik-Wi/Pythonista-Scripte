import sound
sound.load_effect('Powerup_2')
import clipboard
import urllib2
import json

kurzurl = urllib2.quote(clipboard.get())

def shorten_url(long_url):
     username = 'USERNAME'
     apikey = 'API-KEY'
     bitly_url = "http://api.bit.ly/v3/shorten?login=%s&apiKey=%s&longUrl=%s" %(username, apikey, long_url)
     r = urllib2.Request(bitly_url)
     opener = urllib2.build_opener()
     f = json.loads(opener.open(r).read())
     short_url = f['data']['url']
     return short_url

kurz = shorten_url(kurzurl)

clipboard.set(kurz)
print shorten_url(kurzurl)
sound.play_effect('Powerup_2')
