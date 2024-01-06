import heapq
import time
import os
import keyboard
import time

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
                time.sleep(0.25)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True
    
    def move_down(self):
        next_move = pos(self.ply.y+1, self.ply.x)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
                time.sleep(0.25)
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
                time.sleep(0.25)
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
                time.sleep(0.25)
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
                
    def find_path(self):
        self.start = self.find_start()
        self.end = self.find_end()


    def is_valid_move(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols and self.maze[row][col] != 'X'

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
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                if self.is_valid_move(new_row, new_col):
                    new_cost = cost + 1 + self.heuristic((new_row, new_col), self.end)
                    heapq.heappush(heap, ((new_row, new_col), new_cost))

        return False

    def auto_solve(self):
        if self.astar():
            print("Auto-solving the maze:")
            current = self.start
            ed = self.end
            while current != self.end:
                print("Moving to", current)
                time.sleep(0.25)  # Optional: Add a delay for visualization
                current = self.move_towards_end(current)
                next_move = pos(current,ed)
            if self.isInBound(next_move.y,next_move.x):
                if self.maze[next_move.y][next_move.x] == " ":
                    self.maze[self.ply.y][self.ply.x] = " "
                    self.maze[next_move.y][next_move.x] = "P"
                    self.ply = next_move
                    time.sleep(0.25)
                    if self.maze[next_move.y][next_move.x] == "E":
                        self.printEND()

        
    def move_towards_end(self, current):
        row, col = current
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            if self.is_valid_move(new_row, new_col) and self.maze[new_row][new_col] == ' ':
                self.maze[row][col] = ' '
                self.maze[new_row][new_col] = 'P'

                return new_row, new_col
            
    def auto_move(self):
        path = self.find_path()
        if path:
            for step in path[1]:  # ข้ามตำแหน่งเริ่มต้น
                direction = " "
                if step.y < self.start.y:
                    direction = "up"
                    maze.move_up()
                elif step.y > self.start.y:
                    direction = "down"
                    maze.move_down()
                elif step.x < self.start.x:
                    direction = "left"
                    maze.move_left()
                elif step.x > self.start.x:
                    direction = "right"
                    maze.move_right()

                getattr(self, f"move_{direction}")  # เรียกฟังก์ชันเคลื่อนที่ตามทิศทาง
                self.print()  # พิมพ์แผนที่หลังจากเคลื่อนที่
                time.sleep(0.25)  # หน่วงเวลาเพื่อให้เห็นการเคลื่อนที่


# Example Usage:
if __name__ == '__main__':

    m = maze()
    m.print()

    while True:
        solver = MazeSolver(m.maze)
        solver.auto_move()
        m.print

