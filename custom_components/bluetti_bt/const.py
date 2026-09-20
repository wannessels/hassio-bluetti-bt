"""Constants for the Bluetti BT integration."""

DOMAIN = "bluetti_bt"
MANUFACTURER = "Bluetti"

CONF_OPTIONS = "options"

DATA_COORDINATOR = "coordinator"
DATA_LOCK = "lock"

# Hold the BLE link open between polls instead of reconnecting each time.
# Cuts the key exchange from ~960 a day per unit to a handful, but each unit
# accepts one client at a time, so while the link is held the Bluetti phone
# app cannot connect and the slot stays taken on a shared ESPHome proxy.
# 0 disables it. A positive value is a floor: the coordinator holds the link
# for at least one and a half poll intervals, because a keep-alive shorter
# than the gap between reads releases every time and reuses nothing.
KEEP_ALIVE_SECONDS = 60
