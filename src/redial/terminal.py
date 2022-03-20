import dbus 
import os 

envs = os.environ 


def setTabTitle(local, remote):
    if 'KONSOLE_DBUS_SERVICE' in envs:
        konsole_dbus_service = envs['KONSOLE_DBUS_SERVICE']
        konsole_dbus_session = envs['KONSOLE_DBUS_SESSION']
        bus = dbus.SessionBus()
        konsole_obj = bus.get_object(konsole_dbus_service, konsole_dbus_session)
        konsole_obj.setTabTitleFormat(0, local)
        konsole_obj.setTabTitleFormat(1, remote)





