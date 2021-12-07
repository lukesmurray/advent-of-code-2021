import fs from "fs/promises";
import * as R from "ramda";

const readInput = R.curry(fs.readFile)(R.__, "utf8");
const extractNumber = R.pipe(R.match(/(\d+)/), R.head, Number);

const state = { h: 0, d: 0 };

const processInput = R.pipe(
  R.split("\n"),
  R.map(
    R.cond([
      [R.test(/forward \d+/), R.pipe(extractNumber, R.assoc("h", R.__, state))],
      [R.test(/down \d+/), R.pipe(extractNumber, R.assoc("d", R.__, state))],
      [
        R.test(/up \d+/),
        R.pipe(extractNumber, R.negate, R.assoc("d", R.__, state)),
      ],
    ])
  ),
  R.reduce(R.mergeWith(R.add), { h: 0, d: 0 }),
  R.converge(R.multiply, [R.prop("h"), R.prop("d")]),
  console.log
);

const solve = R.pipe(readInput, R.andThen(processInput));

await solve("i");
