""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class Product(Model):
    def __init__(self):
        super(Product, self).__init__()

    def get_all(self):
        query = "SELECT * FROM products"
        return self.db.query_db(query)

    def add_product(self, request_form):
        errors = []
        if request_form:
            if request_form['product_name']:
                if len(request_form['product_name']) < 2:
                    errors.append("You must enter at least two characters")
            else:
                errors.append("Name cannot be blank!")
            if request_form['product_description']:
                if len(request_form['product_description']) < 2:
                    errors.append("You must enter at least two characters")
            else:
                errors.append("Description cannot be blank!")
            if request_form['product_price']:
                if len(request_form['product_price']) < 2:
                    errors.append("You must enter at least two characters")
            else:
                errors.append("Price cannot be blank!")
        else:
            errors.append("You must enter something here")

        if errors:
            return {"status": False, "errors": errors}

        query = "INSERT INTO products (name, description, price, created_at, updated_at) VALUES (:name, " \
                ":description, :price, NOW(), NOW())"
        data = {
            "name": request_form['product_name'],
            "description": request_form['product_description'],
            "price": format(float(request_form['product_price']), '.2f')
        }
        result = self.db.query_db(query, data)
        if result:
            return {"status": True, "result": result}
        return {"status": False, "errors": errors}

    def edit_product(self, request_form, product_id):
        errors = []

        if request_form:
            if request_form['product_name']:
                if len(request_form['product_name']) < 2:
                    errors.append("You must enter at least two characters")
            else:
                errors.append("Name cannot be blank!")
            if request_form['product_description']:
                if len(request_form['product_description']) < 2:
                    errors.append("You must enter at least two characters")
            else:
                errors.append("Description cannot be blank!")
            if request_form['product_price']:
                if len(request_form['product_price']) < 2:
                    errors.append("You must enter at least two characters")
            else:
                errors.append("Price cannot be blank!")
        else:
            errors.append("You must enter something here")

        if errors:
            return {"status": False, "errors": errors}

        query = "UPDATE products SET name=:name, description=:description, price=:price, updated_at=NOW() WHERE " \
                "product_id=:product_id"

        data = {
            "name": request_form['product_name'],
            "description": request_form['product_description'],
            "price": format(float(request_form['product_price']), '.2f'),
            "product_id": product_id
        }

        self.db.query_db(query, data)
        return {"status": True}

    def get_one(self, product_id):
        query = "SELECT * FROM products WHERE product_id=:product_id LIMIT 1"
        data = {
            "product_id": product_id
        }
        result = self.db.get_one(query, data)
        if result:
            return {"status": True, "result": result}
        return {"status": False}

    def delete(self, product_id):
        query = "DELETE FROM products WHERE product_id=:product_id"
        data = {
            "product_id": product_id
        }
        self.db.query_db(query, data)
        return {"status": True}