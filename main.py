# Name = Muhammad Ali Ahson
# Roll = 21i-2535
# Assignment 2

import sys
import numpy as np
import random
from DFS import DFS
from UCS import UCS
from A_star import AStar

def welcome():
    print("╔════════════════════════════════════════════════════════════════╗")
    print("║                                                                ║")
    print("║                    Welcome to the Jigsaw Game!                 ║")
    print("║                                                                ║")
    print("║            Get ready to challenge your puzzle-solving          ║")
    print("║            skills and enjoy hours of fun and excitement!       ║")
    print("║                                                                ║")
    print("║   Actions available:                                           ║")
    print("║   - Left          : Move the agent left                        ║")
    print("║   - Right         : Move the agent right                       ║")
    print("║   - Up            : Move the agent up                          ║")
    print("║   - Down          : Move the agent down                        ║")
    print("║   - NoOp          : Take no action                             ║")
    print("║   - Rotate_left   : Rotate the cell content 90° counterclockwise║")
    print("║   - Rotate_right  : Rotate the cell content 90° clockwise      ║")
    print("║                                                                ║")
    print("║   Remember:                                                    ║")
    print("║   - The environment is deterministic and partially observable. ║")
    print("║   - Your goal is to correctly place as many items as possible  ║")
    print("║     within the allowed number of moves.                        ║")
    print("║                                                                ║")
    print("║            Let the game begin and may the best agent win!      ║")
    print("║                                                                ║")
    print("╚════════════════════════════════════════════════════════════════╝")
    print("\nPlease select the type of agent you would like to use:")
    print("1) DFS")
    print("2) UCS")
    print("3) A*")
    

def select_agent_type():
    while True:
        choice = input("Enter your choice (1, 2, or 3): ")
        if choice == '1':
            print("You have selected DFS Search.")
            return 'DFS'
        elif choice == '2':
            print("You have selected UCS Search.")
            return 'UCS'
        elif choice == '3':
            print("You have selected A* Search.")
            return 'A*'
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def random_number(start, end, grid=False):
    if grid:
        a = random.randint(start, end)
        b = random.randint(start, end)
        return (a, b)


def main():
    grid_size = int(sys.argv[1])
    no_Movement = int(sys.argv[2])
    game_grid = [[random.randint(1, 25) for _ in range(grid_size)] for _ in range(grid_size)]
    starting = random_number(0, grid_size - 1, True)
    ending = random_number(0, grid_size - 1, True)
    print("The Size of the Grid is", grid_size)
    print("The Movements defined are", no_Movement)
    welcome()
    choice = select_agent_type()
    print("Starting point:", starting, "   Value is", game_grid[starting[0]][starting[1]])
    print("Ending point:", ending, "   Value is", game_grid[ending[0]][ending[1]])
    if choice == 'DFS':
        agent = DFS(game_grid,starting,ending,no_Movement)
        agent.dfs()
        agent.performance_measure()
    elif choice == "UCS":
        agent = UCS(game_grid,starting,ending,no_Movement)
        agent.ucs()
        agent.performance_measure()
    else:
        agent = AStar(game_grid,starting,ending,no_Movement)
        agent.a_star()
        agent.performance_measure()
    

if __name__ == "__main__":
    main()


