from common.common import GetBaseDirectory
from dataReaders.controllerDataReader import ControllerDataReader
from dataClasses.loadControllerData import LoadControllerData

class LoadControllerDataReader(ControllerDataReader):
    def __init__(self) -> None:
        super().__init__(
        config_name="SolarFarmParticipantLibrary::SolarFarmDataSubscriberParticipant", 
        url=GetBaseDirectory() + "/solarfarm.xml",
        input_name="SolarFarmDataSubscriber::LoadControllerDataReader")

    def ReadData(self):
        self.input.wait()
        self.input.take()
        for sample in self.input.samples.valid_data_iter:
            data = LoadControllerData()
            data.sensor_id = int(sample.get_number("id"))
            data.timestamp = sample.get_string("timestamp")
            data.load = int(sample.get_number("load"))
            self.data.append(data)