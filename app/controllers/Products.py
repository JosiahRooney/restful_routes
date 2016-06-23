"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Products(Controller):
    def __init__(self, action):
        super(Products, self).__init__(action)
        self.load_model('Product')
        self.db = self._app.db
   
    def index(self):
        products = self.models['Product'].get_all()
        for product in products:
            product['price'] = round(product['price'],2)
        return self.load_view('index.html', products=products)

    def add(self):
        return self.load_view('edit.html', add=True)

    def edit(self, product_id):
        product = self.models['Product'].get_one(product_id)
        if product:
            return self.load_view('edit.html', edit=True, product=product['result'])
        flash("There is no product with the id of "+str(product_id), "error")
        return redirect('/')

    def add_process(self):
        result = self.models['Product'].add_product(request.form)
        if result['status']:
            flash("Product added!","success")
        else:
            flash("There was a problem adding your product, try again", "error")
            return redirect('/product/add')
        return redirect('/')

    def edit_process(self, product_id):
        result = self.models['Product'].edit_product(request.form, product_id)
        if result['status']:
            flash("Product updated!","success")
        else:
            flash("There was a problem updating your product, try again", "error")
            return redirect('/product/'+str(product_id)+'/edit')
        return redirect('/')

    def show(self, product_id):
        result = self.models['Product'].get_one(product_id)
        if not result['status']:
            flash("There is no product with the id of "+str(product_id), "error")
            return redirect('/')
        return self.load_view('show.html', product=result['result'])

    def delete(self, product_id):
        result = self.models['Product'].delete(product_id)
        if not result['status']:
            flash("There is no product with the id of "+str(product_id), "error")
        else:
            flash("Product successfully deleted", "success")
        return redirect('/')