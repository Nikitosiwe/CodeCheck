def setFile(pathFile):
    try:
        file = open(pathFile,'r')
        codeText = file.read()
        file.close()
        #return ''.join(codeText.splitlines())
        return codeText
    except FileNotFoundError:
        print("Файл не найден")

def deleteComment(codeText):
    #for i in range(0,len(codeText)):
    #    if(codeText[i]=="/" and )
    commentText = ' string tmp = "asdad//"+"asda//q"; //+"// djjd  '

    for tmp in commentText.split('\n'):
        if '//' in tmp:
            print(tmp)

    return codeText


def getBlocks(codeText):
    #blocks=[b for b in codeText.replace(' ', ';').replace('(',';').replace(')',';').replace('{',';').replace('}',';').split(';') if b!='']
    blocks=[]
    symbols = [' ',';','(',')','{','}']
    codeText_nonComment = deleteComment(codeText)
    return blocks

if __name__ == '__main__':
    print(getBlocks(setFile('TestCode')))