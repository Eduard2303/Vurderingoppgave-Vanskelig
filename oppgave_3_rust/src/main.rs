
fn main() {

    // Define varibles
    let mut next_nodes: Vec<(isize,isize)> = Vec::new(); // Makes a vector arrray for storeing next nodes to explore.
    let mut explored_nodes: Vec<(isize,isize)> = vec![(0,0)]; // Makes vector for explored nodes and adds the tuple 0,0.
    let is_solvable: bool = false;
    let maze: [[isize; 10]; 9] = [
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ] ,
        [1, 0, 1, 0, 1, 1, 1, 1, 0, 1 ] ,
        [1, 1, 1, 0, 1, 1, 0, 1, 0, 1 ] ,
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 1 ] ,
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1 ] ,
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 0 ] ,
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 1 ] ,
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ] ,
        [1, 1, 0, 0, 0, 1, 1, 1, 0, 1 ]
        ];
    
    //Temp var
    let row: isize = 1;
    let column: isize = 1;    




    find_neighbours( row,column,maze, &mut explored_nodes, &mut next_nodes);
    }

fn find_neighbours( row:isize, column:isize, maze: [[isize; 10]; 9], explored_nodes: &mut Vec<(isize,isize)>, next_nodes: &mut Vec<(isize,isize)>) { // -> (Vec<(isize,isize)>, Vec<(isize,isize)>)
    let row_vector: [isize; 4] = [1, -1, 0, 0];
    let column_vector: [isize; 4] = [0, 0, -1, 1];
    let mut step: usize = 0;

    

    loop {
        if step >= row_vector.len() {continue}; //Loop runs 4 times then ends.
        let new_pos: (isize, isize) = (row + row_vector[step], column + column_vector[step]); // Makes new pos Varible.
        

        if new_pos.0 >= 0 && new_pos.0 as usize > usize::MAX - 10 && new_pos.1 >= 0 && new_pos.1 as usize > usize::MAX - 10 {continue}; // checks if row and collum are in the maze.
        if maze[new_pos.0 as usize][new_pos.1 as usize] == 0 {continue;} // If the cell is a wall we dont add it and continue the loop.
        
        
        if explored_nodes.iter().any(|&tuple| tuple == new_pos) && next_nodes.iter().any(|&tuple| tuple == new_pos){ //Iterates trough the explored_nodes and next_nodes vector arrays and compares it to new_pos
            continue; // Continues to next loop
        }   else {next_nodes.push(new_pos);} // If not placeses new_pos in next_nodes.
        
        step = step + 1; // Check if the loops has ended.  
    
        
    }
    for n in next_nodes {
        println!("Value ({},{})", n.0,n.1)
    }
} 




    
