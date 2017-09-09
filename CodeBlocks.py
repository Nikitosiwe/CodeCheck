class Semicolon():
    def __init__(self):
        self.type = 'Code_Semicolon'
        self.state = 'Close'
        self.content=[]
        self._permissibleContent=[]
    def Close(self):
        self.state='Close'

class Figure():
    def __init__(self):
        self.type = 'Code_Figure'
        self.state = 'Open'
        self.head = []
        self.content=[]
        self._permissibleContent=[]
    def Close(self):
        self.state='Close'

class Dot():
    def __init__(self):
        self.type = 'Code_Dot'
        self.state = 'Open'
        self.head = []
        self.content=[]
        self._permissibleContent=[]
    def Close(self):
        self.state='Close'

class NoneCode():
    def __init__(self):
        self.type = 'Code_NonTypeBlock'
        self.state = 'Open'
        self.content=[]
        self._permissibleContent = []

class Container():
    def __init__(self):
        self.type = 'Code_Conteiner'
        self.state = 'Open'
        self.content=[]
    def Close(self):
        self.state='Close'