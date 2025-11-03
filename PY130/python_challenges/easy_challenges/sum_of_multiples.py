class SumOfMultiples:
    def __init__(self, *multiples):
        self.multiples = multiples if multiples else (3, 5)

    @classmethod
    def sum_up_to(cls, num_arg):
        return cls().to(num_arg)

    def to(self, num_arg):
        final_multiples = set()
        for num in range(1, num_arg):
            for multiple in self.multiples:
                if num % multiple == 0:
                    final_multiples.add(num)

        return sum(final_multiples)