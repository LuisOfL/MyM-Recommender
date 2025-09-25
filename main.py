from reactpy import component, html, run, hooks
from reactpy.backend.fastapi import configure
from fastapi import FastAPI
import pandas as pd
import back
import asyncio

app = FastAPI()
df = pd.read_csv("dataset/titles.csv")
movies = df['title'].astype(str).tolist()


STYLES = {
    "colors": {
        "primary": "#667eea",
        "primary_dark": "#5a6fd8",
        "secondary": "#764ba2",
        "accent": "#f093fb",
        "light": "#f8f9fa",
        "dark": "#343a40",
        "success": "#28a745",
        "white": "#ffffff"
    },
    "shadows": {
        "small": "0 2px 4px rgba(0,0,0,0.1)",
        "medium": "0 4px 6px rgba(0,0,0,0.1)",
        "large": "0 10px 15px rgba(0,0,0,0.1)",
        "xl": "0 20px 25px rgba(0,0,0,0.1)"
    },
    "breakpoints": {
        "mobile": "768px",
        "tablet": "1024px"
    }
}


@component
def Header():
    return html.header(
        {
            "style": {
                "background": f"linear-gradient(135deg, {STYLES['colors']['primary']} 0%, {STYLES['colors']['secondary']} 100%)",
                "color": STYLES['colors']['white'],
                "padding": "1.5rem 2rem",
                "boxShadow": STYLES['shadows']['medium'],
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
                            "background": STYLES['colors']['white'],
                            "borderRadius": "12px",
                            "display": "flex",
                            "alignItems": "center",
                            "justifyContent": "center",
                            "fontWeight": "bold",
                            "color": STYLES['colors']['primary'],
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
                            "background": f"linear-gradient(45deg, {STYLES['colors']['white']}, {STYLES['colors']['accent']})",
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
                            "color": STYLES['colors']['white'],
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


@component
def HeroSection():
    return html.section(
        {
            "style": {
                "background": f"linear-gradient(135deg, {STYLES['colors']['light']} 0%, #e2e8f0 100%)",
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
                    "background": f"radial-gradient(circle, {STYLES['colors']['primary']}20 0%, transparent 70%)",
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
                        "background": f"linear-gradient(45deg, {STYLES['colors']['primary']}, {STYLES['colors']['secondary']})",
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
                        "color": STYLES['colors']['dark'],
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


@component
def MovieCard(movie_title, index):
    return html.div(
        {
            "style": {
                "background": STYLES['colors']['white'],
                "borderRadius": "16px",
                "padding": "1.5rem",
                "boxShadow": STYLES['shadows']['small'],
                "transition": "all 0.3s ease",
                "border": f"2px solid {STYLES['colors']['light']}",
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
                    "boxShadow": STYLES['shadows']['large'],
                    "borderColor": STYLES['colors']['primary']
                }
            }),
            "onMouseOut": lambda e: e.target.update({
                "style": {
                    **e.target["style"],
                    "transform": "translateY(0)",
                    "boxShadow": STYLES['shadows']['small'],
                    "borderColor": STYLES['colors']['light']
                }
            })
        },
        html.div(
            {
                "style": {
                    "position": "absolute",
                    "top": "0.5rem",
                    "left": "0.5rem",
                    "background": STYLES['colors']['primary'],
                    "color": STYLES['colors']['white'],
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
                    "color": STYLES['colors']['dark'],
                    "fontSize": "1.1rem",
                    "fontWeight": "600",
                    "lineHeight": "1.4"
                }
            },
            movie_title
        )
    )

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
                recs = back.KNN(valor_input)
                set_recomendaciones(recs)
            except Exception as e:
                set_recomendaciones([f"Error: {str(e)}"])
            finally:
                set_cargando(False)

    return html.div(
        {
            "style": {
                "background": STYLES['colors']['white'],
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
                        "color": STYLES['colors']['dark']
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
                            "boxShadow": STYLES['shadows']['medium'],
                            "borderRadius": "50px",
                            "overflow": "hidden",
                            "background": STYLES['colors']['white']
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
                                "background": f"linear-gradient(45deg, {STYLES['colors']['primary']}, {STYLES['colors']['secondary']})",
                                "color": STYLES['colors']['white'],
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
                                    "boxShadow": STYLES['shadows']['large']
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
                            "background": STYLES['colors']['white'],
                            "borderRadius": "16px",
                            "boxShadow": STYLES['shadows']['xl'],
                            "zIndex": "1000",
                            "maxHeight": "300px",
                            "overflowY": "auto",
                            "marginTop": "0.5rem",
                            "border": f"1px solid {STYLES['colors']['light']}"
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
                                        "borderBottom": f"1px solid {STYLES['colors']['light']}",
                                        "transition": "all 0.2s ease",
                                        "borderRadius": "8px",
                                        "marginBottom": "0.25rem"
                                    },
                                    "onClick": lambda e, peli=pelicula: elegir(peli),
                                    "onMouseOver": lambda e: e.target.update({
                                        "style": {
                                            **e.target["style"],
                                            "background": STYLES['colors']['light'],
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
                        "background": STYLES['colors']['light'],
                        "padding": "2rem",
                        "borderRadius": "20px",
                        "boxShadow": STYLES['shadows']['medium']
                    }
                },
                html.h3(
                    {
                        "style": {
                            "fontSize": "1.8rem",
                            "marginBottom": "1.5rem",
                            "color": STYLES['colors']['dark'],
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
                                "border": f"4px solid {STYLES['colors']['primary']}20",
                                "borderLeft": f"4px solid {STYLES['colors']['primary']}",
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
                                "color": STYLES['colors']['dark']
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


@component
def Footer():
    return html.footer(
        {
            "style": {
                "background": STYLES['colors']['dark'],
                "color": STYLES['colors']['white'],
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


@component
def App():
    return html.div(
        {
            "style": {
                "margin": "0",
                "padding": "0",
                "minHeight": "100vh",
                "fontFamily": "'Inter', 'Segoe UI', system-ui, sans-serif",
                "background": STYLES['colors']['light']
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