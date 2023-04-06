from core.code_context import CodeContext
from core.project_config import ProjectConfig
from core.version_control import VersionControl, Branch
from core.issue_tracker import IssueTracker
from core.test_suite import TestSuite
from core.dependencies import Dependencies

def create_code_context_interactively():
    # Create an instance of CodeContext and its components
    language = input("Enter the programming language of your project: ")
    code_context = CodeContext(language=language)
    project_config = ProjectConfig()
    version_control = VersionControl()
    issue_tracker = IssueTracker()
    test_suite = TestSuite()
    dependencies = Dependencies()

    # Set project configurations
    compiler_options = input("Enter compiler options: ")
    build_targets = input("Enter build targets: ")
    project_config.set_compiler_options(compiler_options)
    project_config.set_build_targets(build_targets)
    code_context.project_config = project_config

    # Add version control branches and commits
    while True:
        add_branch = input("Do you want to add a branch to version control? (y/n) ")
        if add_branch.lower() != 'y':
            break
        branch_name = input("Enter branch name: ")
        version_control.create_branch(branch_name)
        branch = version_control.branches[branch_name]
        while True:
            add_commit = input(f"Do you want to add a commit to branch '{branch_name}'? (y/n) ")
            if add_commit.lower() != 'y':
                break
            commit_message = input("Enter commit message: ")
            branch.commit_changes(commit_message)
    code_context.version_control = version_control

    # Add issues to issue tracker
    while True:
        add_issue = input("Do you want to add an issue to the issue tracker? (y/n) ")
        if add_issue.lower() != 'y':
            break
        issue_title = input("Enter issue title: ")
        issue_description = input("Enter issue description: ")
        issue_type = input("Enter issue type (e.g., bug, feature): ")
        issue_tracker.create_issue(issue_title, issue_description, issue_type)
    code_context.issue_tracker = issue_tracker

    # Add tests to test suite
    while True:
        add_test = input("Do you want to add a test to the test suite? (y/n) ")
        if add_test.lower() != 'y':
            break
        test_name = input("Enter test name: ")
        inputs = input("Enter test inputs (comma-separated): ").split(',')
        expected_outputs = input("Enter expected outputs (comma-separated): ").split(',')
        test_suite.add_test(test_name, inputs, expected_outputs)
    code_context.test_suite = test_suite

    # Add dependencies
    while True:
        add_dependency = input("Do you want to add a dependency? (y/n) ")
        if add_dependency.lower() != 'y':
            break
        library = input("Enter library name: ")
        version = input("Enter library version: ")
        dependencies.add_dependency(library, version)
    code_context.dependencies = dependencies

    # Serialize CodeContext to JSON and print the result
    code_context_json = code_context.to_json()
    print("Code Context JSON:")
    print(code_context_json)

if __name__ == "__main__":
    create_code_context_interactively()
