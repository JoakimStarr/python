#!/usr/bin/env python
# coding=utf-8
create a unique seesion id
    input - string to use as part of the data used to create the seeion key
        Although not required, it is beset if this includes some unique
        data from the site,such as it's IP address or other environment
            information. For ZOPE applications, pass in the entire ZOPE "REQUEST"
            object

def makeSessionID(st):
    import md5, time, base64, string
    m =md5.new()
    m.update('this is a test the emergency broadcasthing system')
    m.update(str(time.time()))
    m.update(str(st))
    return string.replace(base64.encodestring(m.digest())[:-3],'/','/span>)

def makeSessionID_nostring(st)
    import md5, time, base64 
    m = md5.new()
    m.update(str(time.time()))
    m.update(str(st))
    return base64.encodestring(m.digest())[:-3].replace('/','/span>)

sessionid = akeSessionID("this my seesionID)
print(sessionid)
