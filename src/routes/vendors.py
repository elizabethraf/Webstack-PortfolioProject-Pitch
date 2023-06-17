#!/usr/bin/env python3
"""Creating End-point routes"""
from fastapi import APIRouter
from bson import ObjectId
from models.vendors import Vendors
from config.db import vendor_coll, product_coll
from schemas.vendor import vendorEntity, all_vendors

vendor = APIRouter(
        prefix='/vendor',
        tags=['Vendors']
        )

@vendor.get('/')
async def all_vendors():
    """"Fetching all vendors"""
    print(all_vendors(vendor_coll.find()))
    return all_vendors(vendor_coll.find())

@vendor.get('/{id}')
async def get_vendor(id: str):
    """Fetching vendors where "id' is = id"""
    print(all_vendors(vendor_coll.find({"_id": ObjectId(id)})))
    return all_vendors(vendor_coll.find({"_id": ObjectId(id)}))
