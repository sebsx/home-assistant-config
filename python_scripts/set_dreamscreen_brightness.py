#####################################################
# Set Dreamscreen brightness by converting 256 levels to 100   #
#####################################################

###### Service Call Parameters #######

BRIGHTNESS = int((float(data.get("brightness")))/2.56)

###### Global Variables #######

logger.debug("RGB hex color is: %s",BRIGHTNESS) 
hass.services.call("dreamscreen", "set_brightness", {"entity_id" : "dreamscreen.living_room_tv", "brightness" : BRIGHTNESS}, False)
