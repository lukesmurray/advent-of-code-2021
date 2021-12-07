import fs from "fs/promises";
import * as R from "ramda";

const readInput = R.curry(fs.readFile)(R.__, "utf8");

const solve = R.pipe(
  readInput,
  R.andThen(
    R.pipe(
      R.split("\n"),
      R.map(Number),
      R.aperture(3),
      R.map(R.sum),
      R.aperture(2),
      R.map(R.apply(R.flip(R.gt))),
      R.filter(R.identity),
      R.length,
      console.log
    )
  )
);

await solve("i");
