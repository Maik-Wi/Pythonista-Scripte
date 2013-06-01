# -*- coding: utf-8 -*-                                               
import clipboard
import console
import urllib
import webbrowser

runninglog = clipboard.get()
runninglog = runninglog.encode('ascii', 'ignore')
runninglog = runninglog.replace('Ich habe gerade ein Workout mit der runtastic iPhone App abgeschlossen. Versuch doch meine Zeit zu schlagen.', ' ')
runninglog = runninglog.replace('Sportart: ', '* Sportart: ')
runninglog = runninglog.replace('Distanz: ', '* Distanz: ')
runninglog = runninglog.replace('Dauer: ', '* Dauer: ')                                                                                        
runninglog = runninglog.replace('Wann: ', '* Wann: [')
runninglog = runninglog.replace('Schau dir meine Aktivitt an ', '](')
runninglog = runninglog.replace('Schau auch auf meinem Profil vorbei http://www.runtastic.com/users/11001217.', ')')                              
runninglog = runninglog.replace('Hol dir kostenlos die runtastic iPhone App http://www.runtastic.com/apps/iphone.', ' ')
runninglog = '## Mein Runtestic Jogging-Log ' + runninglog + '#runstatic #sport #tracking'
runninglog = runninglog.encode('utf-8')
runninglog = urllib.quote(runninglog, safe='')
runninglog = runninglog.replace('%20%0A%0A%2A%20', '%0A')
runninglog = runninglog.replace('%0A%0A%5D%28http', '%5D%28http')
runninglog = runninglog.replace('.%0A%29%0A%0A%0A%20', '%29%0A%0A')

webbrowser.open("dayone://post?entry=" + runninglog)
