import reflex as rx
# Componentes
from FerCosentinoDEV.Components.navbar import navbar
# Vistas
from FerCosentinoDEV.Views.personal_info import personal_info
from FerCosentinoDEV.Views.projects import projects
from FerCosentinoDEV.Views.contact import contact
#Propiedades de Colores
from FerCosentinoDEV.Styles.colors import Color
import FerCosentinoDEV.Styles.styles as Styles
from FerCosentinoDEV.Styles.styles import LINE_TOP_STYLE

def index() -> rx.Component:
    return  rx.vstack(
                navbar(),
                rx.box(style=LINE_TOP_STYLE),
                rx.hstack(
                    personal_info(),
                    rx.center(
                        projects(),
                        width= "100%"
                    ),
                    padding_top=Styles.Size.MEDIUM.value,
                ),
            )

app = rx.App(
                style=Styles.BASE_STYLE
            )
app.add_page(
                index,
                title="Fernando Cosentino | Systems Analyst.",
                description="Hi, I'm Fernando Cosentino, a systems analyst, and this is my portfolio."
            )
app.compile()