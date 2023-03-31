from core.version_control import VersionControl

def example_version_control():
    # Create an instance of the VersionControl
    version_control = VersionControl()

    # Create new branches
    version_control.create_branch("feature1")
    version_control.create_branch("feature2")

    # Make commits to different branches
    version_control.current_branch = "feature1"
    version_control.commit_changes("Add new feature 1")
    version_control.current_branch = "feature2"
    version_control.commit_changes("Add new feature 2")

    # Print the version control branches and commits
    print(version_control.to_json())

if __name__ == "__main__":
    example_version_control()
