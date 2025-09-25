from reactpy import component, html, run, hooks
from reactpy.backend.fastapi import configure
from utils import styles

@component
def Footer():
    return html.footer(
        {
            "style": {
                "background": styles.STYLES['colors']['dark'],
                "color": styles.STYLES['colors']['white'],
                "padding": "3rem 2rem",
                "textAlign": "center"
            }
        },
        html.div(
            {
                "style": {
                    "maxWidth": "1200px",
                    "margin": "0 auto"
                }
            },
            html.p(
                {
                    "style": {
                        "fontSize": "1.1rem",
                        "marginBottom": "1rem"
                    }
                },
                "🎬 MRecommender - by LuisMData"
            )
        )
    )