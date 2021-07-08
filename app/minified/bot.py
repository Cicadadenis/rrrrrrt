import logging.config
z=True
from pathlib import Path
from aiogram import Bot,Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from rich.logging import RichHandler
from app.misc import ModuleManager,parse_config,PhotoStorage
L=Path(__file__).parent.parent
Q=parse_config(L/"config.yaml")
v=PhotoStorage(L/"images.txt")
x=Bot(**config.get("bot"))
H=MemoryStorage()
dp=Dispatcher(x,storage=H)
for g in config.get("log_ignore"):
 U=logging.getLogger(g)
 U.disabled=z
logging.basicConfig(level="NOTSET",format="%(message)s",datefmt="[%X]",handlers=[RichHandler()])
# Created by cicadacrypto Cicada3301(https://github.com/Cicada)
