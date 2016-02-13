# Pythonista
from objc_util import *

UIDevice = ObjCClass('UIDevice')
CUR_DEVICE = UIDevice.currentDevice()

###

def battery_level():
	
	CUR_DEVICE.setBatteryMonitoringEnabled_(True)
	battery_percent = CUR_DEVICE.batteryLevel() * 100
	CUR_DEVICE.setBatteryMonitoringEnabled_(False)
	# return '%0.1f%%' % battery_percent
	return '%d %%' % int(battery_percent)

def device_name():
	return str(CUR_DEVICE.name())
	
def system_version():
	return str(CUR_DEVICE.systemVersion())
	
def device_uuid():
	return str(CUR_DEVICE.identifierForVendor()).split()[2]

def all_info():
	
	all_dict = {'device_name': device_name(),
							'battery_level': battery_level(),
							'system_version': system_version(),
							'uuid': device_uuid()}
							
	return all_dict


def	main():
	print battery_level()
	print device_name()
	print system_version()
	print device_uuid()
	
if __name__ == '__main__':
	main()