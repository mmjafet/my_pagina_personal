import reflex as rx

def render():
    return rx.center(
        rx.vstack(
            rx.image(src="/profile_photo.png", width="200px", border_radius="full"),
            rx.heading("Jafet Martinez Meza! 🚀", size="lg"),
            rx.text("Desarrollador web y estudiante de ingeniería en computación"),    
            rx.button("Ver Proyectos", link="/projects", color_scheme="blue"),
            rx.button("Contacto", link="/contact", color_scheme="green"),
            spacing="5",
        ),
        height="100vh",
    )
