# Backend-for-Frontend (the only module that can know every other)
from python import request_for_offer
from python.order_placement.application.application_service import place_client_order
from python.order_placement.domain.function import place_orders

# TODO create REST controllers calling the code below
from python.part_identification.function import product_id_from_chain_criteria


def search_tyres(tyre_size: Tyre_spec):
    blah = product_id_from_chain_criteria()
# if not empty
    request_for_offer(blah)



def book(booking_id: str):
# check connected
# check locale
# ----- start application service
    place_client_order(booking_id)
#----- end application
# return response

