import xbmc
import sys
if sys.argv[0] == '':
    xbmc.executebuiltin('Notification(Showbox,Actually, it doesn\'t do anything here for now, but i think it will do in the future.)')
elif sys.argv[1] == 'toggle':
    xbmc.executebuiltin('ActivateWindow(busydialognocancel)')
    if xbmc.Player().isPlaying() == 1:
        xbmc.executebuiltin('Stop')
        xbmc.executebuiltin('PlayerControl(Stop)')
        xbmc.sleep(250)
    xbmc.sleep(250)
    xbmc.executebuiltin('ActivateWindow(busydialognocancel)')
    xbmc.sleep(500)
    xbmc.executebuiltin('CECToggleState')
    xbmc.executebuiltin('ActivateScreensaver')
    xbmc.executebuiltin('Dialog.Close(busydialognocancel)')
    
