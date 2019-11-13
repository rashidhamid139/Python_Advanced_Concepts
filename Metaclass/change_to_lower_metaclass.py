# A metaclass which will convert all uppercase methods into lowercase

class Change_to_Lower(type):
    def __new__(lowerattr_metaclass, class_name, class_parents, class_attr):
        lowercase_attributes = {}
        for name, value in class_attr.items():
            if not name.startswith('__'):
                lowercase_attributes[name.lower()] = value
            else:
                lowercase_attributes[name] = value
                
        return type(class_name, class_parents, lowercase_attributes)
        
        
 
class Test_class(metaclass= Change_to_Lower):
    def SAY(self):
        print("Uppercase will be converted to lowercase")
        
        
        
        
obj = Test_class()
#if we try to use obj.SAY() it will prompt an error
#since we have used metaclass that will internally change SAY to say
#hence we can use obj.say instead of say


#this will not work
obj.SAY()


#this will work
obj.say()
