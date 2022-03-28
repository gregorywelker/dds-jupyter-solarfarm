class LoadControllerData():
    def __init__(self) -> None:
        super().__init__()
        self.sensor_id: int
        self.timestamp: str
        self.load: int
    def ToString(self) -> str:
        return str(self.sensor_id) + "," + self.timestamp + "," + str(self.load)

    def ToStringLabeled(self) ->str:
        return "Type,LoadController,Id,"+ str(self.sensor_id) + ",Timestamp," + self.timestamp + ",Load," + str(self.load)

    def GetLabels(self):
        return 'id,timestamp,load'