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
