#!/usr/bin/env python3
"""Creating End-point routes"""
from fastapi import APIRouter
from models.vendors import Vendors
from config.db import vendor_coll, product_coll
from schemas.vendor import vendorEntity, all_vendors

vendor = APIRouter()

@vendor.get('/vendor')
async def get_vendors():
    print(vendor_coll.find())
    print(vendorEntity(vendor_coll.find()))
    return vendorEntity(vendor_coll.find())
