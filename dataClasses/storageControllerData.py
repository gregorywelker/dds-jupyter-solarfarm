class StorageControllerData():
    def __init__(self) -> None:
        super().__init__()
        self.sensor_id: int
        self.timestamp: str
        self.energyStorage: int
    def ToString(self) -> str:
        return str(self.sensor_id) + "," + self.timestamp + "," + str(self.energyStorage)

    def ToStringLabeled(self) ->str:
        return "Type,StorageController,Id,"+ str(self.sensor_id) + ",Timestamp," + self.timestamp + ",EnergyStorage," + str(self.energyStorage)

    def GetLabels(self):
        return 'id,timestamp,energyStorage'