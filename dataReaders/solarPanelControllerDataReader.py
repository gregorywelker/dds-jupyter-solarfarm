from common.common import GetBaseDirectory
from dataReaders.controllerDataReader import ControllerDataReader
from dataClasses.solarPanelControllerData import SolarPanelControllerData

class SolarPanelControllerDataReader(ControllerDataReader):
    def __init__(self) -> None:
        super().__init__( 
        config_name="SolarFarmParticipantLibrary::SolarFarmDataSubscriberParticipant", 
        url=GetBaseDirectory() + "/solarfarm.xml",
        input_name="SolarFarmDataSubscriber::SolarPanelControllerDataReader")

    def ReadData(self):
        self.input.wait()
        self.input.take()
        for sample in self.input.samples.valid_data_iter:
            data = SolarPanelControllerData()
            data.sensor_id = int(sample.get_number("id"))
            data.timestamp = sample.get_string("timestamp")
            data.energy = int(sample.get_number("energy"))
            self.data.append(data)