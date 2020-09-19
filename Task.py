#
# タスク管理
#
from datetime import datetime, tzinfo
import json
from uuid import uuid4

class Task():
    def __init__(self, title: str = "", content: str = "", limit = None):
        self.taskID = str(uuid4())
        self.title = title
        self.content = content
        if limit is not None:
            self.limit = limit
        else:
            self.limit = datetime.fromtimestamp(86400)

    # オブジェクトに変換
    def getObject(self):
        taskObject = {"taskID": self.taskID, "title": self.title, "content": self.content, "limit": self.limit.timestamp()}
        return taskObject

    # json文字列からTaskオブジェクトに
    @staticmethod
    def convertFromJson(json: str):
        jsonObj = json.loads(json)
        rst = -1
        try:
            self.title = jsonObj['title']
            self.content = jsonObj['content']
            self.limit = datetime.fromtimestamp(float(jsonObj['limit']))
            rst = 0
        except KeyError:
            rst = 1
        except TypeError:
            rst = 2

        finally:
            return rst