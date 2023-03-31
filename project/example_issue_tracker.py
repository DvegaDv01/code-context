from core.issue_tracker import IssueTracker

def example_issue_tracker():
    # Create an instance of the IssueTracker
    issue_tracker = IssueTracker()

    # Create new issues
    issue_tracker.create_issue("Fix bug in login", "The login page has a bug.", "Bug")
    issue_tracker.create_issue("Improve homepage UI", "Redesign the homepage.", "Enhancement")

    # Update issue statuses
    issue_tracker.update_issue_status(issue_index=0, new_status="In Progress")
    issue_tracker.update_issue_status(issue_index=1, new_status="Closed")

    # Print the updated issues
    print(issue_tracker.to_json())

if __name__ == "__main__":
    example_issue_tracker()
