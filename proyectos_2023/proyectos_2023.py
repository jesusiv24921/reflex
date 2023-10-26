import reflex as rx
import random
import matplotlib.pyplot as plt
from io import BytesIO
import base64

# URL de la documentación
docs_url = "https://reflex.dev/docs/getting-started/introduction"

# Nombre del archivo
filename = "proyectos_2023.py"

class State(rx.State):
    """El estado de la aplicación."""
    pass

# Función para generar puntos aleatorios
def generate_random_points(num_points):
    x = [random.random() for _ in range(num_points)]
    y = [random.random() for _ in range(num_points)]
    return x, y

# Función para generar el gráfico scatter
def scatter_plot():
    x, y = generate_random_points(100)

    plt.scatter(x, y)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Scatter Plot of Random Points')

    # Guardar el gráfico en un objeto BytesIO
    img_bytes = BytesIO()
    plt.savefig(img_bytes, format='png')
    img_bytes.seek(0)

    # Convertir la imagen a base64
    encoded_img = base64.b64encode(img_bytes.read()).decode('utf-8')

    return encoded_img

# Función para mostrar la página
def index() -> rx.Component:
    return rx.fragment(
        rx.color_mode_button(rx.color_mode_icon(), float="right"),
        rx.vstack(
            rx.heading("Scatter Plot en Reflex", font_size="2em"),
            rx.box(
                rx.image(src=f"data:image/png;base64,{scatter_plot()}", width="600px", height="400px"),
                margin="2em",
            ),
            rx.link(
                "¡Consulte nuestra documentación!",
                href=docs_url,
                border="0.1em solid",
                padding="0.5em",
                border_radius="0.5em",
                _hover={
                    "color": rx.color_mode_cond(
                        light="rgb(107,99,246)",
                        dark="rgb(179, 175, 255)",
                    )
                },
            ),
            spacing="1.5em",
            font_size="2em",
            padding_top="5%",
        ),
    )

# Agregar estado y página a la aplicación
app = rx.App()
app.add_page(index)
app.compile()
