from reactpy import component, html, run, hooks
from reactpy.backend.fastapi import configure
from utils import styles

@component
def Header():
    return html.header(
        {
            "style": {
                "background": f"linear-gradient(135deg, {styles.STYLES['colors']['primary']} 0%, {styles.STYLES['colors']['secondary']} 100%)",
                "color": styles.STYLES['colors']['white'],
                "padding": "1.5rem 2rem",
                "boxShadow": styles.STYLES['shadows']['medium'],
                "position": "sticky",
                "top": "0",
                "zIndex": "1000",
                "backdropFilter": "blur(10px)"
            }
        },
        html.div(
            {
                "style": {
                    "display": "flex",
                    "justifyContent": "space-between",
                    "alignItems": "center",
                    "maxWidth": "1200px",
                    "margin": "0 auto",
                    "width": "100%"
                }
            },
  
            html.div(
                {
                    "style": {
                        "display": "flex",
                        "alignItems": "center",
                        "gap": "1rem"
                    }
                },
                html.div(
                    {
                        "style": {
                            "width": "40px",
                            "height": "40px",
                            "background": styles.STYLES['colors']['white'],
                            "borderRadius": "12px",
                            "display": "flex",
                            "alignItems": "center",
                            "justifyContent": "center",
                            "fontWeight": "bold",
                            "color": styles.STYLES['colors']['primary'],
                            "fontSize": "1.2rem"
                        }
                    },
                    "🎬"
                ),
                html.h1(
                    {
                        "style": {
                            "margin": "0",
                            "fontSize": "2rem",
                            "fontWeight": "800",
                            "background": f"linear-gradient(45deg, {styles.STYLES['colors']['white']}, {styles.STYLES['colors']['accent']})",
                            "backgroundClip": "text",
                            "webkitBackgroundClip": "text",
                            "color": "transparent"
                        }
                    },
                    "MRecommender"
                )
            ),
            
            html.nav(
                {
                    "style": {
                        "display": "flex",
                        "gap": "2rem",
                        "alignItems": "center"
                    }
                },
                html.a(
                    {
                        "href": "#about",
                        "style": {
                            "color": styles.STYLES['colors']['white'],
                            "textDecoration": "none",
                            "padding": "0.5rem 1rem",
                            "borderRadius": "25px",
                            "transition": "all 0.3s ease",
                            "fontWeight": "500"
                        },
                        "onMouseOver": lambda e: e.target.update({
                            "style": {
                                **e.target["style"],
                                "background": "rgba(255,255,255,0.1)",
                                "transform": "translateY(-2px)"
                            }
                        }),
                        "onMouseOut": lambda e: e.target.update({
                            "style": {
                                **e.target["style"],
                                "background": "transparent",
                                "transform": "translateY(0)"
                            }
                        })
                    },
                    "About KNN"
                ),
            )
        )
    )