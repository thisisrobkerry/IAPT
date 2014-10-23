def books():
    return dict(products= db(db.Products.type == 'Book').select())

def videos():
    return dict()
