class File:
    def __init__(self, name):
        self.name = name
        self.variables = {}
        self.functions = {}
        self.classes = {}
        
    def add_variable(self, name, data_type):
        if name in self.variables:
            raise ValueError(f"Variable '{name}' already exists")
        self.variables[name] = Variable(name, data_type)
        
    def add_function(self, name, signature):
        if name in self.functions:
            raise ValueError(f"Function '{name}' already exists")
        self.functions[name] = Function(name, signature)
        
    def add_class(self, name, members):
        if name in self.classes:
            raise ValueError(f"Class '{name}' already exists")
        self.classes[name] = Class(name, members)
    
    def update_variable(self, name, data_type):
        if name not in self.variables:
            raise ValueError(f"Variable '{name}' not found")
        self.variables[name].data_type = data_type

    def update_function(self, name, signature):
        if name not in self.functions:
            raise ValueError(f"Function '{name}' not found")
        self.functions[name].signature = signature

    def update_class(self, name, members):
        if name not in self.classes:
            raise ValueError(f"Class '{name}' not found")
        self.classes[name].members = members

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
        if "name" not in file_json:
            raise ValueError("File JSON is missing 'name' key")
        file = cls(name=file_json["name"])
        file.variables = {var["name"]: Variable.from_json(var) for var in file_json.get("variables", [])}
        file.functions = {func["name"]: Function.from_json(func) for func in file_json.get("functions", [])}
        file.classes = {cls["name"]: Class.from_json(cls) for cls in file_json.get("classes", [])}
        return file




class Variable:
    def __init__(self, name, data_type):
        self.name = name
        self.data_type = data_type
    
    def __str__(self):
        return f"{self.data_type} {self.name}"
    
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
    def __init__(self, name, attributes, methods):
        self.name = name
        self.attributes = attributes  # List of attributes
        self.methods = methods  # List of methods
    
    def to_json(self):
        return {
            "name": self.name,
            "attributes": [attr.to_json() for attr in self.attributes],
            "methods": [method.to_json() for method in self.methods]
        }

    @classmethod
    def from_json(cls, class_json):
        attributes = [Variable.from_json(attr) for attr in class_json.get("attributes", [])]
        methods = [Function.from_json(method) for method in class_json.get("methods", [])]
        return cls(name=class_json["name"], attributes=attributes, methods=methods)
