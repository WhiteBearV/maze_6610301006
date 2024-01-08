import os
import keyboard
import time
class pos:
    def __init__(self, y, x) -> None:
        self.y = y
        self.x = x

    def __str__(self):
        return f"({self.y}, {self.x})"

class maze:
    def __init__(self) -> None:
        self.maze = [
                    ["X", "X", "X", "X", "X", "X", "X"],
                    ["X", " ", " ", " ", "X", " ", "X"],
                    ["X", " ", "X", " ", "X", " ", " "],
                    ["X", " ", "X", " ", "X", " ", "X"],
                    ["X", " ", "X", " ", " ", " ", "X"],
                    ["X", " ", "X", "X", "X", "X", "X"],
                    ]
        self.ply = pos(5, 1)
        self.end = pos(2, 6)
        self.maze[self.ply.y][self.ply.x] = "P"
        self.maze[self.end.y][self.end.x] = "E"
        self.stack = Stack()
    
    def isInBound(self, y, x):
        if y>=0 and x>=0 and y<len(self.maze) and x<len(self.maze[0]):
            return True
        else:
            return False
    
    def print(self):
        os.system("cls")
        print("\n\n\n")
        for row in self.maze:
            for col in row:
                print(col," ", end="")
            print("")
        print("\n\n\n")
    
    def printEND(self):
        os.system("cls")
        print("\n\n\n")
        print(">>>>> Congraturation!!! <<<<<")
        print("\n\n\n")
        keyboard.wait("")

    def move_up(self):
        next_move = pos(self.ply.y - 1, self.ply.x)
        if self.isInBound(next_move.y, next_move.x):
            point = self.stack.push(self.ply)
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"

                self.ply = next_move
                time.sleep(0.25)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True , point
    
    def move_down(self):
        next_move = pos(self.ply.y + 1, self.ply.x)
        if self.isInBound(next_move.y, next_move.x):
            point =self.stack.push(self.ply)
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"

                self.ply = next_move
                time.sleep(0.25)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True , point

    def move_left(self):
        next_move = pos(self.ply.y , self.ply.x - 1)
        if self.isInBound(next_move.y, next_move.x):
            point =self.stack.push(self.ply)
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
            
                self.ply = next_move
                time.sleep(0.25)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True , point
    
    def move_right(self):
        next_move = pos(self.ply.y, self.ply.x+1)
        if self.isInBound(next_move.y, next_move.x):
            point =self.stack.push(self.ply)
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
            
                self.ply = next_move
                time.sleep(0.25)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True , point
    
    def undo_move(self):
        if not self.stack.isEmpty():
            Stack.push(prev_pos)
            prev_pos = self.stack.pop()
            self.ply = prev_pos
            self.maze[prev_pos.y][prev_pos.x] =   Stack.__len__.points
            return
        

class Stack:

    def __init__(self):
        self._top = None
        self._size = 0

    def isEmpty(self):
        return self._top is None
    
    def __len__(self):
        return self._size
    
    def peek(self):
        assert not self.isEmpty(), "Cannot peek at an empty stack"
        return self._top.item

    def pop(self):
        assert not self.isEmpty(), "Cannot pop from an empty stack"
        node = self._top
        self._top = self._top.next
        self._size = self._size - 1
        return node.item

    def push(self, item):
        self._top = _StackNode(item, self._top)
        self._size = self._size + 1

class _StackNode:
    def __init__(self, item, link):
        self.item = item
        self.next = link


if __name__ == '__main__':
    m = maze()
    m.print()

    while True:
        if keyboard.is_pressed("q"):
            print("Quit Program")
            break
        if keyboard.is_pressed("w"):
            if m.move_up():
                p = m.move_up
                m.print()
        if keyboard.is_pressed("s"):
            if m.move_down():
                p = m.move_down
                m.print()
        if keyboard.is_pressed("a"):
            if m.move_left():
                p = m.move_left
                m.print()
        if keyboard.is_pressed("d"):
            if m.move_right():
                p = m.move_right
                m.print()
        if keyboard.is_pressed("z"): 
            m.undo_move()
            m.print()
            break
