import justpy as jp
import json

import definition

class Doc:
    path = "/about"

    @classmethod
    def serve(cls, req):
        wp = jp.WebPage()

        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")

        jp.Div(a=div, text="Instant Dictionary API",  classes="text-4xl m-2")
        jp.Div(a=div, text="Get definitions of words",  classes="text-lg")
        jp.Hr(a=div)
        jp.Div(a=div, text="www.example.com/api?w=moon")
        jp.Hr(a=div)
        defined = definition.Definition("moon").get()
        response = {
            "word": "moon",
            "definition": defined
        }
        jp.Div(a=div, text=f"{json.dumps(response)}")

        return wp

