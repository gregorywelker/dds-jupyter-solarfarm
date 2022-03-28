class SolarPanelControllerData():
    def __init__(self) -> None:
        super().__init__()
        self.sensor_id: int
        self.timestamp: str
        self.energy: int   
    def ToString(self) -> str:
        return str(self.sensor_id) + "," + self.timestamp + "," + str(self.energy)

    def ToStringLabeled(self) ->str:
        return "Type,SolarPanelController,Id,"+ str(self.sensor_id) + ",Timestamp," + self.timestamp + ",Energy," + str(self.energy)
    
    def GetLabels(self):
        return 'id,timestamp,energy'