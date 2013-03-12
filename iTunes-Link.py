#Gebaut für Tradedoubler
#affID ist alles vor der iTunes-URL
#affID2 ist alles was nach dem iTunes-Link kommt.
#Beispiel
#I===================== affID ============================I          I=== affID2 ==I
#http://clkde.tradedoubler.com/click?p=23761&a=1998011&url=ITUNES-URL&partnerId=2003

import console
import urllib
import clipboard

origURL = clipboard.get()

affID = "http://clkde.tradedoubler.com/click?p=23761&a=1998011&url="
affID2 = "&partnerId=2003"

affURL = affID + origURL.strip() + affID2

clipboard.set(affURL)
