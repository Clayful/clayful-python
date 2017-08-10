from brand import Brand
from cart import Cart
from collection import Collection
from country import Country
from coupon import Coupon
from currency import Currency
from customer import Customer
from discount import Discount
from downloadable import Downloadable
from group import Group
from image import Image
from order import Order
from order_tag import OrderTag
from payment_method import PaymentMethod
from product import Product
from review import Review
from review_comment import ReviewComment
from shipping_method import ShippingMethod
from store import Store
from subscription import Subscription
from tax_category import TaxCategory
from warehouse import Warehouse
from wish_list import WishList

def register(clayful):

	setattr(clayful, 'Brand', Brand.config(clayful))
	setattr(clayful, 'Cart', Cart.config(clayful))
	setattr(clayful, 'Collection', Collection.config(clayful))
	setattr(clayful, 'Country', Country.config(clayful))
	setattr(clayful, 'Coupon', Coupon.config(clayful))
	setattr(clayful, 'Currency', Currency.config(clayful))
	setattr(clayful, 'Customer', Customer.config(clayful))
	setattr(clayful, 'Discount', Discount.config(clayful))
	setattr(clayful, 'Downloadable', Downloadable.config(clayful))
	setattr(clayful, 'Group', Group.config(clayful))
	setattr(clayful, 'Image', Image.config(clayful))
	setattr(clayful, 'Order', Order.config(clayful))
	setattr(clayful, 'OrderTag', OrderTag.config(clayful))
	setattr(clayful, 'PaymentMethod', PaymentMethod.config(clayful))
	setattr(clayful, 'Product', Product.config(clayful))
	setattr(clayful, 'Review', Review.config(clayful))
	setattr(clayful, 'ReviewComment', ReviewComment.config(clayful))
	setattr(clayful, 'ShippingMethod', ShippingMethod.config(clayful))
	setattr(clayful, 'Store', Store.config(clayful))
	setattr(clayful, 'Subscription', Subscription.config(clayful))
	setattr(clayful, 'TaxCategory', TaxCategory.config(clayful))
	setattr(clayful, 'Warehouse', Warehouse.config(clayful))
	setattr(clayful, 'WishList', WishList.config(clayful))
