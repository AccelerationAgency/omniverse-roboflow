import time
import asyncio
import json
import io
from roboflow import Roboflow

class RoboflowHelper(Roboflow):
    def __init__(
        self,
        api_key: str = None
    ):
        super().__init__(api_key)
        print("initialized!!!")