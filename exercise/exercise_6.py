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
    
    
    
    
#为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：
class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count+=1

# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')
            
#利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
class Screen(object):
    def __init__(self,width=0,height=0):
        self._width=width
        self._height=height
    @property
    def width(self):
        return self._width
    @width.setter#与上面的方法共同定义一个属性，并且加上"可写"功能
    def width(self,v):
        self._width=v
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,v):
        self._height=v
    @property#改变调用语法，并且"只读"
    def resolution(self):
        return self._width*self._height

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
