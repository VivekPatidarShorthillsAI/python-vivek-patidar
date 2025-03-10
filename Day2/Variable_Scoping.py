class VariableScopeDemo:
    """
    A class to demonstrate variable scopes in Python, including local, global, and nonlocal keywords.
    """
    
    global_var = "I am a global variable"
    
    def __init__(self):
        print("\n--- Demonstrating Variable Scopes in Python ---")
        self.local_scope()
        self.global_scope()
        self.nonlocal_scope()
    
    def local_scope(self):
        print("\n--- Local Scope ---")
        local_var = "I am a local variable"
        print(f"Inside local_scope function: {local_var}")
    
    def global_scope(self):
        print("\n--- Global Scope ---")
        print(f"Accessing global variable: {VariableScopeDemo.global_var}")
        
        # Modifying global variable using global keyword
        global global_variable
        global_variable = "Modified Global Variable"
        print(f"Modified global variable using 'global' keyword: {global_variable}")
    
    def nonlocal_scope(self):
        print("\n--- Nonlocal Scope ---")
        
        def outer():
            outer_var = "I am in the outer function"
            print(f"Outer function before calling inner: {outer_var}")
            
            def inner():
                nonlocal outer_var
                print(f"Inside inner function before modification: {outer_var}")
                outer_var = "Modified in inner function"
                print(f"Inside inner function after modification: {outer_var}")
            
            inner()
            print(f"Outer function after inner execution: {outer_var}")
        
        outer()

if __name__ == "__main__":
   obj= VariableScopeDemo()
