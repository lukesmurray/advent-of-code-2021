import fs from "fs";
import * as R from "ramda";

R.pipe(
  R.call(R.curry(R.flip(fs.readFileSync)), "utf8"),
  R.pipe(R.split("\n"), R.map(R.split("|")), R.map(R.map(R.trim))),
  R.map(R.apply(R.useWith(R.merge, [R.objOf("c"), R.objOf("l")]))),
  R.map(
    R.pipe(
      R.evolve({
        c: R.pipe(R.replace(/\s/g, ""), R.countBy(R.identity)),
        l: R.pipe(R.split(" "), R.map(R.map(R.identity))),
      }),
      R.converge(R.map, [
        R.pipe(R.prop("c"), R.flip(R.prop), R.compose(R.map)),
        R.prop("l"),
      ]),
      R.map(R.sum),
      R.map(
        R.flip(R.prop)({
          17: 1,
          25: 7,
          30: 4,
          34: 2,
          37: 5,
          39: 3,
          41: 6,
          42: 0,
          45: 9,
          49: 8,
        })
      ),
      R.join(""),
      Number
    )
  ),
  R.sum,
  console.log
)("i");
