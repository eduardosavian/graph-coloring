use std::env;
use std::process::ExitCode;

fn can_this_color_be_used(graph: &Vec<Vec<i32>>, row: usize, col: usize, color: i32) -> bool {
    if graph[row].iter().any(|&c| c == color) {
        return false;
    }
    if graph.iter().any(|row| row[col] == color) {
        return false;
    }
    let block_size: usize = (graph.len() as f64).sqrt() as usize;
    let start_row = (row / block_size) * block_size;
    let start_col = (col / block_size) * block_size;
    for i in 0..block_size {
        for j in 0..block_size {
            if graph[start_row + i][start_col + j] == color {
                return false;
            }
        }
    }
    return true;
}

fn find_non_colored_location(graph: &Vec<Vec<i32>>) -> Option<(usize, usize)> {
    for (i, row) in graph.iter().enumerate() {
        if let Some(j) = row.iter().position(|col| *col == 0) {
            return Some((i, j));
        }
    }
    None
}

fn graph_coloring(
    graph: &mut Vec<Vec<i32>>,
    start_point: (usize, usize),
    curr_iteration: u64,
) -> bool {
    let (mut row, mut col) = start_point;
    if curr_iteration != 0 {
        let empty = find_non_colored_location(&graph);
        if empty.is_none() {
            return true;
        }
        (row, col) = empty.unwrap();
    }
    for color in 1..=graph.len() {
        if can_this_color_be_used(&graph, row, col, color as i32) {
            graph[row][col] = color as i32;
            let cond: bool = graph_coloring(graph, (0, 0), curr_iteration + 1);
            if cond {
                return true;
            } else {
                graph[row][col] = 0;
            }
        }
    }
    return false;
}

fn graph_to_json(graph: &Vec<Vec<i32>>) -> String {  
    let mut res = String::from("\"graph\":[");
    
    for row in 0..graph.len() {
        res.push_str("[");
        for col in 0..graph.len() {
            res.push_str(&format!("{},", graph[row][col]));
        }                
        res.pop(); // Remove vírgula
        res.push_str("],"); 
    }
    res.pop(); // Remove vírgula
    res.push_str("]"); 

    res
}

fn main() -> ExitCode {
    let args: Vec<String> = env::args().collect();

    // Less or more args than 3
    if args.len() != 4 { return ExitCode::from(1) }

    // Invalid arg for graph_order
    let graph_order: usize = match args[1].parse() {
        Ok(e) => e,
        _ => return ExitCode::from(2)
    };

    // Graph order different from 4 or 9 or 16
    if [4, 9, 16].contains(&graph_order) == false { 
        return ExitCode::from(3); 
    }

    let mut graph = generate_partial_sudoku(graph_order);

    // Invalid arg for row number
    let row: usize = match args[2].parse() {
        Ok(e) => if e >= graph_order { return ExitCode::from(4)} else {e}
        _ => return ExitCode::from(5)
    };

    // Invalid arg for col number
    let col: usize = match args[3].parse() {
        Ok(e) => if e >= graph_order { return ExitCode::from(6)} else {e}
        _ => return ExitCode::from(7)
    };

    // Position on graph is not empty
    if graph[row][col] != 0 {
        return ExitCode::from(8);
    }

    println!("{}", graph_to_json(&graph));
    graph_coloring(&mut graph, (row, col), 0);
    println!("{}", graph_to_json(&graph));

    ExitCode::from(0)
}




// autogerated crate that returns a partially filled sudoku board:
use rand::seq::SliceRandom;
use rand::thread_rng;
use std::vec::Vec;

fn generate_partial_sudoku(size: usize) -> Vec<Vec<i32>> {
    let base = (size as f64).sqrt() as usize;
    let mut rng = thread_rng();
    let pattern = |r: usize, c: usize| -> usize { (base * (r % base) + r / base + c) % size };
    fn shuffle(s: &mut [usize]) {
        s.shuffle(&mut thread_rng());
    }
    let r_base: Vec<usize> = (0..base).collect();
    let mut rows: Vec<usize> = Vec::new();
    let mut cols: Vec<usize> = Vec::new();
    for g in r_base.iter().copied() {
        let mut r_base_shuffle = r_base.clone();
        shuffle(&mut r_base_shuffle);
        for r in r_base_shuffle.iter().copied() {
            rows.push(g * base + r);
        }
    }
    for g in r_base.iter().copied() {
        let mut c_base_shuffle = r_base.clone();
        shuffle(&mut c_base_shuffle);
        for c in c_base_shuffle.iter().copied() {
            cols.push(g * base + c);
        }
    }
    let mut nums: Vec<usize> = (1..=base * base).collect();
    shuffle(&mut nums);
    let mut board: Vec<Vec<i32>> = rows
        .iter()
        .map(|&r| cols.iter().map(|&c| nums[pattern(r, c)] as i32).collect())
        .collect();
    let squares = size * size;
    let empties = squares * 3 / 4;
    let mut positions: Vec<usize> = (0..squares).collect();
    positions.shuffle(&mut rng);
    for &p in positions.iter().take(empties) {
        board[p / size][p % size] = 0;
    }
    board
}
