"""
Purpose: Instantiate class given string module name and class name
Reference: 
    * Instantiate class dynamically, https://stackoverflow.com/a/4821120
    * Import module from string, https://stackoverflow.com/a/8719100
"""
import importlib
import sys



def load_class(module_name: str, class_name: str, *args, **kwargs):
        
    if module_name not in sys.modules:
        module = importlib.import_module(module_name)
    else:
        module = sys.modules[module_name]

    class_ = getattr(module, class_name)
    return class_(*args, **kwargs)

if __name__ == '__main__':
    a = load_class("_class", "SandboxClass", "foo", purpose=None)
    print(a.name)
    print(a.purpose)