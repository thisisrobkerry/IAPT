# -*- coding: utf-8 -*-
# @IAPT: Very simple controller

def index():
    return dict(features=db(db.Products.id==db.Features.product_id).select())

def search():
    return dict(request.vars)
