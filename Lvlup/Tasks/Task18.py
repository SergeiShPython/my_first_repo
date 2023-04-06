import random

class Deck_of_Cards():
    nums_list = ['2', '3', '4', '5', '6', '7', '8', '9', '10', "Валет", "Дама", "Король", "Туз"]
    mast_list = ["пик", "крестей", "бубей", "червей"]
    def __init__(self,i, j):
        self.suit = self.mast_list[i - 1]
        self.nums = self.nums_list[j-1]



    def shuffle(self):

        """for i in range(len(self.suit)):
            for j in range(len(self.nums)):
                self.mix[self.suit[i]] = self.nums[j]
        #random.shuffle(self.mix.keys())"""

        return self.mix
x = Deck_of_Cards(nums_list,mast_list)
print(x.shuffle())