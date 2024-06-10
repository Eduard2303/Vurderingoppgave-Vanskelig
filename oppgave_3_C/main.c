#include <stdio.h>
#include <string.h>


int find_neighbours(int graph[9][10], int marked_graph[9][10], int (*valid_paths)[2], int row, int column) {
    int row_vertecies[] = {-1, +1, 0, 0};
    int column_vertecies[] = {0, 0, -1, +1};

    for (int direction = 0; direction < 4; direction++) {
        int next_row = row + row_vertecies[direction];
        int next_column = column + column_vertecies[direction];

        if (next_row >= 0 && next_row < 9 && next_column >= 0 && next_column < 10) { // checks if row is 0 or higher but also not higher that size of row
            if (marked_graph[next_row][next_column] != 1) {
                if (graph[next_row][next_column] == 1) {
                    valid_paths[direction][0] = next_row;
                    valid_paths[direction][1] = next_column;
                }
            }
        }
    };

}

// This functions takes in a pointer to the first element in the matrix and also specifies the lenght of each subarray [10 of type int]
int dfs(int (*graph)[10], int (*marked_graph)[10], int row, int column) {
    if (row == 8 && column == 9) {
        return 1;
    }

    marked_graph[row][column] = 1; // This marks the current vertex in our marked_graph
    
    int valid_paths[4][2] = {0};
    find_neighbours(graph, marked_graph, &valid_paths[0], row, column);

    //printf("Valid paths: \n", valid_paths);

    for (int i = 0; i < 4; i++) {
        if (valid_paths[i][0] == 0 && valid_paths[i][1] == 0) {
        } else {
            if (dfs(graph, marked_graph, valid_paths[i][0], valid_paths[i][1]) == 1) {  
                return 1;
            }
        }
    };

    return 0;
};

int main() {
    int maze[9][10] = {
        {1, 0, 1, 1, 1, 1, 0, 1, 1, 1 },
        {1, 0, 1, 0, 1, 1, 1, 1, 0, 1 },
        {1, 1, 1, 0, 1, 1, 0, 1, 0, 1 },
        {0, 0, 0, 0, 1, 0, 0, 0, 0, 1 },
        {1, 1, 1, 0, 1, 1, 1, 1, 1, 1 },
        {1, 0, 1, 1, 1, 1, 0, 1, 0, 0 },
        {1, 0, 1, 0, 0, 0, 0, 0, 0, 1 },
        {1, 0, 1, 1, 1, 1, 0, 1, 1, 1 },
        {1, 1, 0, 0, 0, 1, 1, 1, 0, 1 }
    };

    // Creates identical array of maze with all values set to 0 / FALSE
    int marked_vertices[sizeof(maze) / sizeof(maze[0])][sizeof(maze[0]) / sizeof(maze[0][0])] = {{0}};


    int isSolvable = dfs( &maze[0], &marked_vertices[0], 0, 0); // passes a pointer to the first memory address / position of the 2D arrays
    printf("Is Maze solvable: %d\n", isSolvable);
}