class DataTypeDemo:
    """
    A class to demonstrate different data types in Python using OOP practices.
    """
    
    def __init__(self):
        self.numeric_types()
        self.sequence_types()
        self.set_types()
        self.mapping_types()
        self.boolean_type()
        self.binary_types()
        self.none_type()

    def numeric_types(self):
        print("\nNumeric Types:")
        integer_value = 10
        float_value = 10.5
        complex_value = 3 + 4j
        print(f"Integer: {integer_value} ({type(integer_value)})")
        print(f"Float: {float_value} ({type(float_value)})")
        print(f"Complex: {complex_value} ({type(complex_value)})")

    def sequence_types(self):
        print("\nSequence Types:")
        list_value = [1, 2, 3, "Python"]
        tuple_value = (10, 20, 30, "Tuple")
        range_value = range(5)
        print(f"List: {list_value} ({type(list_value)})")
        print(f"Tuple: {tuple_value} ({type(tuple_value)})")
        print(f"Range: {list(range_value)} ({type(range_value)})")

    def set_types(self):
        print("\nSet Types:")
        set_value = {1, 2, 3, 4, "Set"}
        frozenset_value = frozenset([10, 20, 30, "FrozenSet"])
        print(f"Set: {set_value} ({type(set_value)})")
        print(f"FrozenSet: {frozenset_value} ({type(frozenset_value)})")

    def mapping_types(self):
        print("\nMapping Type:")
        dict_value = {"name": "Alice", "age": 25, "city": "New York"}
        print(f"Dictionary: {dict_value} ({type(dict_value)})")

    def boolean_type(self):
        print("\nBoolean Type:")
        bool_value = True
        print(f"Boolean: {bool_value} ({type(bool_value)})")

    def binary_types(self):
        print("\nBinary Types:")
        bytes_value = b"Hello"
        bytearray_value = bytearray([65, 66, 67])
        memoryview_value = memoryview(bytes_value)
        print(f"Bytes: {bytes_value} ({type(bytes_value)})")
        print(f"ByteArray: {bytearray_value} ({type(bytearray_value)})")
        print(f"MemoryView: {memoryview_value} ({type(memoryview_value)})")

    def none_type(self):
        print("\nNone Type:")
        none_value = None
        print(f"None: {none_value} ({type(none_value)})")

if __name__ == "__main__":
    DataTypeDemo()
