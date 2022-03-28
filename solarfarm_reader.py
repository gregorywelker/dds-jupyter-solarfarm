import threading
from automationStrategies.notebookAutomation import NotebookAutomation
from common.common import GetBaseDirectory
from dataReaders.controllerDataReaderThread import ControllerDataReaderThread
from dataReaders.loadControllerDataReader import LoadControllerDataReader
from dataReaders.storageControllerDataReader import StorageControllerDataReader
from dataReaders.solarPanelControllerDataReader import SolarPanelControllerDataReader
from outputStrategies.CSVOutput import CSVOutput
from outputStrategies.consoleOutput import ConsoleOutput


CSVSolarPanelControllerOutput = CSVOutput(filePath=GetBaseDirectory() + "/data/", fileName="solarpanel_controller")
solarPanelControllerNotebookAnalysis = NotebookAutomation(
    jpNotebookInputPath=GetBaseDirectory()+"/jpnotebook/SolarFarm_SolarPanelControllerAnalysis_Input.ipynb", 
    jpNotebookOutputPath=GetBaseDirectory()+"/jpnotebook/output/SolarFarm_SolarPanelControllerAnalysis_Output.ipynb", 
    parameters=dict(
        pathToFile = CSVSolarPanelControllerOutput.filePath + CSVSolarPanelControllerOutput.fileName + '.csv', 
        pathToOutput= GetBaseDirectory() + '/jpnotebook/output/'),
    queueLength=1
)

readers = [
    # ControllerDataReaderThread(LoadControllerDataReader(), outputs=[ConsoleOutput()]),
    # ControllerDataReaderThread(StorageControllerDataReader(), outputs=[ConsoleOutput()]),
    ControllerDataReaderThread(SolarPanelControllerDataReader(), outputs=[ConsoleOutput(), CSVSolarPanelControllerOutput], automations=[solarPanelControllerNotebookAnalysis])
]


def StopReaders():
    print("Stopping all readers")
    for reader in readers:
        if(reader.readerFunctionActive):
            reader.Stop()


def main():
    for reader in readers:
        readerThread = threading.Thread(target=reader.ControllerDataReaderFunction)
        readerThread.daemon = True
        readerThread.start()

    cmd = ''

    while(cmd != 'exit'):
        cmd = input(
            "Waiting for commands | stop = stop readers | exit = exit app: ")
        if(cmd == 'stop'):
            StopReaders()

    StopReaders()
    print("Exiting application")

if __name__ == "__main__":
    main()