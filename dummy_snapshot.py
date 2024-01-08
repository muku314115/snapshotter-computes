from pydantic import BaseModel
from typing import List
from typing import Tuple
from typing import Union

from redis import asyncio as aioredis
from snapshotter.utils.callback_helpers import GenericProcessorSnapshot
from snapshotter.utils.default_logger import logger
from snapshotter.utils.models.message_models import EthTransactionReceipt
from snapshotter.utils.models.message_models import PowerloomSnapshotProcessMessage
from snapshotter.utils.redis.redis_keys import epoch_txs_htable
from snapshotter.utils.rpc import RpcHelper


class DummySnapshotModel(BaseModel):
    dummy: str


class DummySnapshotGenerator(GenericProcessorSnapshot):
    transformation_lambdas = None

    def __init__(self) -> None:
        self.transformation_lambdas = []
        self._logger = logger.bind(module='DummySnapshotGenerator')

    async def compute(
        self,
        epoch: PowerloomSnapshotProcessMessage,
        redis_conn: aioredis.Redis,
        rpc_helper: RpcHelper,

    ) -> Union[None, List[Tuple[str, DummySnapshotModel]]]:  
        return [
            (
                '0xFB0cd42862824030e98D7c60Ef4FeBb3dA44cd09',
                DummySnapshotModel(dummy='dummy')
            )
        ]
