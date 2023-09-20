import justpy as jp

import api
import documentation

jp.Route("/api", api.Api.serve)
jp.Route("/", documentation.Doc.serve)
jp.justpy()
