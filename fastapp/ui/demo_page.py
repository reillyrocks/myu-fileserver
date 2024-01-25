
from fastui import AnyComponent
from fastui import components as c
from fastui.events import GoToEvent


def demo_page(components: AnyComponent) -> list[AnyComponent]:
    return [
        c.PageTitle(text=f'FastUI AAAA'),
        c.Navbar(
            title='FastUI Demo',
            title_event=GoToEvent(url='/'),
        ),
        c.Page(
            components=components,
        ),
        c.Footer(
            extra_text='FastUI Demo',
        ),
    ]