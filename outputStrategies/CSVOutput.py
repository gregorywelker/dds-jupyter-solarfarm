import os
from outputStrategies.outputStrategy import OutputStrategy
from readerwriterlock import rwlock


class CSVOutput(OutputStrategy):

    def __init__(self, filePath, fileName, labeled=False) -> None:
        super().__init__()
        self.filePath = filePath
        self.fileName = fileName
        self.wlock = rwlock.RWLockFairD()
        self.labeled = labeled

        f = open(self.filePath + self.fileName + '.csv', mode='a')
        f.close()

        self.startSize = os.path.getsize(self.filePath + self.fileName + '.csv')
        self.addedLabels = False

    def WriteOutput(self, reader):
        with self.wlock.gen_wlock():
            f = open(self.filePath + self.fileName + '.csv', mode='a')

            for data in reader.data:
                if(self.labeled == False):
                    if(self.startSize <= 0 and self.addedLabels == False):
                        self.addedLabels = True
                        f.write(data.GetLabels()+"\n")
                    f.write(data.ToString() + "\n")
                else:
                    f.write(data.ToStringLabeled() + "\n")
            f.close()
