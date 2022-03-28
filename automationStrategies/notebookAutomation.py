from automationStrategies.automationStrategy import AutomationStrategy
import papermill as pm

class NotebookAutomation(AutomationStrategy):
    
    def __init__(self, jpNotebookInputPath,jpNotebookOutputPath, parameters = dict(), queueLength = 1) -> None:
        super().__init__()
        self.jpNotebookInputPath = jpNotebookInputPath
        self.jpNotebookOutputPath = jpNotebookOutputPath
        self.parameters = parameters
        self.queueLength = queueLength
        self.inQueue = 0

    def PerformAutomation(self):
        if(self.queueLength > 1):
            self.inQueue = self.inQueue + 1
            if(self.inQueue >= self.queueLength):
                self.inQueue = 0
                self.ExecuteJpNotebook()
        else:
            self.ExecuteJpNotebook()

    def ExecuteJpNotebook(self):
        pm.execute_notebook(self.jpNotebookInputPath, self.jpNotebookOutputPath, self.parameters)

