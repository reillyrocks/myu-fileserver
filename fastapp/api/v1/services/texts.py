from fastapp.api.v1 import schema

texts = {"hello", "world"}


def list_text():
    return texts


def post_text(text: schema.Text):
    texts.add(text.text_field)
    return True

