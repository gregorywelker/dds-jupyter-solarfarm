from common.common import GetBaseDirectory
from dataReaders.controllerDataReader import ControllerDataReader
from dataClasses.storageControllerData import StorageControllerData

class StorageControllerDataReader(ControllerDataReader):
    def __init__(self) -> None:
        super().__init__(
        config_name="SolarFarmParticipantLibrary::SolarFarmDataSubscriberParticipant", 
        url=GetBaseDirectory() + "/solarfarm.xml",
        input_name="SolarFarmDataSubscriber::StorageControllerDataReader")

    def ReadData(self):
        self.input.wait()
        self.input.take()
        for sample in self.input.samples.valid_data_iter:
            data = StorageControllerData()
            data.sensor_id = int(sample.get_number("id"))
            data.timestamp = sample.get_string("timestamp")
            data.energyStorage = int(sample.get_number("energyStorage"))
            self.data.append(data)