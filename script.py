import xbmc
import urlparse
import sys
import time

if sys.argv[1] == 'toggle':
	xbmc.executebuiltin('Stop')
	xbmc.executebuiltin('PlayerControl(Stop)')
	print 'Stopped playing media'
	xbmc.executebuiltin('CECToggleState')
	print 'Toggled TV on/off.'
	xbmc.executebuiltin('ActivateScreensaver')
	print 'Activated Screensaver.'
	print 'everything is done, master!'
print 'i think this is end of the if'

print len(sys.argv)
print str(sys.argv)
print str(sys.argv[0])
print str(sys.argv[1])