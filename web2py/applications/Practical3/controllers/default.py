# -*- coding: utf-8 -*-
# @IAPT: Very simple controller

def index():
    return dict(features=db(db.Products.id==db.Features.product_id).select())

def search():
    form=FORM('Search Products', INPUT(_name='search', requires=IS_NOT_EMPTY()), INPUT(_type='submit'))
    if form.accepts(request, session):
        response.flash = 'Search success!'
        results = dict(result=db.Products.name.contains(request.vars))
    elif form.errors:
        response.flash = 'Search went bad :('
        results = dict(none = "no results")
    else:
        response.flash = 'Please enter a search term'
        results = dict(none = "no results")
    return dict(form=form, results=results)
