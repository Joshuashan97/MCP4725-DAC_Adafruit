import board
import busio
import sys

import adafruit_mcp4725

i2c = busio.I2C(board.SCL, board.SDA)

dac = adafruit_mcp4725.MCP4725(i2c)


dac.raw_value = int(sys.argv[1])
#dac.raw_value = 2048