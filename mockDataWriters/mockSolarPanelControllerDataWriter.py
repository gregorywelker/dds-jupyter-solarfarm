from math import sin
import math
from random import random
from datetime import datetime

from scipy import rand
from mockDataWriters.mockControllerDataWriter import MockControllerDataWriter


class MockSolarPanelControllerDataWriter(MockControllerDataWriter):
    def __init__(self, data, sensor_id, output) -> None:
        super().__init__(data, sensor_id, output)

    def PerformMeasurement(self):
        # self.data.timestamp = datetime.now().strftime("%m/%d/%Y:%H:%M:%S")
        self.data.timestamp = datetime(2022, 5, 20, 12, datetime.now().minute, datetime.now().second).strftime("%m/%d/%Y:%H:%M:%S")

        add = 0
        ran = random()
        if(ran > 0.75):
            add = (random() - 0.5) * 2

        self.data.energy = add + (sin(((datetime.now().minute * 60) + datetime.now().second) / 3600 * 90 * math.pi / 180) * 70) + 220

    def WriteSensorData(self):
        self.output.instance.set_number("id", self.data.sensor_id)
        self.output.instance.set_string("timestamp", self.data.timestamp)
        self.output.instance.set_number("energy", self.data.energy)
        self.output.write()
        print("Writing to DDS: " + self.data.ToStringLabeled())
