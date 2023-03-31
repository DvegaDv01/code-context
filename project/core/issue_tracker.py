class IssueTracker:
    def __init__(self):
        self.issues = []
        
    def create_issue(self, title, description, issue_type):
        if not title or not description or not issue_type:
            return None  # Invalid input
        issue = {"title": title, "description": description, "type": issue_type, "status": "Open"}
        self.issues.append(issue)
    
    def update_issue_status(self, issue_index, new_status):
        if 0 <= issue_index < len(self.issues):
            self.issues[issue_index]["status"] = new_status
    
    def to_json(self):
        return self.issues

    @classmethod
    def from_json(cls, issues_json):
        issue_tracker = cls()
        issue_tracker.issues = issues_json
        return issue_tracker
