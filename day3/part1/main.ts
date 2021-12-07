import fs from "fs";
import * as R from "ramda";

const readFile = R.call(R.curry(fs.readFileSync), R.__, "utf8");

const parseBinary = R.call(R.curry(parseInt), R.__, 2);

const processInput = R.pipe(
  R.split("\n"),
  R.transpose,
  R.map(R.countBy(R.identity)),
  R.map(R.pipe(R.toPairs, R.apply(R.maxBy(R.nth(1))), R.nth(0))),
  R.join(""),
  R.converge(R.multiply, [
    parseBinary,
    R.pipe(R.map(Number), R.map(R.subtract(1)), R.join(""), parseBinary),
  ]),
  R.tap(console.log)
);

const solve = R.pipe(readFile, processInput);

solve("i");
