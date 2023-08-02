from . import schema

# file_name: location
files = {"file1": "/file1",
         "file2": "/file2",
         "file3": "/file3",
         "file4": "/file4"
         }

texts = ["text1", "url2", "something"]


# Get
def list_text():
    return texts


def list_files():
    return files.keys()


def get_file(file_name: str):
    return files[file_name]


# Post
def post_text(text: schema.Text):
    print(dir(text))
    return True


def post_file(file: schema.File):
    print(dir(file))
    return True

# key: value
