class TreeNode:
    def __init__(self, key):
        self.key = key
        self.p = None # parent
        self.color = "red"
        self.left = None
        self.right = None


class RedBlackTree:
    def __init__(self):
        self.NIL = TreeNode(None) 
        self.NIL.color = "black"
        self.NIL.left = None
        self.NIL.right = None
        # self.NIL.p = self.NIL
        self.root = self.NIL

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        

        if y.left != self.NIL:
            y.left.p = x
               
        y.p = x.p 

        # if x.p is None:
        if x.p is self.NIL:  # fix
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y 


        y.left = x 
        x.p = y

    def right_rotate(self, x):
        y = x.left 
        x.left = y.right 

        if y.right != self.NIL:
            y.right.p = x

        y.p = x.p 

        # if x.p is None:
        if x.p is self.NIL:  # fix
            self.root = y 
        elif x == x.p.right:
            x.p.right = y 
        else:
            x.p.left = y 

        y.right = x 
        x.p = y

    def transplant(self, u, v):
        # if u.p == None:
        if u.p == self.NIL:  # fix
            self.root = v
        elif u == u.p.left:
            u.p.left = v 
        else:
            u.p.right = v
        v.p = u.p 

    def minimum(self, x):
        while x.left != self.NIL:
            x = x.left
        return x

    def search(self, key):
        x = self.root
        while x != self.NIL and key != x.key:
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def insert(self, key):
        ######### YOUR CODE STARTS HERE #########
        # raise NotImplementedError()
        z = TreeNode(key)
        y = self.NIL
        x = self.root

        while x != self.NIL:
            y = x
            if key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y

        if y == self.NIL:
            self.root = z
        elif key < y.key:
            y.left = z
        else:
            y.right = z
        
        z.left = self.NIL
        z.right = self.NIL
        z.color = "red"

        

        self.insert_fixup(z)


    
    def insert_fixup(self, z):
        while z.p.color == "red":
            if z.p.p.left == z.p:
                y = z.p.p.right
                if y.color == "red":
                    z.p.color = "black"
                    y.color = "black"
                    z.p.p.color = "red"
                    z = z.p.p
                else:
                    if z.p.right == z:
                        z = z.p
                        self.left_rotate(z)
                    z.p.color = "black"
                    z.p.p.color = "red"
                    self.right_rotate(z.p.p)
            else:
                y = z.p.p.left
                if y.color == "red":
                    z.p.color = "black"
                    y.color = "black"
                    z.p.p.color = "red"
                    z = z.p.p
                else:
                    if z.p.left == z:
                        z = z.p
                        self.right_rotate(z)
                    z.p.color = "black"
                    z.p.p.color = "red"
                    # self.my_print(self.root)
                    self.left_rotate(z.p.p)

        
        self.root.color = "black"
        

        
    def delete(self, key):
        ######### YOUR CODE STARTS HERE #########
        # raise NotImplementedError()
        z = self.search(key)

        if z == self.NIL:
            return False

        y = z
        y_original_color = y.color

        if z.left == self.NIL:
            x = z.right
            self.transplant(z, x)
        elif z.right == self.NIL:
            x = z.left
            self.transplant(z, x)
        else:
            
            y = self.minimum(z.right)
            
            y_original_color = y.color
            x = y.right
            if y.p == z:
                x.p = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                z.right.p = y

            self.transplant(z, y)
            y.left = z.left
            z.left.p = y
            y.color = z.color

            

        if y_original_color == "black":
            self.delete_fixup(x)
        
        return True
    

    def delete_fixup(self, x):
        while x != self.root and x.color == "black":
            if x == x.p.left:
                w = x.p.right
                if w.color == "red":
                    w.color = "black"
                    x.p.color = "red"
                    self.left_rotate(x.p)
                    w = x.p.right

                if w.left.color == "black" and w.right.color == "black":
                    w.color = "red"
                    x = x.p
                else:
                    if w.right.color == "black":
                        w.left.color = "black"
                        w.color = "red"
                        self.right_rotate(w)
                        w = x.p.right
                    
                    w.color = x.p.color
                    x.p.color = "black"
                    w.right.color = "black"  #fix
                    self.left_rotate(x.p)
                    x = self.root
            else:
                w = x.p.left
                if w.color == "red":
                    w.color = "black"
                    x.p.color = "red"
                    self.right_rotate(x.p)
                    w = x.p.left

                if w.right.color == "black" and w.left.color == "black":
                    w.color = "red"
                    x = x.p
                else:
                    if w.left.color == "black":
                        w.right.color = "black"
                        w.color = "red"
                        self.left_rotate(w)
                        w = x.p.left
                    
                    w.color = x.p.color
                    x.p.color = "black"
                    w.left.color = "black"  #fix
                    self.right_rotate(x.p)
                    x = self.root
        
        x.color = "black"

    def my_print(self, node):
        if node != self.NIL:

            print("[ ", end="")
            self.my_print(node.left)
            print(f"{node.key}({node.color})", end = "")
            self.my_print(node.right)
            print(" ]", end="")



if __name__ == "__main__":
    rbt = RedBlackTree()
    keys = [12, 13, 17, 10, 4, 6, 9, 15, 30, 25, 20, 40]

    for key in keys:
        rbt.insert(key)
    
    rbt.my_print(rbt.root)
    rbt.delete(13)
    rbt.my_print(rbt.root)
    rbt.delete(12)
    print()
    rbt.my_print(rbt.root)