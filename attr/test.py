class Fool:
    def __init__(self, name, age):
        self.name = name
        self.age = age

foo = Fool("Haha", "0.1")

print("".join(["BEFORE:", str(foo.name)]))
print("".join(["BEFORE with getattr:", str(getattr(foo, "name"))]))
setattr(foo, "name", "Changed")
print("".join(["AFTER with setattr:",str(getattr(foo, "name"))]))