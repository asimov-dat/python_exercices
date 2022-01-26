class Super_list(list):
    def __len__(self):
        return 1000

super_list = Super_list()

super_list.append([1,2,3,4,5])
print(len(Super_list()))
print(super_list[0])
print(issubclass(Super_list, list))