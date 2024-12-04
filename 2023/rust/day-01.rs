use std::io::{self};
use std::fs::read_to_string;

fn read_lines(filename: &str) -> Vec<String> {
    let mut result = Vec::new();
    for line in read_to_string(filename).unwrap().lines() {
        result.push(line.to_string())
    }
    result
}

fn solve_1(lines: Vec<String>) -> u32 {
    let mut result = Vec::new();
    for line in lines {
        for c in line.chars() {
            if c.is_digit(10) {
                let i:u32 = c.to_digit(10).unwrap();
                result.push(i);
            }
        }
    }
    result.first().unwrap() * 10 + result.last().unwrap()
}

fn main() -> io::Result<()> {
    let lines = read_lines("../data/day-01.txt");
    let result1 = solve_1(lines);
    println!("Day 01 - Result 1: {}", result1);

    Ok(())
}
