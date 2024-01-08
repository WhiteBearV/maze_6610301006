import os
import time
import sys 

mytime = 0.25
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

class maze:
 
    def __init__(self) -> None:
        self.maze = [
                    ["X", "X", "X", "X", "X", "X", "X"],
                    ["X", " ", "X", " ", "X", " ", "X"],
                    ["X", " ", "X", " ", "X", " ", " "],
                    ["X", " ", "X", " ", "X", " ", "X"],
                    ["X", " ", " ", " ", " ", " ", "X"],
                    ["X", " ", "X", "X", "X", "X", "X"],
                    ]
        self.ply = pos(5, 1)
        self.end = pos(2, 6)
        self.maze[self.ply.y][self.ply.x] = "P"
        self.maze[self.end.y][self.end.x] = "E"
    
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
        sys.exit()


    def move_up(self):
        next_move = pos(self.ply.y-1, self.ply.x)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
                time.sleep(mytime)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True
    
    def move_down(self):
        next_move = pos(self.ply.y + 1, self.ply.x)
        if self.isInBound(next_move.y, next_move.x):
            if self.maze[next_move.y][next_move.x] == (" "):
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
                time.sleep(mytime)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True

    def move_left(self):
        next_move = pos(self.ply.y, self.ply.x-1)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
                time.sleep(mytime)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True

    def move_right(self):
        next_move = pos(self.ply.y, self.ply.x+1)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
                time.sleep(mytime)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True
        
class pos:
    def __init__(self) -> None:
        self.y = None
        self.x = None
    
    def __init__(self, y, x) -> None:
        self.y = y
        self.x = x

    def __str__ (self) -> str:
        return f"Pos(x={self.y}, y={self.x})"
    
if __name__ == '__main__':
    m = maze()
    m.print()
    stack = Stack()
    visited = set()

    print("START")

    while True:
        current_pos = (m.ply.y, m.ply.x)
        m.ply = pos(current_pos[0],current_pos[1])
        if current_pos not in visited:
            visited.add(current_pos)
            
            if m.maze[m.ply.y - 1][m.ply.x] != "X" and (m.ply.y - 1, m.ply.x) not in visited:
                m.move_up()
                m.print()
                stack.push(current_pos)
                print("MOVE_UP")    
            #    input()

            elif m.maze[m.ply.y + 1][m.ply.x] != "X" and (m.ply.y + 1, m.ply.x) not in visited:
                m.move_down()
                m.print()
                stack.push(current_pos)
                print("MOVE_DOWN")
            #    input()

            elif m.maze[m.ply.y][m.ply.x + 1] != "X" and (m.ply.y, m.ply.x + 1) not in visited:
                m.move_right()
                m.print()
                stack.push(current_pos)
                print("MOVE_RIGHT")
            #    input()

            elif m.maze[m.ply.y][m.ply.x - 1] != "X" and (m.ply.y, m.ply.x - 1) not in visited:
                m.move_left()
                m.print()
                stack.push(current_pos)
                print("MOVE_LEFT")
              #  input()

            else:

                Deadend = True

                while not stack.isEmpty() and Deadend == True : # and m.maze[m.ply.y][m.ply.x] == "P" :
                    lastmove = stack.pop()
                    visited.remove(lastmove)
                    m.maze[current_pos[0]][current_pos[1]] = "D"
                    m.ply = pos(lastmove[0],lastmove[1])
                    m.maze[m.ply.y][m.ply.x] = "P"
                    m.print()
                    print('Nope No Pass')
                    Deadend = False

