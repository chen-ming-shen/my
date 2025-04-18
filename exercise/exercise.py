# 给定振动传感器数据：vibration = [2.1, 3.0, None, 2.8, 3.2, None, 2.9]
# 要求：1. 删除None值 2. 计算有效数据的平均值
vibration = [2.1, 3.0, None, 2.8, 3.2, None, 2.9]
# 你的代码写在这里
vibration_tmp=[v_tmp for v_tmp in vibration if v_tmp is not None]
print(sum(vibration_tmp)/len(vibration_tmp),vibration_tmp)

# 编写一个函数，输入转速(rpm)，返回角速度(rad/s)
# 公式：
def rpm_to_rads(rpm=None):
    # 你的代码写在这里
    try:
        if rpm==None:
            rpm=114
            print(rpm * 0.10472,"默认rpm=",rpm)
        else:
            rpm=float(input("输入转速(rpm)"))
            print(rpm * 0.10472)
    except Exception as e:
        print("输入了无效转速",e)
rpm_to_rads()

    #给定温度序列，连续3次超过阈值则触发报警
temps = [68, 72, 85, 87, 84, 70, 86, 88, 90]
threshold = 85
def check_alert(temps, threshold):
    # 你的代码写在这里
    third=[]
    Record=0
    for alarm_tmp in temps:
        if Record==3:
            break
        if alarm_tmp >threshold:
            third.append(alarm_tmp)
            Record+=1
        else:
            Record=0
            third=[]
    print("警报",third,"有",Record,"次连续超过阈值")
check_alert(temps, threshold)
