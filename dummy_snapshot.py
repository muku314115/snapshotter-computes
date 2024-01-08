import time
from typing import List, Tuple, Union
from pydantic import BaseModel
from ipfs_client.main import AsyncIPFSClient
from redis import asyncio as aioredis
from snapshotter.utils.callback_helpers import GenericProcessor
from snapshotter.utils.default_logger import logger
from snapshotter.utils.models.message_models import SnapshotProcessMessage
from snapshotter.utils.rpc import RpcHelper

from .redis_keys import uniswap_v2_monitored_pairs
from .utils.core import get_pair_reserves
from .utils.models.message_models import EpochBaseSnapshot


class DummySnapshotModel(BaseModel):
    dummy: str


class DummySnapshotGenerator(GenericProcessor):
    transformation_lambdas = None

    def __init__(self) -> None:
        self.transformation_lambdas = []
        self._logger = logger.bind(module='DummySnapshotGenerator')

    async def compute(
        self,
        msg_obj: SnapshotProcessMessage,
        redis: aioredis.Redis,
        rpc_helper: RpcHelper,
        anchor_rpc_helper: RpcHelper,
        ipfs_reader: AsyncIPFSClient,
        protocol_state_contract,

    ) -> Union[None, List[Tuple[str, DummySnapshotModel]]]:  
        return [
            (
                '0xFB0cd42862824030e98D7c60Ef4FeBb3dA44cd09',
                DummySnapshotModel(dummy='dummy')
            )
        ]
