from fastapp.api.v1_depricated import schema

texts = {"hello", "world"}


def list_text():
    return texts


def post_text(text: schema.Text):
    texts.add(text.text_field)
    return True

