import random


class SelectionSort:
    def __init__(self):
        random_size = random.randrange(2, 100)

        self.list_to_be_sorted = []
        for i in range(1, random_size):
            self.list_to_be_sorted.append(random.randrange(1, random_size))

    def select(self):
        outer_counter = 0
        while outer_counter < len(self.list_to_be_sorted) - 1:
            minimum = outer_counter
            inner_counter = outer_counter + 1
            while inner_counter < len(self.list_to_be_sorted):
                if self.list_to_be_sorted[inner_counter] < self.list_to_be_sorted[minimum]:
                    minimum = inner_counter
                inner_counter += 1
            temp = self.list_to_be_sorted[outer_counter]
            self.list_to_be_sorted[outer_counter] = self.list_to_be_sorted[minimum]
            self.list_to_be_sorted[minimum] = temp
            outer_counter += 1


sel = SelectionSort()
print(sel.list_to_be_sorted)
sel.select()
print(sel.list_to_be_sorted)
