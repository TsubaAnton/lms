import stripe
from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_product(product):
    """Создает продукт в Stripe"""
    stripe_product = stripe.Product.create(name=product.name)
    return stripe_product


def create_price(amount, product):
    """Создает цену в Stripe"""
    stripe_price = stripe.Price.create(
        currency="rub",
        unit_amount=int(amount) * 100,
        product=product.id,
    )
    return stripe_price


def create_session(price):
    """Создает сессию в Stripe"""
    stripe_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{"price": price.id, "quantity": 1}],
        mode="payment",
        success_url="http://http://127.0.0.1:8000/",
        cancel_url='http://127.0.0.1:8000/cancel',
    )
    return stripe_session.id, stripe_session.url, stripe_session.status
