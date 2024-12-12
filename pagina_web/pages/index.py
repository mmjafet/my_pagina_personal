import reflex as rx

def render():
    return rx.center(
        rx.vstack(
            rx.image(src="/profile_photo.png", width="200px", border_radius="full"),
            rx.heading("¡Hola, soy Suseth Sandoval! 🚀", size="lg"),
            rx.text("Soy desarrolladora con experiencia en Flask, optimización y aplicaciones modernas."),
            rx.button("Ver Proyectos", link="/projects", color_scheme="blue"),
            rx.button("Contacto", link="/contact", color_scheme="green"),
            spacing="5",
        ),
        height="100vh",
    )
