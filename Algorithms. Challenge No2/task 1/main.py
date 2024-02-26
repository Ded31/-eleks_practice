import random


def main():
    random_int = random.randint(0, 30)
    elements = makelist(random_int)
    return elements
    

def makelist(random_int):
    num_list = []
    for count in range(random_int):
        num_list.append(random.randint(0, 1000))
    return num_list


def filterlist(any_list):
  filter_list = sorted(list(set(any_list)))
  filter_list = [i for i in filter_list if i % 5 != 0]
  return filter_list


list1 = main()
list2 = main()
list1.extend(list2)

print(filterlist(list1))