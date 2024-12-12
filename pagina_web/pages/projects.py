import reflex as rx

def render():
    return rx.vstack(
        rx.heading("Mis Proyectos", size="lg"),
        rx.text("Aquí encontrarás una lista de mis proyectos más destacados."),
        rx.hstack(
            rx.card(
                rx.image(src="/project1.png"),
                rx.text("Proyecto 1: Optimización Simplex"),
            ),
            rx.card(
                rx.image(src="/project2.png"),
                rx.text("Proyecto 2: Aplicación de Flask para facial points"),
            ),
            rx.card(
                rx.image(src="/project3.png"),
                rx.text("Proyecto 3: Creaccion y estudio de pipelines para analis de datos"),
            ),
        ),
        rx.link("Volver al inicio", href="/"),
        spacing="5",
        padding="5",
    )
