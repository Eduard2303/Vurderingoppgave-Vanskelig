fn main() {

    // Define varibles
    
    let explored_nodes: Vec<(isize,isize)> = vec![(0,0)]; // Makes vector for explored nodes and adds the tuple 0,0.
    
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
        
    find_neighbours(maze, explored_nodes);
    }

fn find_neighbours(maze: [[isize; 10]; 9], explored_nodes: &mut Vec<(isize,isize)>) {
    let row: isize = 1;
    let column: isize = 1;
    
    let row_vector: [isize; 4] = [1, -1, 0, 0];
    let column_vector: [isize; 4] = [0, 0, -1, 1];
    let mut step: usize = 0;
    let valid_paths: Vec<(isize,isize)> = Vec::new();

    println!("{:?}",maze);

    loop {
        if step >= row_vector.len() {continue}; //Loop runs 4 times then ends.
        let new_row: isize = row + row_vector[step]; 
        let new_collum: isize = column + column_vector[step];
        
        if new_row >= 0 && new_row as usize > usize::MAX - 10 && new_collum >= 0 && new_collum as usize > usize::MAX - 10 {break}; // checks if row and collum are in the maze.
        
        let new_pos: (isize, isize) = (new_row, new_collum);
        
        println!("Vector r,c {},{}", row_vector[step],column_vector[step]);
        println!("new_pos {},{}", new_pos.0, new_pos.1);
        
        let node: isize = maze[new_pos.0 as usize][new_pos.1 as usize]; 
        println!("{}", node);

        if explored_nodes.iter().any(|&tuple| tuple == new_pos){ //Iterates trough the expored nodes vector array and compares it to new_pos
            continue;
        }   else {explored_nodes.push(new_pos);}
        

        step = step + 1;      
    }
      
}   




    
