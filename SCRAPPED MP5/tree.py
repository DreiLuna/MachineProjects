from cs1graphics import *
import math
import random

class Tree:
   
    def __init__(self, intitial_tree_origin= (500,250), intitial_tree_radius = 75, intitial_num_leaves = 20, initial_leaf_radius = 25):
        self.tree_origin = intitial_tree_origin
        self.tree_radius = intitial_tree_radius
        self.num_leaves = intitial_num_leaves
        self.leaf_radius = initial_leaf_radius
        
    
    def getTreeLayer(self):
        tree = Layer()
        leaves = []
        branches = []
        change_in_degrees = 180/self.num_leaves
        for i in range(self.num_leaves+1):
            x = (math.cos(math.radians(change_in_degrees*i))*self.tree_radius) + self.tree_origin[0]
            y = self.tree_origin[1] - (math.sin(math.radians(change_in_degrees*i))*self.tree_radius)  
            
            


            leaves.append(Circle(self.leaf_radius+random.randint(1,3), Point(x+random.randint(-5,5),y+random.randint(-5,5))))
            leaves[i].setFillColor((0,50,0))
            leaves[i].setBorderWidth(0)
            
            branches.append(Path(Point(self.tree_origin[0],self.tree_origin[1]),Point(x,y)))
            branches[i].setBorderColor((125,100,20))
            branches[i].setBorderWidth(5)
            
            tree.add(branches[i])
            tree.add(leaves[i])
        trunk = Path(Point(self.tree_origin[0],self.tree_origin[1]),Point(self.tree_origin[0],self.tree_origin[1]+100))
        trunk.setBorderColor((125,100,20))
        trunk.setBorderWidth(25)
        tree.add(trunk)
        
        return tree
