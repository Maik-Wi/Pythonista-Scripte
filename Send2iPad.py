print '''
****************************************
*            Send To Phone             *
****************************************'''
print "lade httplib..."
import httplib
print "lade urllib..."
import urllib
print "lade console..."
import console
print "lade Clipboard..."
import clipboard
print "laden der Bibliotheken abgeschlossen"

# Hier musst du nur deinen User Key eintragen
userkey = '_DEIN_USER_KEY_'


if numArgs < 1:  
    console.show_activity()
    text = clipboard.get()
    console.hide_activity()
else:
    text = sys.argv[1]
    
  	
conn = httplib.HTTPSConnection("api.pushover.net:443")
text = console.input_alert('Text', 'Gib hier dein Text ein.')
conn.request("POST", "/1/messages.json",
urllib.urlencode({
           "token": "iyQE2RmQZkqBvTSJBxRUYYAedmASXz",
           "user": userkey,
           "message": text,
}), { "Content-type": "application/x-www-form-urlencoded" })
conn.getresponse()    

print "Push Nachricht gesendet"
