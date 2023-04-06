import sys
import os
import json

relative_path = '/home/ben/code-context/project/'
absolute_path = os.path.abspath(relative_path)
sys.path.append(absolute_path)

from models.directory import Directory

from core.project_config import ProjectConfig

from core.version_control import VersionControl

from core.issue_tracker import IssueTracker

from core.test_suite import TestSuite

from core.dependencies import Dependencies

from core.code_context import CodeContext

from core.language_context import LanguageContext

def test_code_context():

    # Test: Create CodeContext instance
    code_context = CodeContext(language="Python")
    assert isinstance(code_context, CodeContext)
    assert code_context.language == "Python"

    # Test creating a directory and file
    src_dir = code_context.create_directory("src")
    
    # Test: Create and get language contexts
    lang_context = code_context.create_language_context("Java")
    assert lang_context is not None
    assert code_context.get_language_context("Java") == lang_context

    # Test: Clear context
    code_context.clear_context(language="Java")
    assert code_context.get_language_context("Java") is None

    # Test: Create directories and files
    src_dir = code_context.create_directory("src")
    assert src_dir is not None, "Failed to create 'src' directory"
    assert src_dir.name == "src"
    main_file = code_context.create_file("main.py", parent_path="src")
    assert main_file is not None, "Failed to create 'main.py' file"
    assert main_file.name == "main.py"
    directory = code_context.directories.get_subdirectory("src")
    assert isinstance(directory, Directory)
    assert "src" in code_context.directories.subdirectories
    assert "main.py" in directory.files

    # Test: Add and remove dependencies
    code_context.add_dependency("numpy", "1.21.0")
    assert {"library": "numpy", "version": "1.21.0"} in code_context.dependencies.dependencies
    code_context.dependencies.remove_dependency("numpy")
    assert {"library": "numpy", "version": "1.21.0"} not in code_context.dependencies.dependencies

    # Test: JSON serialization and deserialization
    serialized = code_context.serialize()
    code_context.deserialize(serialized)
    assert code_context.language == "Python"

# Execute the tests
test_code_context()
