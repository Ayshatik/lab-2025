class LazyProperty:
    def __init__(self, func):
        self.func = func
        self.name = func.__name__
        self.attr_name = f"_lazy_{self.name}"

    def __get__(self, instance, cls=None):
        if instance is None:
            return self
        if not hasattr(instance, self.attr_name):
            setattr(instance, self.attr_name, self.func(instance))
        return getattr(instance, self.attr_name)

class ExampleClass:
    @LazyProperty
    def expensive_calculation(self):
        print("Computing value...")
        return 42
