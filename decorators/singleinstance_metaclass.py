class Single_instance(type):
    def __init__(self, *args, **kwargs):
        self._instance = None
        super().__init__(*args, **kwargs)
        
        
    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = super().__call__(*args, **kwargs)
            return self._instance
        else:
            return self._instance
            
            
class Create(metaclass= Single):
    pass
    
    
    
obj1 = Create()
obj2 = Create()



print(id(obj2))
print(id(obj1))