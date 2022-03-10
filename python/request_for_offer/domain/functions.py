import abc
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Mapping

from python.part_identification.function import ProductID, Segment


@dataclass(frozen=True)
class Distributor:
    name: str
    _supported_segments: list[Segment]

    def supports(self, segment: Segment) -> bool:
        return segment in self._supported_segments


distributors = [
    Distributor("exadis", _supported_segments=[Segment.CHAIN, Segment.PART]),
    Distributor("idpl", _supported_segments=[Segment.TYRE, Segment.OIL]),
]

class Address:
    pass

class Offer:
    product_id: ProductID
    description: str
    retail_price: Decimal
    delivery_date: datetime
    valid_until: datetime
    from_distributor: Distributor

# TODO kata unit tests
def group_by_segment(products):
    pass

# TODO kata unit tests
def products_for_distributor(products_by_segment, distributor: Distributor):
    pass

# TODO kata unit tests
def curate_offers(offers):
    pass


class Partners(abc.ABC):

    @abc.abstractmethod
    def request_offers_for_distributor(self, distributor, products_by_distributor):
        pass

# TODO call pricing and add our margin to prices (another class, inject a Pricer class to it)
def post_process(offers):
    return offers;


def request_offers(products: list[ProductID], adress: Address, partners: Partners) -> list[Offer]:
    offers = []
    products_by_segment: Mapping[Segment, list[ProductID]] = group_by_segment(products)
    for distributor in distributors:
        products_by_distributor: list[ProductID]  = products_for_distributor(products_by_segment, distributor)
        offers_for_distributor: list[Offer] = partners.request_offers_for_distributor(distributor, products_by_distributor)
        offers.extend(offers_for_distributor)
    return post_process(offers)

