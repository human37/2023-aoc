import { readFileSync } from "fs";

let instructions = [];
const network = {};

const read_input = () => {
  const file = readFileSync("./p8-input.txt", "utf-8");
  const lines = file.split("\n");
  instructions = lines[0].split("").map((dir) => {
    if (dir === "L") return 0;
    if (dir === "R") return 1;
  });
  for (let i = 2; i < lines.length; i++) {
    const line = lines[i].split(" = ");
    const key = line[0];
    const values = line[1].split(", ");
    const lv = values[0].replace("(", "");
    const rv = values[1].replace(")", "");
    network[key] = [lv, rv];
  }
};

const p1 = () => {
  let steps = 0;
  let currentNode = "AAA";
  while (currentNode !== "ZZZ") {
    for (let i = 0; i < instructions.length; i++) {
      currentNode = network[currentNode][instructions[i]];
      steps++;
      if (currentNode === "ZZZ") break;
    }
  }
  return steps;
};

const main = () => {
  read_input();
  console.log("Steps required to reach ZZZ: ", p1());
};

main();
