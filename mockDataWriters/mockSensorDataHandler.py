from os import path as os_path
from time import sleep
import rticonnextdds_connector as rti
from mockDataWriters.mockLoadControllerDataWriter import MockLoadControllerDataWriter
from mockDataWriters.mockStorageControllerDataWriter import MockStorageControllerDataWriter
from mockDataWriters.mockSolarPanelControllerDataWriter import MockSolarPanelControllerDataWriter
from dataClasses.loadControllerData import LoadControllerData
from dataClasses.storageControllerData import StorageControllerData
from dataClasses.solarPanelControllerData import SolarPanelControllerData



class MockSensorDataHandler:

    def WriteMockSensorData(self):
        base_directory = os_path.dirname(os_path.realpath(__file__))

        with rti.open_connector(
            config_name="SolarFarmParticipantLibrary::SolarFarmDataPublisherParticipant",
            url=base_directory + "/../solarfarm.xml") as connector:

            sensors = [
            MockLoadControllerDataWriter(data=LoadControllerData(),sensor_id=3,output=connector.getOutput("SolarFarmDataPublisher::LoadControllerDataWriter")),
            MockStorageControllerDataWriter(data=StorageControllerData(), sensor_id=4,output=connector.getOutput("SolarFarmDataPublisher::StorageControllerDataWriter")),
            MockSolarPanelControllerDataWriter(data=SolarPanelControllerData(),sensor_id=0,output=connector.getOutput("SolarFarmDataPublisher::SolarPanelControllerDataWriter")),
            MockSolarPanelControllerDataWriter(data=SolarPanelControllerData(),sensor_id=1,output=connector.getOutput("SolarFarmDataPublisher::SolarPanelControllerDataWriter")),
            MockSolarPanelControllerDataWriter(data=SolarPanelControllerData(),sensor_id=2,output=connector.getOutput("SolarFarmDataPublisher::SolarPanelControllerDataWriter"))
            ]
            while (True):
                for sensor in sensors:
                    sensor.PerformMeasurement()
                for sensor in sensors:
                    sensor.WriteSensorData()
                sleep(2)