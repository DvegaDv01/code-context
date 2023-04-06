class Dependencies:
    def __init__(self):
        self.dependencies = []
        
    def add_dependency(self, library, version):
        if not library or not version:
            return None  # Invalid input
        if any(dep["library"] == library for dep in self.dependencies):
            return None  # Duplicate dependency
        dependency = {"library": library, "version": version}
        self.dependencies.append(dependency)
    
    def remove_dependency(self, library):
        self.dependencies = [dep for dep in self.dependencies if dep["library"] != library]

    def to_json(self):
        return self.dependencies

    @classmethod
    def from_json(cls, dependencies_json):
        dependencies = cls()
        dependencies.dependencies = dependencies_json
        return dependencies

    def __str__(self):
        dep_str_list = [f"{dep['library']} (v{dep['version']})" for dep in self.dependencies]
        return ", ".join(dep_str_list)
