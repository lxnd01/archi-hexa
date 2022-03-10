# Application service
from python.order_placement.domain.function import place_orders


def save_booking_decision():
    pass


def place_client_order(booking_id: str):
    save_booking_decision()
    # lookup preferred address
    # select the right module and calls it
    # load the booking (shopping cart) by id
    # convert the shopping cart into a client_order
    place_orders(client_order=None, )
    # convert response into user-friendly response
    # (record stats, logs...)
