import random


class InsertionSort:
    def __init__(self):
        random_size = random.randrange(2, 100)

        self.list_to_be_sorted = []
        for i in range(1, random_size):
            self.list_to_be_sorted.append(random.randrange(1, random_size))

    def insert(self):
        outer_counter = 1
        while outer_counter < len(self.list_to_be_sorted):
            index = self.list_to_be_sorted[outer_counter]
            inner_counter = outer_counter
            while inner_counter > 0 and self.list_to_be_sorted[inner_counter - 1] > index:
                self.list_to_be_sorted[inner_counter] = self.list_to_be_sorted[inner_counter - 1]
                inner_counter -= 1
            self.list_to_be_sorted[inner_counter] = index
            outer_counter += 1


ins = InsertionSort()
print(ins.list_to_be_sorted)
ins.insert()
print(ins.list_to_be_sorted)
