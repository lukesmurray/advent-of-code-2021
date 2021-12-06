import fs from "fs/promises";
import * as R from "ramda";

const isIncreasing = (l: [number, number]): boolean => l[1] > l[0];

const readInput = () => fs.readFile("i", "utf8");

const solve = R.pipe(
  readInput,
  R.andThen(
    R.pipe(
      R.split("\n"),
      R.map(Number),
      R.aperture(3),
      R.map(R.sum),
      R.aperture(2),
      R.map(isIncreasing),
      R.filter(R.identity),
      R.length,
      console.log
    )
  )
);

await solve();
