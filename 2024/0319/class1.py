class Singer:
    def sing(self):
        return 'Lalala~'

    def func2(self):
        print(id(self))
        print("func2 is called")


taegi = Singer()
print(f"t... {id(taegi)}" )
print(taegi.func2())
