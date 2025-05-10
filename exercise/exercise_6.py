#请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：
class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self._gender = gender
    def get_gender(self):
        return self._gender
    def set_gender(self,tmp):
        self._gender=tmp 
        return self._gender

# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('1测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('2测试失败!',bart.get_gender())
    else:
        print('测试成功!')
        
        
        
# 尝试完成这个函数来检测当前水平
def dynamic_temperature(step,total_steps):
    """
    实现温度动态衰减：生成前30%步骤用高温(1.2)探索，
    中间50%用中温(0.9)，最后20%用低温(0.5)收束
    """
    # 你的代码写在这里
    percentage=step/total_steps
    if percentage<=0.3:
        return 1.2
    elif 0.3<percentage<=0.8:
        return 0.9
    else:
        return 0.5
for _ in range(1,11):
    print(dynamic_temperature(_,10),)
