class MockControllerDataWriter:
    def __init__(self,data ,sensor_id, output) -> None:
        self.data = data
        self.data.sensor_id = sensor_id
        self.output = output
    
    def PerformMeasurement(self):
        pass

    def WriteSensorData(self):
        pass