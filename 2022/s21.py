
fname = "in21.txt"

# %% 
f = open(fname)
lines = [l.strip() for l in f]

values = {}
formulas = {}

for l in lines:
    left, right = l.split(': ')
    if right[0].isalpha():
        formulas[left] = right.split()
    else:
        values[left] = int(right)

# %% part 1 v1

def op(lo, sign, ro):
    if sign == '+':
        return lo + ro
    elif sign == '-':
        return lo - ro
    elif sign == '*':
        return lo * ro
    else:
        return lo // ro
        
while formulas:
    used = []
    for var, f in formulas.items():
        if f[0] in values and f[2] in values:
            lo, sign, ro = f
            values[var] = op(values[lo], sign, values[ro])
            used.append(var)
    for u in used:
        del formulas[u]
        
print(values['root'])


# %% 
class Node:
    def __init__(self, name, rhs):
        self.name = name
        
        self.leftname = None
        self.rightname = None
        
        self.left = None
        self.right = None
        self.op = None
        
        self.value = None
        
        # part2
        self.onhumnpath = False
        
        if rhs[0].isalpha():
            self.leftname, self.op, self.rightname = rhs.split()
        else:
            self.value = int(rhs)
            
    def __repr__(self):
        return f"<'{self.name}'>"

def create_tree(root, lhsrhs):
    if root.value is None:
        if root.left is None:
            root.left = lhsrhs[root.leftname]
            create_tree(root.left, lhsrhs)
        if root.right is None:
            root.right = lhsrhs[root.rightname]
            create_tree(root.right, lhsrhs)
            
def calculate(root):
    if root.left.value is None:
        calculate(root.left)
    if root.right.value is None:
        calculate(root.right)
        
    root.value = op(root.left.value, root.op, root.right.value)
    
def mark_humn_path_nodes(root):
    if root.name == 'humn':
        root.onhumnpath = True
        root.value = None
        return True
    elif root.op is None:
        False
    else:
        l = mark_humn_path_nodes(root.left)
        r = mark_humn_path_nodes(root.right)
        if l or r:
            root.onhumnpath = True
            root.value = None
        return l or r
    
def reverse_travel_tree(root, finalvalue):
    if root.name == 'humn':
        return finalvalue
    if root.op == '+':
        if root.left.value is None:
            root.left.value = finalvalue - root.right.value 
            return reverse_travel_tree(root.left, root.left.value)
        elif root.right.value is None:
            root.right.value = finalvalue - root.left.value 
            return reverse_travel_tree(root.right, root.right.value)
    elif root.op == '*':
        if root.left.value is None:
            root.left.value = finalvalue // root.right.value 
            return reverse_travel_tree(root.left, root.left.value)
        elif root.right.value is None:
            root.right.value = finalvalue // root.left.value 
            return reverse_travel_tree(root.right, root.right.value)
    elif root.op == '/':
        if root.left.value is None:
            root.left.value = finalvalue * root.right.value
            return reverse_travel_tree(root.left, root.left.value)
        elif root.right.value is None:
            root.right.value = root.left.value / finalvalue
            return reverse_travel_tree(root.right, root.right.value)
    elif root.op == '-':
        if root.left.value is None:
            root.left.value = finalvalue + root.right.value
            return reverse_travel_tree(root.left, root.left.value)
        elif root.right.value is None:
            root.right.value = root.left.value - finalvalue            
            return reverse_travel_tree(root.right, root.right.value)
        
# %% 

f = open(fname)
lines = [l.strip() for l in f]

values = {}
formulas = {}

for l in lines:
    left, right = l.split(': ')
    if right[0].isalpha():
        formulas[left] = right.split()
    else:
        values[left] = int(right)
        
# %% part 1 v2
    
lhsrhs = {}
for l in lines:
    name, rhs = l.split(': ')
    lhsrhs[name] = Node(name, rhs)
    n = Node(name, rhs)

root = Node('root', ' '.join(formulas['root']))
create_tree(root, lhsrhs)
calculate(root)
# print(root.value)

# %% part 2

mark_humn_path_nodes(root)

humn_root = root.right
finalvalue = root.left.value
if root.left.onhumnpath:
    humn_root = root.left
    finalvalue = root.right.value
    
part2 = reverse_travel_tree(humn_root, finalvalue)
print(part2)