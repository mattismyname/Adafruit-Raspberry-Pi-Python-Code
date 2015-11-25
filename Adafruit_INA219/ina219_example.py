#!/usr/bin/python

from Subfact_ina219 import INA219
import time

ina = INA219()

while True:
    result = ina.getBusVoltage_V()
    print "{} Shunt: {} mV, Bus: {} V, Current: {} mA".format(time.time(), ina.getShuntVoltage_mV(), ina.getBusVoltage_V(), ina.getCurrent_mA())
