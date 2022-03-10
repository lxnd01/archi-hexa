# Application service
from python.order_placement.domain.function import place_orders
from python.request_for_offer.domain.functions import request_offers


def request_offer(booking_id: str):
    # lookup preferred address
    # select the right module and calls it
    request_offers()
    # convert response into user-friendly response
    # (record stats, logs...)
