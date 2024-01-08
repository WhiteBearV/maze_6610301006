import heapq
import time
import os
import keyboard

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


class pos:
    def __init__(self) -> None:
        self.y = None
        self.x = None
    
    def __init__(self, y, x) -> None:
        self.y = y
        self.x = x

class maze:
    def __init__(self) -> None:
        self.maze = [
                    ["X", "X", "X", "X", "X", "X", "X"],
                    ["X", " ", "X", " ", "X", " ", "X"],
                    ["X", " ", " ", " ", "X", " ", " "],
                    ["X", " ", "X", " ", "X", " ", "X"],
                    ["X", " ", "X", " ", " ", " ", "X"],
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
        keyboard.wait("")


    def move_up(self):
        next_move = pos(self.ply.y-1, self.ply.x)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
                time.sleep(1)
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
                time.sleep(1)
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
                time.sleep(1)
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
                time.sleep(1)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True

class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.start = self.find_start()
        self.end = self.find_end()

    def find_start(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.maze[i][j] == 'P':
                    return i, j

    def find_end(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.maze[i][j] == 'E':
                    return i, j



    def heuristic(self, current, goal):
        return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

    def astar(self):
        start_node = (self.start, 0)
        heap = [start_node]
        visited = set()

        while heap:
            current, cost = heapq.heappop(heap)

            if current == self.end:
                return False

            if current in visited:
                continue

            visited.add(current)

            row, col = current
            directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                if maze.isInBound(self,new_col,new_row):
                    new_cost = cost + 1 + self.heuristic((new_row, new_col), self.end)
                    heapq.heappush(heap, ((new_row, new_col), new_cost))

        return True

    def auto_solve_new(self):
        if self.astar():
            stack = Stack()
            visited = set()
        while True:
            ceakpoint = self.find_start()
            m.ply = pos(ceakpoint[0],ceakpoint[1])
            if ceakpoint not in visited:
                visited.add(ceakpoint)
            
            if m.maze[m.ply.y - 1][m.ply.x] != "X" and (m.ply.y - 1, m.ply.x) not in visited:
                m.move_up()
                m.print()
                stack.push(ceakpoint)
                print("MOVE_UP")    

            elif m.maze[m.ply.y + 1][m.ply.x] != "X" and (m.ply.y + 1, m.ply.x) not in visited:
                m.move_down()
                m.print()
                stack.push(ceakpoint)
                print("MOVE_DOWN")

            elif m.maze[m.ply.y][m.ply.x + 1] != "X" and (m.ply.y, m.ply.x + 1) not in visited:
                m.move_right()
                m.print()
                stack.push(ceakpoint)

            elif m.maze[m.ply.y][m.ply.x - 1] != "X" and (m.ply.y, m.ply.x - 1) not in visited:
                m.move_left()
                m.print()
                stack.push(ceakpoint)
                print("MOVE_LEFT")

            else:
                Noway = True
                while not stack.isEmpty() and Noway == True : # and m.maze[m.ply.y][m.ply.x] == "P" :
                    lastmove = stack.pop()
                    visited.remove(lastmove)
                    m.maze[ceakpoint[0]][ceakpoint[1]] = "N"
                    m.ply = pos(lastmove[0],lastmove[1])
                    m.maze[m.ply.y][m.ply.x] = "P"
                    m.print()
                    print('Nope No Pass')
                    Noway = False

    def auto_solve_old(self):
        if self.astar():
            ceakpoin = self.find_start()
        while True :
            maze.print(self)
            print("Auto-solving the maze:")
            time.sleep(1.50)
            ceakpoin = self.move_towards_end_new(ceakpoin)
            next_move = pos(ceakpoin[0], ceakpoin[1])

            if maze.isInBound(self,next_move.y, next_move.x) and self.maze[next_move.y][next_move.x] == "E":
                self.maze.printEND()



            

    def move_towards_end_new(self, ceakpoin):
        stack = Stack()
        visited = set()
        while True:
            row, col = ceakpoin
            directions = [ceakpoin[0],ceakpoin[1]]
            stack.push(directions)
            if maze.isInBound(self,row,col) and self.maze[row][col] == ' ':
                self.maze[row][col] = '1'
                self.maze[row][col] = 'P'

                return row, col
            return ceakpoin  

# Example Usage:
if __name__ == '__main__':

    m = maze()
    m.print()
    solver = MazeSolver(m.maze)
    solver.auto_solve_new()
    m.print

