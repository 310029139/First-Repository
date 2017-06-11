# 1. 编写代码，实现一个栈（Stack）类。栈是只能在一端插入和删除数据的序列，
# 它按照先进后出的原则存储数据，先进入的数据被压入栈底，最后的数据在栈顶，
# 需要读数据的时候从栈顶开始弹出数据，最后一个数据被第一个读出来
# 思路1 按思路来实现栈,但这样并不pythonic
# 思路2 用Python的描述符，但是忘记了怎么用,以后补上
class My_Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if not self.stack:
            print("栈空!")
        else:
            return self.stack.pop()


def main():
    my_stack = My_Stack()
    while True:
        ch = input("请输入要进行的操作:q退出!")
        if ch == 'q':
            break
        elif ch == 'push':
            Element = input('请输入要压入栈的元素!')
            my_stack.push(Element)
        elif ch == 'pop':
            print(my_stack.pop())
        else:
            print("输入有误!")

if __name__ == '__main__':
    main()
