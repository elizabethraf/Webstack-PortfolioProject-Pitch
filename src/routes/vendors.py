#!/usr/bin/env python3
"""Creating End-point routes"""
from fastapi import APIRouter
from bson import ObjectId
from models.vendors import Vendors
from config.db import vendor_coll, product_coll
from schemas.vendor import vendorEntity, many_vendors

vendor = APIRouter(
        prefix='/vendors',
        tags=['Vendors']
        )

@vendor.get("/")
async def all_vendors():
    """"Fetching all vendors"""
    _vendors = many_vendors(vendor_coll.find())
    return {"status": "ok", "data": _vendors}

@vendor.get("/{id}")
async def get_vendor(id: str):
    """Fetching vendors where "id' is = id"""
    _id = ObjectId(id)
    _vendor = vendor_coll.find_one({"_id": _id})
    return vendorEntity(_vendor)

@vendor.post("/")
async def post_vendor(vendor: Vendors):
    """Creating new Vendor"""
    _id = vendor_coll.insert_one(dict(vendor))
    vendor = vendorEntity(vendor_coll.find_one({"_id": _id.inserted_id}))
    return {"status": "ok", "data": vendor}

