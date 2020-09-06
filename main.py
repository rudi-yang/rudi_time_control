from rudi_controller import RudiControl
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 5000)

control = RudiControl()

while True:
    try:
        Description = """>>> 选择你的输入\n\t1:显示所有数据\n\t2:显示时间分布\n\t3:插入记录\n\t4:删除记录\n>>>:"""
        action_id = input(Description)
        action_id = int(action_id)
        if action_id == 1:
            print(control.get_data_all())
        elif action_id == 2:
            day_duration = input(">>> 选择观察的天数")
            day_duration = int(day_duration)
            control.show_time_distribution_till_now(day_duration)
        elif action_id == 3:
            # 吃饭 鱼香肉丝 吃的很开心 202009061200 202009062000
            print(control.get_data_recent_2_days())
            content = input(">>> 输入插入记录:")
            content = content.split(" ")
            print("输入内容为:", content)
            try:
                content = control.instert_time_control(*content)
            except Exception as e:
                print("插入失败,检查输入格式")
        elif action_id == 4:
            ids = input(">>> 输入要删除的记录id:")
            ids = ids.split(",")
            for id in ids:
                control.delete_time_control_by_id(int(id))
        else:
            print("...输入有误，重新输入")
    except Exception as e:
        print("出现未知错误")
        continue
