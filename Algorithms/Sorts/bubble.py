import random


class BubbleSort:
    def __init__(self):
        random_size = random.randrange(2, 100)

        self.list_to_be_sorted = []
        for i in range(1, random_size):
            self.list_to_be_sorted.append(random.randrange(1, random_size))

    def bubble(self):
        outer_counter = len(self.list_to_be_sorted) - 1
        while outer_counter >= 0:
            inner_counter = 1
            while inner_counter <= outer_counter:
                if self.list_to_be_sorted[inner_counter - 1] > self.list_to_be_sorted[inner_counter]:
                    temp = self.list_to_be_sorted[inner_counter - 1]
                    self.list_to_be_sorted[inner_counter - 1] = self.list_to_be_sorted[inner_counter]
                    self.list_to_be_sorted[inner_counter] = temp
                inner_counter += 1
            outer_counter -= 1


bub = BubbleSort()
print(bub.list_to_be_sorted)
bub.bubble()
print(bub.list_to_be_sorted)
