class PerfectNumber:
    @classmethod
    def classify(cls, arg_number):
        if arg_number < 1:
            raise ValueError("Input must be a positive integer")
        divisor_list = sum([num for num in range(1, arg_number) if arg_number % num == 0])
        if divisor_list > arg_number:
            return "abundant"
        elif divisor_list < arg_number:
            return "deficient"
        else:
            return "perfect"
        