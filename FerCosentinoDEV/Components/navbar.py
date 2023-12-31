import reflex as rx
from FerCosentinoDEV.Styles.colors import Color

def navbar() -> rx.Component:
    return  rx.hstack(
                rx.image(
                    src="favicon.ico",
                    height="90px",
                    margin_right="1%",
                    margin_left="2%"
                ),
                rx.text(
                    "Fernando Cosentino",
                    font_size="2.3em",
                    _as='b',
                    color = Color.PRIMARY.value,
                    margin_right="auto",
                    margin_left="2%",
                    width="81%"
                ),
                rx.button(
                    rx.icon(tag="download"),
                    'Download CV',
                    bg = Color.PRIMARY.value,
                    color = Color.BACKGROUND.value,
                    margin_left="0%",
                    margin_right="5%",
                    _hover={
                        "bg":Color.CONTENT.value,
                        "border_color":Color.SECONDARY.value,
                        "text_color":Color.SECONDARY.value,
                    },
                    on_click=rx.download(
                        url="/cv_pdf_file.pdf",
                        filename="Fernando_Cosentino_CV.pdf"
                    )
                ),
            bg = Color.BACKGROUND.value,
            position="fixed",
            width="100%",
            top="0px",
            z_index="5"    
            )