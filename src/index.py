#!/usr/bin/env python3
"""Display The presentation root"""
from fastapi import FastAPI
import json
from routes.vendors import vendor

app = FastAPI()
app.include_router(vendor)

@app.get("/")
def read_index():
    """Display Health Status for the API"""
    return {"Health": "Ok"}


