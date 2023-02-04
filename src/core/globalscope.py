import importlib

class State:
    def Update(self):
        pass
    def Draw(self,self):
        pass
    def Init(self,File):
        mod = importlib.import_module(File)
        mod.Init();
            

Global = State();
print("Global Init")
