class VersionControl:
    def __init__(self):
        self.branches = {"main": Branch("main")}
        self.current_branch = "main"
    
    def create_branch(self, name):
        self.branches[name] = Branch(name)
    
    def commit_changes(self, message):
        current_branch = self.branches[self.current_branch]
        current_branch.commit_changes(message)
    
    def to_json(self):
        return {
            "branches": [branch.to_json() for branch in self.branches.values()],
            "current_branch": self.current_branch
        }

    @classmethod
    def from_json(cls, vc_json):
        vc = cls()
        vc.branches = {branch["name"]: Branch.from_json(branch) for branch in vc_json.get("branches", [])}
        vc.current_branch = vc_json.get("current_branch", "main")
        return vc


class Branch:
    def __init__(self, name):
        self.name = name
        self.commits = []
    
    def commit_changes(self, message):
        timestamp = time.time()
        commit = {"message": message, "timestamp": timestamp}
        self.commits.append(commit)
    
    def to_json(self):
        return {
            "name": self.name,
            "commits": self.commits
        }

    @classmethod
    def from_json(cls, branch_json):
        branch = cls(name=branch_json["name"])
        branch.commits = branch_json["commits"]
        return branch
