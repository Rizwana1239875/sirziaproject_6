
class MathUtils:
    @staticmethod
    def add(a, b):
        return a+b
    
#print(MathUtils.add(5, 10))

if __name__ =="__main__":
    result = MathUtils.add(5,10)
    print("sum:", result)