from outputStrategies.outputStrategy import OutputStrategy

class ConsoleOutput(OutputStrategy):
    def WriteOutput(self, reader):
        for data in reader.data:
            print("ConsoleOutput:" + data.ToStringLabeled())