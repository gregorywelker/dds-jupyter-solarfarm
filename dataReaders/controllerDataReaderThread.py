class ControllerDataReaderThread:
    def __init__(self, reader, outputs = [], automations = []) -> None:
        self.reader = reader
        self.outputs = outputs
        self.automations = automations
        self.readerFunctionActive = True

    def ControllerDataReaderFunction(self):
        self.reader.input.wait_for_publications()
        while(self.readerFunctionActive):
            self.reader.ReadData()

            if(len(self.outputs) > 0):
                for output in self.outputs:
                    output.WriteOutput(self.reader)
                self.reader.data = []

            if(len(self.automations) > 0):
                for automation in self.automations:
                    automation.PerformAutomation()
    
    def Stop(self):
        self.readerFunctionActive = False
        self.reader.Cleanup()