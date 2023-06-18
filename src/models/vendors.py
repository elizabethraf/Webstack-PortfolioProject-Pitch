#!/usr/bin/env python3
"""Database Model for vendors"""
from pydantic import BaseModel
from typing import Optional


class Vendors(BaseModel):
    name: str
    email: Optional[str] = None
    location: str
    contact_number: str

class UpdateVendors(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    location: Optional[str] = None
    contact_number: Optional[str] = None
