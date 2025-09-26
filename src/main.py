from reactpy import component, html
from reactpy.backend.fastapi import configure
from fastapi import FastAPI

# Importaciones absolutas
from src.components.Header import Header
from src.components.Footer import Footer
from src.components.HeroSection import HeroSection
from src.components.MovieSearch import MovieSearch

app = FastAPI()

@component
def App():
    return html.div(
        {
            "style": {
                "margin": "0",
                "padding": "0",
                "minHeight": "100vh",
                "fontFamily": "'Inter', 'Segoe UI', system-ui, sans-serif",
                "background": "#F3F4F6"
            }
        },
        html.style("""
            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
            body {
                margin: 0;
                padding: 0;
            }
            * {
                box-sizing: border-box;
            }
        """),
        Header(),
        HeroSection(),
        MovieSearch(),
        Footer()
    )

configure(app, App)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)