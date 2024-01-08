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
                
    def find_path(self):
        start = self.find_start()
        self.end = self.find_end()
        return start , self.end


    def is_valid_move(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols and self.maze[row][col] != 'X':
            return True
        else:
            return False

    def heuristic(self, current, goal):
        return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

    def astar(self):
        start_node = (self.start, 0)
        heap = [start_node]
        visited = set()

        while heap:
            current, cost = heapq.heappop(heap)

            if current == self.end:
                return True

            if current in visited:
                continue

            visited.add(current)

            row, col = current
            directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                if self.is_valid_move(new_row, new_col):
                    new_cost = cost + 1 + self.heuristic((new_row, new_col), self.end)
                    heapq.heappush(heap, ((new_row, new_col), new_cost))

        return False    
    """def astar(self):
        start_node = (self.start, 0)
        heap = [start_node]
        visited = set()

        while heap:
            current, cost = heapq.heappop(heap)

            if current == self.end:
                return True

            if current in visited:
                continue

            visited.add(current)

            row, col = current
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                if self.is_valid_move(new_row, new_col):
                    new_cost = cost + 1 + self.heuristic((new_row, new_col), self.end)
                    heapq.heappush(heap, ((new_row, new_col), new_cost))

        return False"""

    def auto_solve(self):
        if self.astar():
            current = self.find_start()
            ed = self.find_end()
            while current != ed:  
                maze.print(self)
                print("Auto-solving the maze:")  
                time.sleep(1.25)  # Optional: Add a delay for visualization
                current = self.move_towards_end_new(current)
                next_move = pos(current,ed)
            if self.is_valid_move(next_move.y,next_move.x):
                if self.maze[next_move.y][next_move.x] == " ":
                    self.maze[self.ply.y][self.ply.x] = " "
                    self.maze[next_move.y][next_move.x] = "P"
                    self.ply = next_move

                    time.sleep(1.25)
                    if self.maze[next_move.y][next_move.x] == "E" :
                        self.printEND()

    def auto_solve_new(self):
        if self.astar():
            current = self.find_start()
            end = self.find_end()
        while current != end:
            maze.print(self)
            print("Auto-solving the maze:")
            time.sleep(1.50)
            current = self.move_towards_end_new(current)
            next_move = pos(current[0], current[1])
            if self.is_valid_move(next_move.y, next_move.x) and self.maze[next_move.y][next_move.x] == "E":
                self.maze.printEND()
                break


            

    def move_towards_end_new(self, current):
        row, col = current
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if self.is_valid_move(new_row, new_col) and self.maze[new_row][new_col] == ' ':
                self.maze[row][col] = '1'
                self.maze[new_row][new_col] = 'P'

                print(dr, dc)

                return new_row, new_col
        return current   

# Example Usage:
if __name__ == '__main__':

    m = maze()
    m.print()
    """s = MazeSolver(m.maze)
    a,b = s.find_path()
    print(a)
    print(b)"""
    solver = MazeSolver(m.maze)
    solver.auto_solve_new()
    m.print

