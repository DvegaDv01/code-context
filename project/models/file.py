class File:
    def __init__(self, name):
        self.name = name
        self.variables = {}
        self.functions = {}
        self.classes = {}
        
    def add_variable(self, name, data_type):
        if name not in self.variables:
            self.variables[name] = Variable(name, data_type)
        
    def add_function(self, name, signature):
        if name not in self.functions:
            self.functions[name] = Function(name, signature)
        
    def add_class(self, name, members):
        if name not in self.classes:
            self.classes[name] = Class(name, members)
    
    def remove_variable(self, name):
        self.variables.pop(name, None)
    
    def remove_function(self, name):
        self.functions.pop(name, None)
    
    def remove_class(self, name):
        self.classes.pop(name, None)
    
    def to_json(self):
        return {
            "name": self.name,
            "variables": [var.to_json() for var in self.variables.values()],
            "functions": [func.to_json() for func in self.functions.values()],
            "classes": [cls.to_json() for cls in self.classes.values()]
        }

    @classmethod
    def from_json(cls, file_json):
        file = cls(name=file_json["name"])
        file.variables = {var["name"]: Variable.from_json(var) for var in file_json["variables"]}
        file.functions = {func["name"]: Function.from_json(func) for func in file_json["functions"]}
        file.classes = {cls["name"]: Class.from_json(cls) for cls in file_json["classes"]}
        return file


class Variable:
    def __init__(self, name, data_type):
        self.name = name
        self.data_type = data_type
    
    def to_json(self):
        return {
            "name": self.name,
            "data_type": self.data_type
        }

    @classmethod
    def from_json(cls, variable_json):
        return cls(name=variable_json["name"], data_type=variable_json["data_type"])


class Function:
    def __init__(self, name, signature):
        self.name = name
        self.signature = signature
    
    def to_json(self):
        return {
            "name": self.name,
            "signature": self.signature
        }

    @classmethod
    def from_json(cls, function_json):
        return cls(name=function_json["name"], signature=function_json["signature"])


class Class:
    def __init__(self, name, members):
        self.name = name
        self.members = members
    
    def to_json(self):
        return {
            "name": self.name,
            "members": self.members
        }

    @classmethod
    def from_json(cls, class_json):
        return cls(name=class_json["name"], members=class_json["members"])
