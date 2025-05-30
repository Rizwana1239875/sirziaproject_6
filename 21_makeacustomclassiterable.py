# # how to check if a class is iterable

# from collections.abc import Iterable
# # Check if a class is iterable
# print("isinstance([1,2,3], Iterable) = ",isinstance([1,2,3], Iterable)) # True because list is iterable
# print('isinstance("Hello", Iterable) =', isinstance("Hello", Iterable)) # True because string is iterable
# print("isinstance(123, Iterable) = ", isinstance(123, Iterable)) # False because integer is not iterable


# make a custom class iterable

from collections.abc import Iterable, Iterator

class MyCollection(Iterable):
    def __init__(self, collection_data):
        self.collection_data = collection_data

    def __iter__(self):
        return MyIterator(self.collection_data)
    
class MyIterator(Iterator):
    def __init__(self, collection_data):
        self.collection_data = collection_data
        self.index = 0

    def __next__(self):
        if self.index >= len(self.collection_data):
            raise StopIteration
        value = self.collection_data[self.index]
        self.index += 1
        print("MyIterator.__next__ Called")
        return value
        
# usage
my_iterable = MyCollection([1, 2, 3])
for item in my_iterable:
    print("item :", item)
            