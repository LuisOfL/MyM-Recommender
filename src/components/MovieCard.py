from reactpy import component, html, run, hooks
from reactpy.backend.fastapi import configure
from src.utils import styles

@component
def MovieCard(movie_title, index):
    return html.div(
        {
            "style": {
                "background": styles.STYLES['colors']['white'],
                "borderRadius": "16px",
                "padding": "1.5rem",
                "boxShadow": styles.STYLES['shadows']['small'],
                "transition": "all 0.3s ease",
                "border": f"2px solid {styles.STYLES['colors']['light']}",
                "textAlign": "center",
                "minHeight": "120px",
                "display": "flex",
                "alignItems": "center",
                "justifyContent": "center",
                "position": "relative",
                "overflow": "hidden"
            },
            "onMouseOver": lambda e: e.target.update({
                "style": {
                    **e.target["style"],
                    "transform": "translateY(-5px)",
                    "boxShadow": styles.STYLES['shadows']['large'],
                    "borderColor": styles.STYLES['colors']['primary']
                }
            }),
            "onMouseOut": lambda e: e.target.update({
                "style": {
                    **e.target["style"],
                    "transform": "translateY(0)",
                    "boxShadow": styles.STYLES['shadows']['small'],
                    "borderColor": styles.STYLES['colors']['light']
                }
            })
        },
        html.div(
            {
                "style": {
                    "position": "absolute",
                    "top": "0.5rem",
                    "left": "0.5rem",
                    "background": styles.STYLES['colors']['primary'],
                    "color": styles.STYLES['colors']['white'],
                    "width": "30px",
                    "height": "30px",
                    "borderRadius": "50%",
                    "display": "flex",
                    "alignItems": "center",
                    "justifyContent": "center",
                    "fontWeight": "bold",
                    "fontSize": "0.9rem"
                }
            },
            f"#{index + 1}"
        ),
        
        html.h3(
            {
                "style": {
                    "margin": "0",
                    "color": styles.STYLES['colors']['dark'],
                    "fontSize": "1.1rem",
                    "fontWeight": "600",
                    "lineHeight": "1.4"
                }
            },
            movie_title
        )
    )