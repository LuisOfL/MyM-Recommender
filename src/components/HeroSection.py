from reactpy import component, html, run, hooks
from reactpy.backend.fastapi import configure
from src.utils import styles

@component
def HeroSection():
    return html.section(
        {
            "style": {
                "background": f"linear-gradient(135deg, {styles.STYLES['colors']['light']} 0%, #e2e8f0 100%)",
                "minHeight": "70vh",
                "display": "flex",
                "alignItems": "center",
                "justifyContent": "center",
                "padding": "4rem 2rem",
                "position": "relative",
                "overflow": "hidden"
            }
        },
       
        html.div(
            {
                "style": {
                    "position": "absolute",
                    "top": "-50%",
                    "right": "-10%",
                    "width": "800px",
                    "height": "800px",
                    "background": f"radial-gradient(circle, {styles.STYLES['colors']['primary']}20 0%, transparent 70%)",
                    "borderRadius": "50%"
                }
            }
        ),
        
        html.div(
            {
                "style": {
                    "maxWidth": "1200px",
                    "margin": "0 auto",
                    "textAlign": "center",
                    "position": "relative",
                    "zIndex": "2"
                }
            },
            html.h1(
                {
                    "style": {
                        "fontSize": "3.5rem",
                        "fontWeight": "800",
                        "marginBottom": "1rem",
                        "background": f"linear-gradient(45deg, {styles.STYLES['colors']['primary']}, {styles.STYLES['colors']['secondary']})",
                        "backgroundClip": "text",
                        "webkitBackgroundClip": "text",
                        "color": "transparent",
                        "lineHeight": "1.2"
                    }
                },
                "Find your new favorite movie"
            ),
            html.p(
                {
                    "style": {
                        "fontSize": "1.3rem",
                        "color": styles.STYLES['colors']['dark'],
                        "marginBottom": "2.5rem",
                        "maxWidth": "600px",
                        "marginLeft": "auto",
                        "marginRight": "auto",
                        "lineHeight": "1.6"
                    }
                },
                "This is a movie recommender using AI"
            )
        )
    )