from dataclasses import dataclass

@dataclass
class TaskRunSubscriberRequest:
    uuid: str
    code: str
    answer: str
    time_limit: int


@dataclass
class TaskRunCacheRequest:
    uuid: str
    res: bool
    completed_time: float

    def get_data(self):
        data = self.__dict__
        del data["uuid"]
        return data
