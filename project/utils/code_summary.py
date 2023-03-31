class CodeSummary:
    def __init__(self):
        self.summary = {
            'variables': {},
            'functions': {},
            'classes': {}
        }
    
    def add_variable(self, name, data_type, language):
        if not name or not data_type or not language:
            return None  # Invalid input
        self.summary['variables'][name] = {'data_type': data_type, 'language': language}
    
    def remove_variable(self, name):
        self.summary['variables'].pop(name, None)
    
    def add_function(self, name, signature, language):
        if not name or not signature or not language:
            return None  # Invalid input
        self.summary['functions'][name] = {'signature': signature, 'language': language}
    
    def remove_function(self, name):
        self.summary['functions'].pop(name, None)
    
    def add_class(self, name, members, language):
        if not name or not members or not language:
            return None  # Invalid input
        self.summary['classes'][name] = {'members': members, 'language': language}
    
    def remove_class(self, name):
        self.summary['classes'].pop(name, None)
    
    def get_summary(self):
        return self.summary
    
    def update_code_context(self, code_context):
        def update_language_context(language, data, update_func):
            lang_context = code_context.get_language_context(language)
            if not lang_context:
                lang_context = code_context.create_language_context(language)
            update_func(lang_context, data)
        
        for name, variable_data in self.summary['variables'].items():
            language = variable_data['language']
            update_language_context(language, variable_data, lambda ctx, data: ctx.add_variable(name, data['data_type']))
        
        for name, function_data in self.summary['functions'].items():
            language = function_data['language']
            update_language_context(language, function_data, lambda ctx, data: ctx.add_function(name, data['signature']))
        
        for name, class_data in self.summary['classes'].items():
            language = class_data['language']
            update_language_context(language, class_data, lambda ctx, data: ctx.add_class(name, data['members']))
