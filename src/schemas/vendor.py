#!/usr/bin/env python3
"""Creating Schemas for data and input validation"""

def vendorEntity(item) -> dict:
    """Display vendor information"""
    return {
            "id": item["_id"].toString(),
            "name": item["name"],
            "email": item["email"],
            "location": item["location"],
            "contact number": item["contact_number"]
            }


def all_vendors(all_entities) -> list:
    """Define all vendors on display"""
    return [vendorEntity(item) for item in entities]
