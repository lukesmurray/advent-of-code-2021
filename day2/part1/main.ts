import fs from "fs/promises";
import * as R from "ramda";

const input = () => fs.readFile("i", "utf8");

const getNumber = R.pipe(R.match(/\d+/), R.head, Number);

type State = {
  horizontal: number;
  depth: number;
};

const incrementHorizontal =
  (state: State): ((by: number) => State) =>
  (n) => ({
    ...state,
    horizontal: state.horizontal + n,
  });

const incrementDepth =
  (state: State): ((by: number) => State) =>
  (n) => ({
    ...state,
    depth: state.depth + n,
  });

const solve = R.pipe(
  input,
  R.andThen(
    R.pipe(
      R.split("\n"),
      R.reduce(
        (acc, elem) =>
          R.cond([
            [
              R.test(/forward \d+/),
              R.pipe(getNumber, incrementHorizontal(acc)),
            ],
            [R.test(/down \d+/), R.pipe(getNumber, incrementDepth(acc))],
            [
              R.test(/up \d+/),
              R.pipe(getNumber, R.negate, incrementDepth(acc)),
            ],
          ])(elem),
        { horizontal: 0, depth: 0 }
      ),
      (v) => R.multiply(R.prop("horizontal", v), R.prop("depth", v)),
      console.log
    )
  )
);

await solve();
