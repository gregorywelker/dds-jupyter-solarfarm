from os import path as os_path
def GetBaseDirectory():
    return os_path.dirname(os_path.realpath(__file__)).replace("/common","")