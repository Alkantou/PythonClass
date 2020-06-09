


class TreeNode:
    # def __init__(self, a, b):
    #     self.a = a
    #     self.b = b

    # def __int__(self, name, age, location):
    #     self.name = name
    #     self.age = age
    #     self.location = location

    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return self.value


pappous = TreeNode('Karolos', None, None)
babas = TreeNode('Kostas', None, None)
george = TreeNode('George', None, None)

pappous.left = babas
pappous.right = george

Vafouskos = TreeNode('Karolos', None, None)
Alex = TreeNode('Alexandros', None, None)
Ko = TreeNode('KarolosX', None, None)
Kinezos = TreeNode('Vasilios', None, None)

babas.right = Alex
babas.left = Vafouskos
george.right = Kinezos
george.left = Ko

current_level = [pappous]
while len(current_level) != 0:
    next_level = []
    for x in current_level:
        if x.left:
            next_level.append(x.left)
        if x.right:
            next_level.append(x.right)
    print(current_level)
    current_level = next_level

