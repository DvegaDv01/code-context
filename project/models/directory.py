class Directory:

    def __init__(self, name):

        self.name = name

        self.subdirectories = {}

        self.files = {}

        

    def create_subdirectory(self, name):

        if name not in self.subdirectories:

            subdir = Directory(name)

            self.subdirectories[name] = subdir

            return subdir

        return None  # Subdirectory already exists

    

    def remove_subdirectory(self, name):

        self.subdirectories.pop(name, None)

    

    def create_file(self, name):

        if name not in self.files:

            self.files[name] = File(name)

            return self.files[name]

        return None  # File already exists

    

    def remove_file(self, name):

        self.files.pop(name, None)

    

    def get_subdirectory(self, path):

        parts = path.split('/')

        current = self

        for part in parts:

            if part in current.subdirectories:

                current = current.subdirectories[part]

            else:

                return None  # Could not find the specified subdirectory

        return current

    

    def to_json(self):

        subdirectories_json = [subdir.to_json() for subdir in self.subdirectories.values()]

        files_json = [file.to_json() for file in self.files.values()]

        return {

            "name": self.name,

            "subdirectories": subdirectories_json,

            "files": files_json

        }



    @classmethod

    def from_json(cls, directory_json):

        directory = cls(name=directory_json["name"])

        for subdir_json in directory_json["subdirectories"]:

            subdir = Directory.from_json(subdir_json)

            directory.subdirectories[subdir.name] = subdir

        for file_json in directory_json["files"]:

            file = File.from_json(file_json)

            directory.files[file.name] = file

        return directory
