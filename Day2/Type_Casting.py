class TypeCastingDemo:
    """
    A class to demonstrate type casting in Python using OOP principles.
    """
    
    def __init__(self):
        self.numeric_casting()
        self.sequence_casting()
        self.set_casting()
        self.dict_casting()
        self.boolean_casting()
        self.binary_casting()

    def numeric_casting(self):
        print("\nNumeric Type Casting:")
        int_value = 10
        float_value = float(int_value)
        complex_value = complex(int_value)
        print(f"Integer to Float: {float_value} ({type(float_value)})")
        print(f"Integer to Complex: {complex_value} ({type(complex_value)})")
        
        float_num = 10.99
        int_from_float = int(float_num)
        print(f"Float to Integer: {int_from_float} ({type(int_from_float)})")

    def sequence_casting(self):
        print("\nSequence Type Casting:")
        list_value = [1, 2, 3, 4]
        tuple_from_list = tuple(list_value)
        string_from_list = str(list_value)
        print(f"List to Tuple: {tuple_from_list} ({type(tuple_from_list)})")
        print(f"List to String: {string_from_list} ({type(string_from_list)})")
        
        string_value = "1234"
        list_from_string = list(string_value)
        print(f"String to List: {list_from_string} ({type(list_from_string)})")

    def set_casting(self):
        print("\nSet Type Casting:")
        list_value = [1, 2, 3, 4, 2]
        set_from_list = set(list_value)
        tuple_value = (5, 6, 7, 5)
        set_from_tuple = set(tuple_value)
        print(f"List to Set: {set_from_list} ({type(set_from_list)})")
        print(f"Tuple to Set: {set_from_tuple} ({type(set_from_tuple)})")

    def dict_casting(self):
        print("\nDictionary Type Casting:")
        tuple_list = [("name", "Alice"), ("age", 25)]
        dict_from_tuple_list = dict(tuple_list)
        print(f"Tuple List to Dictionary: {dict_from_tuple_list} ({type(dict_from_tuple_list)})")

    def boolean_casting(self):
        print("\nBoolean Type Casting:")
        print(f"Integer to Boolean: {bool(1)} ({type(bool(1))})")
        print(f"Zero to Boolean: {bool(0)} ({type(bool(0))})")
        print(f"Empty String to Boolean: {bool('')} ({type(bool(''))})")
        print(f"Non-empty String to Boolean: {bool('Hello')} ({type(bool('Hello'))})")

    def binary_casting(self):
        print("\nBinary Type Casting:")
        str_value = "Hello"
        bytes_value = bytes(str_value, 'utf-8')
        bytearray_value = bytearray(str_value, 'utf-8')
        print(f"String to Bytes: {bytes_value} ({type(bytes_value)})")
        print(f"String to ByteArray: {bytearray_value} ({type(bytearray_value)})")

if __name__ == "__main__":
    TypeCastingDemo()
