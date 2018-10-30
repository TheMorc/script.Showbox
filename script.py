import xbmc
import sys
if sys.argv[0] == '':
    xbmc.executebuiltin('Notification(Showbox,It doesn\'t do anything here.)')
elif sys.argv[1] == 'toggle':
    if xbmc.Player().isPlaying() == 1:
        xbmc.executebuiltin('Stop')
        xbmc.executebuiltin('PlayerControl(Stop)')
    xbmc.executebuiltin('CECToggleState')
    xbmc.executebuiltin('ActivateScreensaver')
