from rticonnextdds_connector.rticonnextdds_connector import Connector, Input
import rticonnextdds_connector as rti

class ControllerDataReader:
    def __init__(self, config_name, url, input_name) -> None:
        self.data = []
        self.connector: Connector = rti.Connector(config_name=config_name, url=url)
        self.input: Input = self.connector.get_input(input_name=input_name)
    def ReadData(self):
        pass

    def Cleanup(self):
        self.connector.close()
        print("Reader has been cleaned up")