class ProjectConfig:
    def __init__(self):
        self.compiler_options = ""
        self.build_targets = ""
        self.settings = {}
    
    def set_compiler_options(self, options):
        self.compiler_options = options
    
    def set_build_targets(self, targets):
        self.build_targets = targets
    
    def set_setting(self, key, value):
        self.settings[key] = value
    
    def to_json(self):
        return {
            "compiler_options": self.compiler_options,
            "build_targets": self.build_targets,
            "settings": self.settings
        }

    @classmethod
    def from_json(cls, config_json):
        config = cls()
        config.compiler_options = config_json.get("compiler_options", "")
        config.build_targets = config_json.get("build_targets", "")
        config.settings = config_json.get("settings", {})
        return config
