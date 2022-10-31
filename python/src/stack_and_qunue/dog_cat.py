"""
宠物，狗，猫的类如下：
"""
from collections import deque
from queue import Queue


class Pet:
    def __init__(self, category):
        self.type = category

class Dog(Pet):
    def __init__(self):
        super(Dog, self).__init__('dog')

class Cat(Pet):
    def __init__(self):
        super(Cat, self).__init__('cat')
"""
实现一种猫狗队列的结构，要求：
1. 用户可以调用add方法将cat或dog的实例放入队列中
2. 用户可以调用pollAll方法，将队列中所有的实例按照进队列的先后顺序依次弹出
3. 用户可以调用pollDog方法，将队列中dog实例按照进队列的先后顺序依次弹出
4. 用户可以调用pollCat方法，将队列中cat实例按照进队列的先后顺序依次弹出
5. 用户可以调用isEmpty方法，检查队列中是否还有dog或cat实例
6. 用户可以调用isDogEmpty方法，检查队列中是否有dog类的实例
7. 用户可以调用isCatEmpty方法，检查队列中是否有cat类的实例
"""

class PetEntryQueue:
    def __init__(self, pet, count):
        self.pet = pet
        self.count = count


class PetQueue:
    def __init__(self):
        self.dog_queue = deque()
        self.cat_queue = deque()
        self.count = 0

    def add(self, pet: Pet):
        if pet.type == 'dog':
            self.dog_queue.append(PetEntryQueue(pet, self.count))
        elif pet.type == 'cat':
            self.cat_queue.append(PetEntryQueue(pet, self.count))
        else:
            raise Exception('unknown pet type')

        self.count += 1

    def poll_all(self):
        if not self.cat_queue and not self.dog_queue:
            raise Exception('No data')

        if not self.cat_queue or not self.dog_queue:
            if not self.cat_queue:
                return self.dog_queue.pop().pet
            else:
                return self.cat_queue.pop().pet

        cat_entry = self.cat_queue[0]
        dog_entry = self.dog_queue[0]
        if cat_entry.count < dog_entry.count:
            return self.cat_queue.pop().pet
        else:
            return self.dog_queue.pop().pet

    def poll_dog(self):
        if not self.dog_queue:
            raise Exception('no dog data')
        return self.dog_queue.pop().pet

    def poll_cat(self):
        if not self.cat_queue:
            raise Exception('no cat data')
        return self.cat_queue.pop().pet

    def is_empty(self):
        return self.is_dog_empty() and self.is_cat_empty()

    def is_dog_empty(self):
        return not self.dog_queue

    def is_cat_empty(self):
        return not self.cat_queue


if __name__ == '__main__':
    pass