
class FileHandler:

    def __init__(self):
        self.__fileName = 'log.txt'


    def writeToFile(self, data:str):
        with open(file=self.__fileName, mode='a', encoding='UTF-8') as FILE:
            FILE.write(str(data))

