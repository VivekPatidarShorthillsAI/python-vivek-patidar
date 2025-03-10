class ListOperations:
    """Class to demonstrate list operations"""
    def __init__(self, lst):
        self.lst = lst

    def access_items(self):
        print(f"First item: {self.lst[0]}")

    def modify_items(self):
        self.lst[0] = 10
        print(f"Modified List: {self.lst}")

    def add_items(self):
        self.lst.append(4)
        print(f"List after append: {self.lst}")

    def remove_items(self):
        if 10 in self.lst:
            self.lst.remove(10)
        print(f"List after removal: {self.lst}")

    def loop_list(self):
        print("Looping through list:")
        for item in self.lst:
            print(item)

    def list_comprehension(self):
        squares = [x**2 for x in self.lst]
        print(f"Squares: {squares}")

    def sort_list(self):
        self.lst.sort()
        print(f"Sorted List: {self.lst}")

    def copy_list(self):
        lst_copy = self.lst.copy()
        print(f"Copied List: {lst_copy}")

class TupleOperations:
    """Class to demonstrate tuple operations"""
    def __init__(self, tp):
        self.tp = tp

    def access_items(self):
        print(f"First item: {self.tp[0]}")

    def update_tuple(self):
        self.tp = self.tp + (4,)
        print(f"Updated Tuple: {self.tp}")

    def unpack_tuple(self):
        a, b, c = self.tp[:3]
        print(f"Unpacked: {a}, {b}, {c}")

    def loop_tuple(self):
        print("Looping through tuple:")
        for item in self.tp:
            print(item)

class SetOperations:
    """Class to demonstrate set operations"""
    def __init__(self, st):
        self.st = st

    def add_items(self):
        self.st.add(4)
        print(f"Set after addition: {self.st}")

    def remove_items(self):
        if 1 in self.st:
            self.st.remove(1)
        print(f"Set after removal: {self.st}")

    def loop_set(self):
        print("Looping through set:")
        for item in self.st:
            print(item)

class DictionaryOperations:
    """Class to demonstrate dictionary operations"""
    def __init__(self, dict1):
        self.dict1 = dict1

    def access_items(self):
        print(f"Name: {self.dict1.get('name', 'N/A')}")

    def change_items(self):
        self.dict1["age"] = 30
        print(f"Updated Dictionary: {self.dict1}")

    def add_items(self):
        self.dict1["city"] = "New York"
        print(f"Dictionary after addition: {self.dict1}")

    def remove_items(self):
        self.dict1.pop("city", None)
        print(f"Dictionary after removal: {self.dict1}")

    def loop_dictionary(self):
        print("Looping through dictionary:")
        for key, value in self.dict1.items():
            print(f"{key}: {value}")

class RangeOperations:
    """Class to demonstrate range operations"""
    def __init__(self, start, stop, step=1):
        self.rng = range(start, stop, step)

    def access_range(self):
        print(f"First element: {self.rng[0]}")

    def loop_range(self):
        print("Looping through range:")
        for num in self.rng:
            print(num)

if __name__ == "__main__":
    print("\n--- List Operations ---")
    list_obj = ListOperations([1, 2, 3])
    list_obj.access_items()
    list_obj.modify_items()
    list_obj.add_items()
    list_obj.remove_items()
    list_obj.loop_list()
    list_obj.list_comprehension()
    list_obj.sort_list()
    list_obj.copy_list()
    
    print("\n--- Tuple Operations ---")
    tuple_obj = TupleOperations((1, 2, 3))
    tuple_obj.access_items()
    tuple_obj.update_tuple()
    tuple_obj.unpack_tuple()
    tuple_obj.loop_tuple()
    
    print("\n--- Set Operations ---")
    set_obj = SetOperations({1, 2, 3})
    set_obj.add_items()
    set_obj.remove_items()
    set_obj.loop_set()
    
    print("\n--- Dictionary Operations ---")
    dict_obj = DictionaryOperations({"name": "John", "age": 25})
    dict_obj.access_items()
    dict_obj.change_items()
    dict_obj.add_items()
    dict_obj.remove_items()
    dict_obj.loop_dictionary()
    
    print("\n--- Range Operations ---")
    range_obj = RangeOperations(1, 10, 2)
    range_obj.access_range()
    range_obj.loop_range()
