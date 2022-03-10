from dataclasses import dataclass
from enum import Enum


class TireSize:
    pass


class IDType(Enum):
    EAN = "EAN"
    TECDOC = "Tecdoc"


class Segment(Enum):
    CHAIN = "chain"
    TYRE = "tyre"
    OIL = "oil"
    PART = "tecdoc"


@dataclass(frozen=True)
class ProductID:
    id_type: IDType
    id_value: str
    segment: Segment


class Chain:
    def ean(self) -> str:
        return ""


class ChainDB:
    def query(self) -> list[Chain]:
        return []

def product_id_from_chain_criteria(tire_size: TireSize) -> list[ProductID]:
    chains = ChainDB.query(tire_size)
    product_ids = [_product_id_chain(chain) for chain in chains]


def _product_id_chain(chain: Chain) -> ProductID:
    return ProductID(id_type=IDType.EAN, id_value=chain.ean())


class TecdocPart:
    def tecdoc_number(self) -> str:
        return ""


class TecdocService:
    def query(self, plate, part_type) -> list[TecdocPart]:
        return []


def product_id_from_plate_and_part_type(plate, part_type) -> list[ProductID]:
    tecdoc_parts = TecdocService.query(plate, part_type)
    product_ids = [_product_id_tecdoc(tecdoc_part) for tecdoc_part in tecdoc_parts]


def _product_id_tecdoc(tecdoc_part) -> ProductID:
    return ProductID(id_type=IDType.TECDOC, id_value=tecdoc_part.tecdoc_number())