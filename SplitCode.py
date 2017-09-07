def setFile(pathFile):
    try:
        file = open(pathFile,'r')
        codeText = file.read()
        file.close()
        return codeText
    except FileNotFoundError:
        print("Файл не найден")

def getBlocks(codeText):
    pass

if __name__ == '__main__':
    print(setFile('TestCode'))