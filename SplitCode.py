from CodeBlocks import *

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
    #commentText = ' string tmp = "asdad//"+"asda//q"; //+"// djjd  '

    #for tmp in commentText.split('\n'):
        #if '//' in tmp:
            #print(tmp)

    return codeText


def getBlocks(codeText):
    #blocks=[b for b in codeText.replace(' ', ';').replace('(',';').replace(')',';').replace('{',';').replace('}',';').split(';') if b!='']
    blocks=Container()
    symbols = [';','.','{']
    blockText = []
    for ch in codeText:
        try:
            index = symbols.index(ch)
            #print(''.join(blockText)+ch)
            blockText.append(ch)
            cont = Container()
            if index == 0:
                sem = Semicolon()
                sem.content.append(blockText)
                cont.content.append(sem)
            elif index == 1:
                pass
            elif index == 2:
                pass
                #fig = Figure()
                #fig.head.append(blockText)
                #cont.content.append(fig)
            #if(len(cont.content)>0):
                #print(cont.content[0].content)
            blocks.content.append(cont)
            #print(blocks.content[0].content[0].content)
            blockText.clear()
        except ValueError:
            blockText.append(ch)
    return blocks

def addToBlock(blocks,block):
    pass

def printList(lst, tab):
    for l in lst:
        if isinstance(l,list):
            printList(l,tab+'\t')
        else:
            print(tab,l)

if __name__ == '__main__':
    print(getBlocks(setFile('TestCode')).content[0].content[0].content)



