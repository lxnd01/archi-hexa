import abc

from python.request_for_offer.domain.functions import Partners, Offer


class FakePartners(Partners):
    def __init__(self, expected_results):
        self._expected_results = expected_results

    def request_offers_for_distributor(self, distributor, products_by_distributor) -> list[Offer]:
        return self._expected_results


class DistributorGateway(abc.ABC):

    @abc.abstractmethod
    def distributor(self) -> str:
        pass


class ExadisGateway(DistributorGateway):
    def distributor(self) -> str:
        return "exadis"


class ExadisSOAPGateway:
    pass


class IDPL_FTP_Gateway:
    pass


class PartnersGateway(Partners):

    def __init__(self, gateways: list[DistributorGateway]):
        self._gateways = gateways

    def request_offers_for_distributor(self, distributor, products_by_distributor) -> list[Offer]:
        # select (lookup) the gateway for the given distributor and call it
        if distributor.name == "exadis":
            return ExadisSOAPGateway.invoke(products_by_distributor)
        if distributor.name == "idpl":
            return IDPL_FTP_Gateway.invoke(products_by_distributor)
        if distributor.name == "exadis":
            return ExadisSOAPGateway.invoke(products_by_distributor)
