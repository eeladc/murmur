from flask_restplus import fields
from api.api import api

trackable = api.model('Trackable', {
    'timestamp': fields.DateTime(dt_format='rfc822', description="Timestamp for time-series data"),
    'id': fields.Integer(description="Id field")
})

product = api.inherit('Product', trackable, {
    'productName': fields.String(description='Name of the product'),
    'productId': fields.Integer(description="Product id"),
    'branchId': fields.Integer(description="Shop id"),
    'supplierId': fields.Integer(description="Supplier id"),
    'brandName': fields.String(description="Brand name"),
    'promoCode': fields.String(description="Promocode"),
    'price': fields.String(description="Price"),
    'quantity': fields.String(description="Quantity"),
    'premiumPromotion': fields.Boolean(description="Is Premium Promotion"),
    'category': fields.String(description="Category"),
    'discount': fields.String(description="Attached Discount"),
    'context': fields.String(description="Product tracker context")
})

merchant = api.inherit('Merchant', trackable, {
    'merchantType': fields.String(description='Merchant Type'),
    'merchantId': fields.Integer(description="Merchant id"),
    'name': fields.Integer(description="Name"),
    'latitude': fields.Float(description="Latitude"),
    'longitude': fields.Float(description="Longitude"),
    'emailId': fields.String(description="Email id"),
    'price': fields.String(description="Price"),
    'subscriptionType': fields.String(description="Subscription Type"),
    'lob': fields.String(description="Line of business"),
    'context': fields.String(description="Merchant tracker context")
})

trackType = api.model('TrackType', {
    'product': fields.Nested(product),
    'merchant': fields.Nested(merchant)
})

track_data = api.model('Track', {
    'type': fields.String(required=True, description='Type of tracked data'),
    'data': fields.Nested(trackType, required=True, description="Trackable data")
})

page_request = api.model('Page request', {
    'page_no': fields.Integer(description='Page number'),
    'page_size': fields.Integer(description='Page sie'),
})

search_track = api.model('Search', {
    'type': fields.String(required=True, description='Type of data'),
    'text': fields.String(required=True, description='Search text'),
    'fields': fields.List(fields.String, description='Query fields'),
    'pageRequest': fields.Nested(page_request, description='Pagination request')
})

