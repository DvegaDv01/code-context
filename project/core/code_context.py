import json
import time

class CodeContext:
    def __init__(self, language):
        self.language = language
        self.directories = Directory("root")
        self.project_config = ProjectConfig()
        self.version_control = VersionControl()
        self.issue_tracker = IssueTracker()
        self.test_suite = TestSuite()
        self.dependencies = Dependencies()
        self.languages = {}

    def to_json(self):
        # Capture directories and files
        directories = self.directories.to_json()

        # Capture project configurations
        project_config = self.project_config.to_json()

        # Capture version control
        version_control = self.version_control.to_json()

        # Capture dependencies
        dependencies = self.dependencies.to_json()

        # Capture languages
        languages = {
            language: context.to_json() for language, context in self.languages.items()
        }

        # Build the JSON representation based on the schema
        context_json = {
            "language": self.language,
            "directories": directories,
            "project_config": project_config,
            "version_control": version_control,
            "dependencies": dependencies,
            "languages": languages,
            "issue_tracker": self.issue_tracker.to_json(),
            "test_suite": self.test_suite.to_json(),
        }

        return context_json

    @classmethod
    def from_json(cls, context_json):
        # If context_json is a JSON string, parse it into a dictionary
        if isinstance(context_json, str):
            context_json = json.loads(context_json)

        # Extract language
        language = context_json.get("language", "")

        # Create CodeContext instance with the extracted language
        code_context = cls(language=language)

        # Populate directories and files
        directories_json = context_json.get("directories", [])
        code_context.directories = Directory.from_json(directories_json)

        # Populate project configurations
        project_config_json = context_json.get("project_config", {})
        code_context.project_config = ProjectConfig.from_json(project_config_json)

        # Populate version control
        version_control_json = context_json.get("version_control", {})
        code_context.version_control = VersionControl.from_json(version_control_json)

        # Populate dependencies
        dependencies_json = context_json.get("dependencies", [])
        code_context.dependencies = Dependencies.from_json(dependencies_json)

        # Populate languages
        languages_json = context_json.get("languages", {})
        for language, language_json in languages_json.items():
            code_context.languages[language] = LanguageContext.from_json(language_json)

        # Populate issue tracker
        issue_tracker_json = context_json.get("issue_tracker", [])
        code_context.issue_tracker = IssueTracker.from_json(issue_tracker_json)

        # Populate test suite
        test_suite_json = context_json.get("test_suite", [])
        code_context.test_suite = TestSuite.from_json(test_suite_json)

        return code_context

    def create_language_context(self, language):
        if language not in self.languages:
            self.languages[language] = LanguageContext()
        return self.languages[language]
    
    def get_language_context(self, language):
        return self.languages.get(language)
    
    def serialize(self):
        return json.dumps(self.to_json())
    
    def deserialize(self, serialized_context):
        loaded_data = json.loads(serialized_context)
        self.__dict__.update(CodeContext.from_json(loaded_data).__dict__)
    
    def clear_context(self, language=None):
        if language:
            if language in self.languages:
                del self.languages[language]
                return True
        else:
            self.languages.clear()
            return True
        return False

    def create_directory(self, name, parent_path=None):
        if parent_path:
            parent_dir = self.directories.get_subdirectory(parent_path)
            if parent_dir:
                return parent_dir.create_subdirectory(name)
            else:
                return None  # Could not find the specified parent directory
        else:
            return self.directories.create_subdirectory(name)

    def create_file(self, name, parent_path=None):
        if parent_path:
            parent_dir = self.directories.get_subdirectory(parent_path)
            if parent_dir:
                return parent_dir.create_file(name)
            else:
                return None  # Could not find the specified parent directory
        else:
            return self.directories.create_file(name)
        
    def add_dependency(self, library, version):
        self.dependencies.add_dependency(library, version)