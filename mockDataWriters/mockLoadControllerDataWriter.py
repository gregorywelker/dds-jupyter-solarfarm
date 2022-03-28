from random import random
from datetime import datetime
from mockDataWriters.mockControllerDataWriter import MockControllerDataWriter


class MockLoadControllerDataWriter(MockControllerDataWriter):
    def __init__(self, data, sensor_id, output) -> None:
        super().__init__(data, sensor_id, output)

    def PerformMeasurement(self):
        # self.data.timestamp = datetime.now().strftime("%m/%d/%Y:%H:%M:%S")
        self.data.timestamp = datetime(2022, 5, 20, 12, datetime.now().minute, datetime.now().second).strftime("%m/%d/%Y:%H:%M:%S")
        self.data.load = 1.256

    def WriteSensorData(self):
        if(random() > 0.4):
            self.output.instance.set_number("id", self.data.sensor_id)
            self.output.instance.set_string("timestamp", self.data.timestamp)
            self.output.instance.set_number("load", self.data.load)
            self.output.write()
            print("Writing to DDS: " + self.data.ToStringLabeled())
