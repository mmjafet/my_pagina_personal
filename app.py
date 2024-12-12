import reflex as rx
from mi_cv_reflex.pages import index, projects, contact
from mi_cv_reflex.styles.theme import theme

# Crear la aplicación Reflex
app = rx.App(theme=theme)

# Agregar las páginas
app.add_page(index.render, route="/")
app.add_page(projects.render, route="/projects")
app.add_page(contact.render, route="/contact")

# Compilar la app
app.compile()
