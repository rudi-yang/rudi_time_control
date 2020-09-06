import datetime
import traceback


class EntityTimeControl:
    def __init__(self):
        self.action = ""
        self.cate = ""
        self.detail = ""
        self.start_timestamp = None
        self.end_timestamp = None
        self.ds = None
        self.duration = None

    def build(self, action, cate, detail, start_timestamp, end_timestamp):
        self.action = action
        self.cate = cate
        self.detail = detail
        try:
            # 特殊情况处理
            if str(end_timestamp).endswith("2400"):
                end_timestamp = end_timestamp[:-4] + "2359"

            self.start_timestamp = datetime.datetime.strptime(start_timestamp, '%Y%m%d%H%M')
            self.end_timestamp = datetime.datetime.strptime(end_timestamp, '%Y%m%d%H%M')
            self.ds = int(start_timestamp[:8])
            duration = self.end_timestamp - self.start_timestamp
            self.duration = float(duration.seconds) / 3600
        except Exception as e:
            print(e)
            traceback.print_stack()
            print("输入格式有误，重新输入")
            return False
        return True
