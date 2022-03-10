import abc
from decimal import Decimal

from python.part_identification.function import ProductID


class Distributor:
    pass

class Offer:
    product_id: ProductID # or SKU
    distributor: Distributor

class OrderLine:
    quantity: Decimal
    offer: Offer

# Multi-distributor
class Workshop:
    pass


class Address:
    pass


class ClientOrder:
    workshop: Workshop
    address: Address
    order_lines : list[OrderLine]

class DistributorOrder:
    distributor: Distributor
    order_lines: list[OrderLine] # may be a subset of the client order
    from_client_order: ClientOrder # traceability


def group_by_distributor(order_lines):
    pass


def prepare_orders(client_order: ClientOrder) -> list[DistributorOrder]:
    # split order lines of the client order by distributor
    subsets: dict[Distributor, list[OrderLine]] = group_by_distributor(client_order.order_lines)
    return [DistributorOrder(distributor, subset, client_order) for distributor, subset in subsets.items()]
    # invoke for each distributor


class OrderPartners(abc.ABC):
    @abc.abstractmethod
    def place_order_for_distributor(self, distributor_order: DistributorOrder):
        raise NotImplementedError


def place_orders(client_order: ClientOrder, partners: OrderPartners):
    distributor_orders = prepare_orders(client_order)
    for distributor_order in distributor_orders:
        partners.place_order_for_distributor(distributor_order)
