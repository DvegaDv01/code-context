def test_directory_and_file():
    # Import relevant classes
    from project.models.directory import Directory
    from project.models.file import File
    
    # Test: Create Directory and File instances
    directory = Directory("src")
    assert isinstance(directory, Directory)
    assert directory.name == "src"
    file = File("main.py")
    assert isinstance(file, File)
    assert file.name == "main.py"
    
    # Test: Add and remove subdirectories and files
    directory.create_subdirectory("subdir")
    assert "subdir" in directory.subdirectories
    directory.create_file("file.py")
    assert "file.py" in directory.files
    directory.remove_subdirectory("subdir")
    assert "subdir" not in directory.subdirectories
    directory.remove_file("file.py")
    assert "file.py" not in directory.files
    
    # Test: Add and remove variables, functions, and classes
    file.add_variable("x", "int")
    file.add_function("foo", "int foo()")
    file.add_class("Bar", ["x", "y"])
    assert file.get_variable("x") is not None
    assert file.get_function("foo") is not None
    assert file.get_class("Bar") is not None
    file.remove_variable("x")
    file.remove_function("foo")
    file.remove_class("Bar")
    assert file.get_variable("x") is None
    assert file.get_function("foo") is None
    assert file.get_class("Bar") is None