import fs from "fs";
import * as R from "ramda";

const readFile = R.call(R.curry(fs.readFileSync), R.__, "utf8");

const parseBinary = R.call(R.curry(parseInt), R.__, 2);

const processInput = R.pipe(
  R.split("\n"),
  // make an array for each bit
  R.transpose,
  // count instances of each number
  R.map(R.countBy(R.identity)),
  // keep the number with the most instances
  R.map(R.pipe(R.toPairs, R.apply(R.maxBy(R.nth(1))), R.nth(0))),
  // convert the list of numbers to a string
  R.join(""),
  // multiple gamma/epsilon
  R.converge(R.multiply, [
    // parse the string as a binary
    parseBinary,
    // invert the string then parse it as binary
    R.pipe(R.map(Number), R.map(R.subtract(1)), R.join(""), parseBinary),
  ]),
  R.tap(console.log)
);

const solve = R.pipe(readFile, processInput);

solve("i");
