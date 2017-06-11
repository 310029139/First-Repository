# 2. 编写代码，定义一个名叫为 ListInstanceAttr 的类，显示从一个实例可以访问的所有属性名及其值。
# 再将这个 ListInstanceAttr 类作为超类，用在多重继承中，看一看运行结果。
# 提示：参考一下 “第6章__面向对象程序设计_1.pptx”的第38页。可能需要使用内置函数 getattr 以及 dir，比如：dir(self)
class ListInstanceAttr(object):
    def __init__(self, name, value, base=3):
        self.name = name
        self.value = value
        self.base = base

    def getattr(self):
        attrs = ['%s ==> %s' % (key, getattr(self, key)) for key in sorted(self.__dict__)]
        print(attrs)

class SubClass(ListInstanceAttr):
    def __init__(self, name, value, base=3, new='U'):
        super(SubClass, self).__init__(name, value, base)
        self.new = new


def main():
    cls = SubClass('Li', 3.14, 5, 'me')
    cls.getattr()

if __name__ == '__main__':
    main()
