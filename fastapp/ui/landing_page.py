
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastui import FastUI, AnyComponent, prebuilt_html, components as c
from fastui.events import PageEvent

from fastapp.ui.demo_page import demo_page

ui_router = APIRouter(
    prefix="/ui",
)

#
#
#
# Too new
# https://github.com/pydantic/FastUI
#
#
#
#
#

@ui_router.get("/reek/", response_model=FastUI, response_model_exclude_none=True)
def button() -> list[AnyComponent]:
    return demo_page(
        c.Div(
            components=[
                c.Heading(text='Button and Modal', level=2),
                c.Paragraph(text='The button below will open a modal with static content.'),
                c.Button(text='Show Static Modal', on_click=PageEvent(name='static-modal')),
                c.Modal(
                    title='Static Modal',
                    body=[c.Paragraph(text='This is some static content that was set when the modal was defined.')],
                    footer=[
                        c.Button(text='Close', on_click=PageEvent(name='static-modal', clear=True)),
                    ],
                    open_trigger=PageEvent(name='static-modal'),
                ),
            ],
            class_name='border-top mt-3 pt-1',
        )
    )


@ui_router.get('/{path:path}')
async def html_landing() -> HTMLResponse:
    """Simple HTML page which serves the React app, comes last as it matches all paths."""
    return HTMLResponse(prebuilt_html(title='FastUI Demo'))
