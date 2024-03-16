/*
Day 1 puzzle
*/
function puzzle_part1(input) {
  var totalVales = 0;

  input.forEach((line, index, array) => {
    var testNum = 116;
    var firstNum = line.match(/[0-9]+/)[0].charAt(0);
    if (index == testNum) {
      console.log(firstNum);
    }
    var lastNum = line
      .split("")
      .reverse()
      .join("")
      .match(/[0-9]+/)[0]
      .charAt(0);
    if (index == testNum) {
      console.log(lastNum);
    }
    totalVales += parseInt(firstNum) * 10 + parseInt(lastNum);
  });
  return totalVales;
}

function puzzle_part1(input) {
  var totalVales = 0;

  input.forEach((line, index, array) => {
    //console.log(line);
    line = line
      .replaceAll("one", "o1e")
      .replaceAll("two", "t2o")
      .replaceAll("three", "t3e")
      .replaceAll("four", "f4r")
      .replaceAll("five", "f5e")
      .replaceAll("six", "s6x")
      .replaceAll("seven", "s7n")
      .replaceAll("eight", "e8t")
      .replaceAll("nine", "n9e");
    //console.log(line);
    //var testNum = 981;
    var firstNum = line.match(/[0-9]+/)[0].charAt(0);
    // if (index == testNum) {
    //   console.log(firstNum);
    // }
    var lastNum = line
      .split("")
      .reverse()
      .join("")
      .match(/[0-9]+/)[0]
      .charAt(0);
    // if (index == testNum) {
    //   console.log(lastNum);
    // }
    totalVales += parseInt(firstNum) * 10 + parseInt(lastNum);
  });
  return totalVales;
}

function readInputAsLines(filename) {
  try {
    const fs = require("fs");
    const data = fs.readFileSync(filename, "utf8");
    const lines = data.split("\n");
    return lines;
  } catch (err) {
    console.error(err);
  }
  return [];
}

console.log(puzzle_part1(readInputAsLines("input.txt")));
console.log(puzzle_part2(readInputAsLines("input.txt")));
