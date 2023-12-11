import { readFileSync } from "fs";

let sequences = [];

const read_input = () => {
  sequences = readFileSync("./p9-input.txt", "utf-8")
    .split("\n")
    .map((line) => line.split(" ").map((n) => parseInt(n)))
    .map((line) => line.reverse());
};

const predictNext = (sequence) => {
  let last = sequence[sequence.length - 1];
  if (new Set(sequence).size === 1) return last;
  const newSequence = [];
  for (let i = 0; i < sequence.length - 1; i++) {
    newSequence.push(sequence[i + 1] - sequence[i]);
  }
  return last + predictNext(newSequence);
};

const p1 = () => {
  let sum = 0;
  for (let i = 0; i < sequences.length; i++) {
    sum += predictNext(sequences[i]);
  }
  return sum;
};

const main = () => {
  read_input();
  console.log("Extrapolated values sum:", p1());
};

main();
