#!/usr/bin/env python3
"""Creating End-point routes"""
from fastapi import APIRouter
from bson import ObjectId
from models.vendors import Vendors, UpdateVendors
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

@vendor.put("/{id}")
async def update_vendor(id: str, vendor: UpdateVendors):
    """Updating vendor list or id"""
    _id = ObjectId(id)
    _vendor = vendor_coll.find_one({"_id": ObjectId(id)})

    if not _vendor:
        return {"status": "error", "data": "Id not available"}
    to_update = dict(vendor)
    for _item, _val  in to_update.items():
        updates = {}
        if _val is not None:
            updates.update({str(_item): to_update.get(_item)})
            print(updates)
            vendor_coll.update_one({"_id": _id}, {
                "$set": updates
        })
    vendor_updated = vendor_coll.find_one({"_id": ObjectId(id)})
    return {"status": "ok", "data": vendor_updated}

