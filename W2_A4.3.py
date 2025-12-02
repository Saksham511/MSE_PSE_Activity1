class MathSeries:
    # No self, no staticmethod
    def __init__(self):
        pass

    def factorial_recursive(n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        if n in (0, 1):
            return 1
        return n * MathSeries.factorial_recursive(n - 1)

    def fibonacci_recursive(n):
        if n < 0:
            raise ValueError("Fibonacci is not defined for negative numbers.")
        if n == 0:
            return 0
        if n == 1:
            return 1
        return (MathSeries.fibonacci_recursive(n - 1) +
                MathSeries.fibonacci_recursive(n - 2))

    # New method to print all Fibonacci values up to n
    def fibonacci_series(n):
        series = []
        for i in range(n + 1):
            series.append(MathSeries.fibonacci_recursive(i))
        return series


if __name__ == "__main__":
    n = 5

    # Create an object
    obj1 = MathSeries()