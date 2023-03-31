class LanguageContext:
    def __init__(self):
        self.variables = {}
        self.functions = {}
        self.classes = {}
    
    def add_variable(self, name, data_type):
        self.variables[name] = {"data_type": data_type}
    
    def add_function(self, name, signature):
        self.functions[name] = {"signature": signature}
    
    def add_class(self, name, members):
        self.classes[name] = {"members": members}
    
    def get_variable(self, name):
        return self.variables.get(name)
    
    def get_function(self, name):
        return self.functions.get(name)
    
    def get_class(self, name):
        return self.classes.get(name)
    
    def update_variable(self, name, new_data):
        if name in self.variables:
            self.variables[name].update(new_data)
    
    def update_function(self, name, new_data):
        if name in self.functions:
            self.functions[name].update(new_data)
    
    def update_class(self, name, new_data):
        if name in self.classes:
            self.classes[name].update(new_data)
    
    def delete_variable(self, name):
        self.variables.pop(name, None)
    
    def delete_function(self, name):
        self.functions.pop(name, None)
    
    def delete_class(self, name):
        self.classes.pop(name, None)
