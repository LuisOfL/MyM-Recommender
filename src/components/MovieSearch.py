from reactpy import component, html, hooks
from reactpy.backend.fastapi import configure
from utils import styles
import pandas as pd
import asyncio
from .MovieCard import MovieCard  
from ..models.back import KNN 

df = pd.read_csv("dataset/titles.csv")
movies = df['title'].astype(str).tolist()

@component
def MovieSearch():
    valor_input, set_valor_input = hooks.use_state("")
    resultados, set_resultados = hooks.use_state([])
    mostrar_sugerencias, set_mostrar_sugerencias = hooks.use_state(False)
    enviado, set_enviado = hooks.use_state("")
    recomendaciones, set_recomendaciones = hooks.use_state([])
    cargando, set_cargando = hooks.use_state(False)

    def filtrar(event=None):
        if valor_input.strip() == "":
            set_resultados([])
        else:
            filtradas = [p for p in movies if valor_input.lower() in p.lower()][:6]
            set_resultados(filtradas)
        set_mostrar_sugerencias(True)

    def elegir(pelicula):
        set_valor_input(pelicula)
        set_mostrar_sugerencias(False)

    async def enviar_texto(event=None):
        if valor_input.strip() != "" and valor_input in movies:
            set_enviado(valor_input)
            set_cargando(True)
            set_recomendaciones([])
            
            await asyncio.sleep(0.5)
            
            try:
                recs = KNN(valor_input)  # ✅ Usar KNN directamente
                set_recomendaciones(recs)
            except Exception as e:
                set_recomendaciones([f"Error: {str(e)}"])
            finally:
                set_cargando(False)

    return html.div(
        {
            "style": {
                "background": styles.STYLES['colors']['white'],
                "padding": "4rem 2rem",
                "minHeight": "60vh"
            }
        },
        html.div(
            {
                "style": {
                    "maxWidth": "800px",
                    "margin": "0 auto",
                    "textAlign": "center"
                }
            },

            html.h2(
                {
                    "style": {
                        "fontSize": "2.5rem",
                        "fontWeight": "700",
                        "marginBottom": "1rem",
                        "color": styles.STYLES['colors']['dark']
                    }
                },
                "Intelligent Search"
            ),
            html.p(
                {
                    "style": {
                        "fontSize": "1.1rem",
                        "color": "#6c757d",
                        "marginBottom": "3rem"
                    }
                },
                "Write a name of your movie"
            ),
            
            html.div(
                {
                    "style": {
                        "position": "relative",
                        "maxWidth": "600px",
                        "margin": "0 auto 3rem auto"
                    }
                },
                html.div(
                    {
                        "style": {
                            "display": "flex",
                            "gap": "0",
                            "boxShadow": styles.STYLES['shadows']['medium'],
                            "borderRadius": "50px",
                            "overflow": "hidden",
                            "background": styles.STYLES['colors']['white']
                        }
                    },
                    html.input(
                        {
                            "type": "text",
                            "placeholder": "Write a movie name here...",
                            "value": valor_input,
                            "onFocus": filtrar,
                            "onChange": lambda e: (set_valor_input(e["target"]["value"]), filtrar()),
                            "style": {
                                "flex": "1",
                                "padding": "1.2rem 1.5rem",
                                "border": "none",
                                "outline": "none",
                                "fontSize": "1.1rem",
                                "background": "transparent"
                            }
                        }
                    ),
                    html.button(
                        {
                            "onClick": enviar_texto,
                            "style": {
                                "padding": "1.2rem 2rem",
                                "background": f"linear-gradient(45deg, {styles.STYLES['colors']['primary']}, {styles.STYLES['colors']['secondary']})",
                                "color": styles.STYLES['colors']['white'],
                                "border": "none",
                                "cursor": "pointer",
                                "fontWeight": "600",
                                "fontSize": "1rem",
                                "transition": "all 0.3s ease",
                                "minWidth": "140px"
                            },
                            "onMouseOver": lambda e: e.target.update({
                                "style": {
                                    **e.target["style"],
                                    "transform": "scale(1.05)",
                                    "boxShadow": styles.STYLES['shadows']['large']
                                }
                            }),
                            "onMouseOut": lambda e: e.target.update({
                                "style": {
                                    **e.target["style"],
                                    "transform": "scale(1)",
                                    "boxShadow": "none"
                                }
                            })
                        },
                        "🎯 Search" if not cargando else "⏳ Loading..."
                    )
                ),
                
                (html.div(
                    {
                        "style": {
                            "position": "absolute",
                            "top": "100%",
                            "left": "0",
                            "right": "0",
                            "background": styles.STYLES['colors']['white'],
                            "borderRadius": "16px",
                            "boxShadow": styles.STYLES['shadows']['xl'],  # ✅ CORREGIDO
                            "zIndex": "1000",
                            "maxHeight": "300px",
                            "overflowY": "auto",
                            "marginTop": "0.5rem",
                            "border": f"1px solid {styles.STYLES['colors']['light']}"
                        }
                    },
                    html.ul(
                        {
                            "style": {
                                "listStyle": "none",
                                "margin": "0",
                                "padding": "0.5rem"
                            }
                        },
                        [
                            html.li(
                                {
                                    "key": f"suggestion-{i}",
                                    "style": {
                                        "padding": "1rem 1.5rem",
                                        "cursor": "pointer",
                                        "borderBottom": f"1px solid {styles.STYLES['colors']['light']}",
                                        "transition": "all 0.2s ease",
                                        "borderRadius": "8px",
                                        "marginBottom": "0.25rem"
                                    },
                                    "onClick": lambda e, peli=pelicula: elegir(peli),
                                    "onMouseOver": lambda e: e.target.update({
                                        "style": {
                                            **e.target["style"],
                                            "background": styles.STYLES['colors']['light'],
                                            "transform": "translateX(5px)"
                                        }
                                    }),
                                    "onMouseOut": lambda e: e.target.update({
                                        "style": {
                                            **e.target["style"],
                                            "background": "transparent",
                                            "transform": "translateX(0)"
                                        }
                                    })
                                },
                                f"🎬 {pelicula}"
                            ) for i, pelicula in enumerate(resultados)
                        ]
                    )
                ) if mostrar_sugerencias and resultados else None)
            ),
            
            (html.div(
                {
                    "style": {
                        "background": styles.STYLES['colors']['light'],
                        "padding": "2rem",
                        "borderRadius": "20px",
                        "boxShadow": styles.STYLES['shadows']['medium']
                    }
                },
                html.h3(
                    {
                        "style": {
                            "fontSize": "1.8rem",
                            "marginBottom": "1.5rem",
                            "color": styles.STYLES['colors']['dark'],
                            "display": "flex",
                            "alignItems": "center",
                            "justifyContent": "center",
                            "gap": "0.5rem"
                        }
                    },
                    html.span("✨"),
                    f"Recomendaciones similares a \"{enviado}\""
                ),
                
                (html.div(
                    {
                        "style": {
                            "textAlign": "center",
                            "padding": "3rem"
                        }
                    },
                    html.div(
                        {
                            "style": {
                                "width": "50px",
                                "height": "50px",
                                "border": f"4px solid {styles.STYLES['colors']['primary']}20",
                                "borderLeft": f"4px solid {styles.STYLES['colors']['primary']}",
                                "borderRadius": "50%",
                                "animation": "spin 1s linear infinite",
                                "margin": "0 auto"
                            }
                        }
                    ),
                    html.p(
                        {
                            "style": {
                                "marginTop": "1rem",
                                "color": styles.STYLES['colors']['dark']
                            }
                        },
                        "Analizando películas..."
                    )
                ) if cargando else
                
                html.div(
                    {
                        "style": {
                            "display": "grid",
                            "gridTemplateColumns": "repeat(auto-fit, minmax(280px, 1fr))",
                            "gap": "1.5rem",
                            "marginTop": "1rem"
                        }
                    },
                    [
                        MovieCard(rec, i) for i, rec in enumerate(recomendaciones)
                    ]
                ) if recomendaciones else None)
            ) if enviado else None)
        )
    )