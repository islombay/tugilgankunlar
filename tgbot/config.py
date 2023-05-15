import os
from dataclasses import dataclass

from environs import Env
from typing import List


@dataclass
class DbConfig:
    path: str


@dataclass
class TgBot:
    token: str
    admin_ids: List[int]


@dataclass
class Miscellaneous:
    other_params: str = None


@dataclass
class Config:
    tg_bot: TgBot
    db: DbConfig
    misc: Miscellaneous


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env.str("BOT_TOKEN"),
            admin_ids=list(map(int, env.list("ADMINS")))
        ),
        db=DbConfig(
            path=env.str("DB_PATH")
        ),
        misc=Miscellaneous()
    )
