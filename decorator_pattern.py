class Decorator:
    def catchNonIntegerException(self, func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                print(e)
                return 'Error'
            return result
        return wrapper

class DataProcessor:
    decorator = Decorator()

    @decorator.catchNonIntegerException
    def calculateMax(self, num1, num2):
        return max(num1, num2)

if __name__ == '__main__':

    dp = DataProcessor()
    print(dp.calculateMax(1, 2))
    print(dp.calculateMax(None, 1))
