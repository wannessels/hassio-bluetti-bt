"""Constants for the Bluetti BT integration."""

DOMAIN = "bluetti_bt"
MANUFACTURER = "Bluetti"

CONF_OPTIONS = "options"

DATA_COORDINATOR = "coordinator"
DATA_LOCK = "lock"

# Hold the BLE link open between polls instead of reconnecting each time.
# Cuts the key exchange from thousands a day to a handful, but each unit
# accepts one client at a time, so while the link is held the Bluetti phone
# app cannot connect and the slot stays taken on a shared ESPHome proxy.
# 0 disconnects after every read.
KEEP_ALIVE_SECONDS = 0
