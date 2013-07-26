# -*- coding: utf-8 -*-                                               
print '''
****************************************
*      Runtastic To DayOn Exporter     *
****************************************'''
import clipboard
import console
import urllib
import webbrowser

mytext = clipboard.get()
mytext = mytext.encode('ascii', 'ignore')
mytext = mytext.replace('Ich habe gerade ein Workout mit der Runtastic iPhone App abgeschlossen. Versuch doch meine Zeit zu schlagen.', ' ')
mytext = mytext.replace('Sportart: ', '* Sportart: ')
mytext = mytext.replace('Distanz: ', '* Distanz: ')
mytext = mytext.replace('Dauer: ', '* Dauer: ')                                                                                        
mytext = mytext.replace('Wann: ', '* Wann: [')
mytext = mytext.replace('Schau dir meine Aktivitt an ', '](')
mytext = mytext.replace('Schau auch auf meinem Profil vorbei http://www.runtastic.com/users/11001217.', ')')                              
mytext = mytext.replace('Hol dir kostenlos die Runtastic iPhone App http://www.runtastic.com/apps/iphone.', ' ')
mytext = '## Mein Runtestic Jogging-Log ' + mytext + '#runstatic #sport #tracking'
mytext = mytext.encode('utf-8')
mytext = urllib.quote(mytext, safe='')
mytext = mytext.replace('%20%0A%0A%2A%20', '%0A')
mytext = mytext.replace('%0A%0A%5D%28http', '%5D%28http')
mytext = mytext.replace('.%0A%29%0A%0A%0A%20', '%29%0A%0A')

webbrowser.open("dayone://post?entry=" + mytext)
