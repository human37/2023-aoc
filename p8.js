import { readFileSync } from "fs";

let instructions = [];
const network = {};

const gcd = (a, b) => (b == 0 ? a : gcd(b, a % b));

const lcm = (a, b) => (a / gcd(a, b)) * b;

const lcmAll = (ns) => ns.reduce(lcm, 1);

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

const p2 = () => {
  let startNodes = Object.keys(network).filter((node) => node.endsWith("A"));
  let steps = [];
  for (let i = 0; i < startNodes.length; i++) {
    let currentNode = startNodes[i];
    let currentSteps = 0;
    while (!currentNode.endsWith("Z")) {
      for (let i = 0; i < instructions.length; i++) {
        currentNode = network[currentNode][instructions[i]];
        currentSteps++;
        if (currentNode.endsWith("Z")) break;
      }
    }
    steps.push(currentSteps);
  }
  return steps;
};

const main = () => {
  read_input();
  console.log("Steps required to reach ZZZ: ", p1());
  console.log(
    "Steps required to reach all nodes that end with Z: ",
    lcmAll(p2())
  );
};

main();
