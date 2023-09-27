from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote
import requests

from sqlalchemy.exc import IntegrityError

#from models import Session, Produto, Comentario
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="Loja API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Doc", description="Doc selection: Swagger, Redoc ou RapiDoc: Swagger, Redoc ou RapiDoc")
product_tag = Tag(name="Products", description="View products")
order_tag = Tag(name="Orders", description="Addition, view and exclusion of orders")

@app.get('/', tags=[home_tag])
def home():
    """Redirect to /openapi, options of different kinds of docs.
    """
    return redirect('/openapi')

@app.get('/order', tags=[order_tag])
def get_order(query: OrderViewSchema):
    """Return an specific order by a given id

    Return the order with all key values.
    """
    url = 'http://127.0.0.1:5000/order?id={id}'.format(id = query.id)
    orderApi = requests.get(url)
    return orderApi.json()

@app.get('/orders', tags=[order_tag])
def get_orders():
    """Return all orders in the db

    Return a list of orders.
    """
    url = 'http://127.0.0.1:5000/orders'
    orderApi = requests.get(url)
    return orderApi.json()

@app.get('/product', tags=[product_tag])
def get_product(query: ProductViewSchema):
    """Return product from external API by specific id

    Return the product with all key values.
    """
    url = 'https://fakestoreapi.com/products/{id}'.format(id = query.id)
    orderApi = requests.get(url)
    return orderApi.json()


@app.get('/products', tags=[product_tag])
def get_products():
    """Return all products from the external API

    Return a list of products.
    """
    url = 'https://fakestoreapi.com/products'
    orderApi = requests.get(url)
    return orderApi.json()

    
@app.post('/order', tags=[order_tag])
def create_order(form: OrderSchema):
    """Add new oredr in the db

    Return the order with all key values.
    """
    url = 'http://127.0.0.1:5000/order'
    dataForm = {
        'product_id': form.product_id,
        'quantity': form.quantity
    } 
    orderApi = requests.post(url, data=dataForm)
    return orderApi.json()

@app.put('/order', tags=[order_tag])
def update_order(form: OrderUpdateSchema):
    """Update one order in the db

    Return the updated order.
    """
    url = 'http://127.0.0.1:5000/order'
    dataForm = {
        'id': form.id,
        'quantity': form.quantity
    }
    orderApi = requests.put(url, data=dataForm)
    return orderApi.json()

@app.delete('/order', tags=[order_tag])
def delete_order(form: OrderDelSchema):
    """Delete an order by a given id

    Return a message of success and the deleted order id.
    """
    url = 'http://127.0.0.1:5000/order'
    order_id = form.id
    dataForm = {
        'id': form.id
    }
    orderApi = requests.delete(url, data=dataForm)
    return orderApi.json()
