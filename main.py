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
            print("最近两天的全部记录如下：")
            print(control.get_data_recent_2_days())
            print("*********************************************************")
            print("输入数据样例：吃饭 喝喜茶 真开心 202009071200 202009071300")
            print("*********************************************************")
            print("注意，每条输入只对应当天")

            input_action  = input(">>> 行为：")
            input_cate = input(">>> 类目：")
            input_detail  = input(">>> 具体：")
            input_start_timestamp = input(">>> 开始时间：")
            input_end_timestamp = input(">>> 结束时间：")
            try:
                content = control.instert_time_control(input_action, input_cate,input_detail,input_start_timestamp,input_end_timestamp)
            except Exception as e:
                print("插入失败,检查输入格式\n")
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
