import importlib

class State:
    def Update(self,placeholder):
        pass
    def Draw(self,placeholder):
        pass
    def Init(self,File):
        mod = importlib.import_module(File)
        mod.Init();
            

Global = State();
print("Global Init")
