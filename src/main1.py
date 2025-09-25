from reactpy import component, html, run, hooks
from reactpy.backend.fastapi import configure
from fastapi import FastAPI
from components import Footer
from components import Header
from components import HeroSection
from components import MovieSearch
from utils import styles

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
                "background": styles.STYLES['colors']['light']
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
    uvicorn.run(app, host="0.0.0.0", port=8002, reload=True)