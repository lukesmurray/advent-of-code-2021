import fs from "fs";
import * as R from "ramda";

const readFile = R.call(R.curry(fs.readFileSync), R.__, "utf8");
const applyN = R.compose(R.reduceRight(R.compose, R.identity), R.repeat);
const simulateDay = R.pipe(
  R.toPairs,
  R.map(
    R.cond([
      [
        R.pipe(R.nth(0), R.equals("0")),
        R.converge(R.concat, [
          R.pipe(R.nth(1), R.of, R.prepend("6")),
          R.pipe(R.nth(1), R.of, R.prepend("8")),
        ]),
      ],
      [
        R.T,
        R.converge(R.concat, [
          R.pipe(R.nth(0), Number, R.dec, String, R.of),
          R.pipe(R.nth(1), R.of),
        ]),
      ],
    ])
  ),
  R.flatten,
  R.splitEvery(2),
  R.groupBy(R.nth(0)),
  R.map(R.pipe(R.map(R.nth(1)))),
  R.map(R.sum)
);

const processInput = R.pipe(
  R.unapply(R.identity),
  R.adjust(0, R.pipe(R.nth(0), readFile, R.split(","), R.countBy(R.identity))),
  R.converge(R.call, [
    R.converge(R.call, [R.always(applyN), R.always(simulateDay), R.nth(1)]),
    R.nth(0),
  ]),
  R.values,
  R.sum,
  console.log
);

const solve = R.pipe(processInput);

solve("i", 80);
