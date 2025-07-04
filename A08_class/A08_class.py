# ============================================
#    第一部分：类的基础 - 定义你的第一个“蓝图”
# ============================================

# 1. 定义一个简单的类
# `class` 关键字用来定义一个类。按照惯例，类名使用**驼峰命名法 (PascalCase)**，即每个单词首字母大写。
class Dog:
    # 'pass' 是一个占位符，表示这个类暂时是空的
    pass

print(Dog)

print("-" * 30)

#### **2. 创建对象（实例化）**
# 从一个类创建出一个具体的对象，这个过程叫做**实例化 (Instantiation)**。

my_dog = Dog() # 创建一个 Dog 对象，也叫 Dog 的一个实例
another_dog = Dog() # 创建另一个独立的 Dog 对象

print(my_dog)
print(type(my_dog))
# 输出:
# <__main__.Dog object at 0x...>  (内存地址可能不同)
# <class '__main__.Dog'>
print("-" * 30)


#### **3. `__init__` 方法：构造器**
#`__init__` 是一个非常特殊的“魔法方法”（Dunder Method）。它在**创建对象时自动被调用**，用于初始化对象的属性。它就像是蓝图上的施工说明。
#
#* `self`：这是 OOP 中最重要的概念之一。`self` 代表**对象本身**。在类的方法中，`self` 总是作为第一个参数，让你可以在方法内部访问和修改对象的属性。

class Dog:
    # 构造器方法
    def __init__(self, name, age, breed):
        # self.name, self.age 是对象的属性 (Attributes)
        self.name = name
        self.age = age
        self.breed = breed
        print(f"一只名叫 {self.name} 的狗被创造出来了！")

# 实例化时，传入 __init__ 方法需要的参数 (self 会被自动传入)
dog1 = Dog("旺财", 3, "中华田园犬")
dog2 = Dog("小白", 5, "萨摩耶")

# 访问对象的属性
print(f"{dog1.name} 是一只 {dog1.breed}。")
print(f"{dog2.name} 今年 {dog2.age} 岁了。")

print("-" * 30)


#### **4. 实例方法 (Instance Methods)**

# 实例方法是定义在类中的函数，它们可以操作对象的属性。**第一个参数必须是 `self`**。
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
  
    # 这是一个实例方法
    def bark(self):
        """让狗叫的方法"""
        return f"{self.name} 说: 汪汪汪！"
  
    # 这是另一个实例方法
    def celebrate_birthday(self):
        """给狗过生日，年龄加一"""
        self.age += 1
        return f"祝 {self.name} {self.age} 岁生日快乐！"

my_dog = Dog("豆豆", 2)
print(my_dog.bark())
print(my_dog.celebrate_birthday())
print(f"现在 {my_dog.name} 的年龄是 {my_dog.age} 岁。")
print("-" * 30)
"""
后定义的类会覆盖前定义的类
"""



# ============================================
#    第二部分：OOP 三大支柱 - 继承、多态、封装
# ============================================

#### **1. 封装 (Encapsulation)**
# 封装就是将数据（属性）和操作数据的代码（方法）“包装”在一个对象中。它还提倡“信息隐藏”——对象的使用者不应该随意直接访问其内部数据，而应该通过对象提供的方法来交互。
# 
# 在 Python 中，我们通过命名约定来实现信息隐藏：
# 
# * **`_` 单下划线前缀:** 这是一个**约定**，告诉其他程序员：“这是一个内部属性，请不要在外部直接访问它，除非你真的知道你在做什么。”
# * **`__` 双下划线前缀:** 这会触发 Python 的**名称改写 (Name Mangling)** 机制。Python 会将 `__attribute` 改名为 `_ClassName__attribute`，使得从外部直接访问变得非常困难。

class BankAccount:
    def __init__(self, owner, balance,timestamp):
        self.owner = owner
        self.__balance = balance # 双下划线，"私有"属性
        self._timestamp = timestamp


    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"存款成功，当前余额: {self.__balance}")
        else:
            print("存款金额必须大于0！")
  
    def get_balance(self):
        """提供一个公共方法来安全地获取余额"""
        return self.__balance

acc = BankAccount("Alice", 1000,"2025/3/4 15:20:25")
# print(acc.__balance) # 这行会报错 AttributeError，因为名字被改写了
print(acc._timestamp) # 可以通过这个名字访问保护属性
print(acc._BankAccount__balance)# 可以通过这个名字访问私有属性
print(f"通过公共方法获取余额: {acc.get_balance()}")
acc.deposit(500)
print("-" * 30)

#### **2. 继承 (Inheritance)**
# 继承允许我们创建一个新类（**子类/派生类**），它会继承另一个类（**父类/基类**）的所有属性和方法。这实现了代码的终极复用。
# 
# 继承体现了 **"is-a" (是一种)** 的关系。例如，`Poodle` (贵宾犬) *是一种* `Dog`。
# 
# * `super()` 函数：用于在子类中调用父类的方法，最常用于 `__init__` 中以确保父类的初始化逻辑被执行。

# 父类
class Animal:
    def __init__(self, name):
        self.name = name
  
    def speak(self):
        raise NotImplementedError("子类必须实现这个方法")

# 子类，继承自 Animal
class Dog(Animal):
    def speak(self): # 方法重写 (Method Overriding)
        return f"{self.name} 说: 汪汪！"

# 另一个子类
class Cat(Animal):
    def speak(self):
        return f"{self.name} 说: 喵喵！"

# 更复杂的继承
class GoldenRetriever(Dog):
    def __init__(self, name, favorite_toy):
        super().__init__(name) # 调用父类 Dog 的 __init__ 方法
        self.favorite_toy = favorite_toy
  
    def fetch(self):
        return f"{self.name} 叼回了它的 {self.favorite_toy}！"

d = Dog("旺财")
c = Cat("咪咪")
gr = GoldenRetriever("金宝", "网球")

print(d.speak())
print(c.speak())
print(gr.speak()) # 继承了 Dog 的 speak 方法
print(gr.fetch())

print("-" * 30)

#### **3. 多态 (Polymorphism)**
# 多态（字面意思是“多种形态”）意味着不同的对象可以对同一个消息（方法调用）做出不同的响应。
# 
# 在上面的例子中，`d` 和 `c` 都是 `Animal` 的子类，它们都有 `speak` 方法。当我们调用 `speak` 时，它们会根据自己的类型执行不同的行为。这就是多态。

def make_animal_speak(animal_object):
    # 这个函数不关心传来的是 Dog 还是 Cat
    # 它只知道这个对象有一个 .speak() 方法
    print(animal_object.speak())

make_animal_speak(d) # 传入 Dog 对象
make_animal_speak(c) # 传入 Cat 对象
make_animal_speak(gr) # 传入 GoldenRetriever 对象

print("-" * 30)



# ============================================
#    第三部分：魔法方法 (Dunder Methods)
# ============================================

# 这些以双下划线开头和结尾的方法，能让你自定义 Python 的内置行为，使你的对象能像内置类型一样工作。

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
  
    # 决定了 print(book_object) 的输出
    def __str__(self):
        return f"《{self.title}》 by {self.author}"
  
    # 决定了直接在解释器中输入 book_object 的输出，用于调试
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"

    # 决定了 len(book_object) 的行为
    def __len__(self):
        return self.pages

book = Book("Python入门", "张三", 300)

print(book)         # 调用 __str__          《Python入门》 by 张三
print(str(book))    # 明确调用 __str__      《Python入门》 by 张三
print(repr(book))   # 明确调用 __repr__     Book(title='Python入门', author='张三')
print(len(book))    # 调用 __len__          300

print("-" * 30)

# ============================================
#               第四部分：高级概念
# ============================================

#### **1. 类变量 vs. 实例变量**

# * **实例变量 (Instance Variable):** 在 `__init__` 中通过 `self.variable` 定义，每个对象独有一份。
# * **类变量 (Class Variable):** 在类定义下直接定义，所有该类的对象**共享**同一份。

class Car:
    # 这是类变量，所有 Car 对象共享
    wheels = 4

    def __init__(self, brand):
        # 这是实例变量，每个 Car 对象独有
        self.brand = brand

car1 = Car("Toyota")
car2 = Car("Honda")

print(f"{car1.brand} 有 {car1.wheels} 个轮子。")
print(f"{car2.brand} 有 {car2.wheels} 个轮子。")

# 修改类变量会影响所有实例
Car.wheels = 3
print(f"灾难！现在 {car1.brand} 只有 {car1.wheels} 个轮子了！")
print("-" * 30)


#### **2. 静态方法和类方法**
# * **`@staticmethod`**: 一个普通的函数，只是被“放”在了类的命名空间里。它**不接收 `self` 或 `cls`**，无法访问实例或类的属性。通常是与类主题相关的工具函数。
# * **`@classmethod`**: 第一个参数是类本身（约定俗成写为 `cls`），而不是实例 `self`。它可以访问类变量，常用于创建“工厂方法”。

class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def margherita(cls):
        """一个创建经典玛格丽特披萨的工厂方法"""
        return cls(['mozzarella', 'tomatoes'])

    @staticmethod
    def is_vegetarian(ingredients):
        """一个检查配料是否素食的工具函数"""
        return 'ham' not in ingredients and 'bacon' not in ingredients

pizza1 = Pizza(['cheese', 'ham'])
pizza2 = Pizza.margherita() # 使用类方法创建实例

print(pizza1.ingredients)
print(pizza2.ingredients)
print(Pizza.is_vegetarian(['cheese', 'mushrooms'])) # 使用静态方法


