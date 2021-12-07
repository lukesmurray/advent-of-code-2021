import fs from "fs/promises";
import * as R from "ramda";

const readInput = R.curry(fs.readFile)(R.__, "utf8");

const processInput = R.pipe(
  R.split("\n"),
  R.map(R.pipe(R.match(/(\w+) (\d+)/), R.slice(1, 3), R.adjust(1, Number))),
  R.reduce(
    ([depth, position, aim], [command, value]) => {
      if (command === "forward") {
        return [depth + aim * value, position + value, aim];
      } else if (command === "up") {
        return [depth, position, aim - value];
      } else if (command === "down") {
        return [depth, position, aim + value];
      } else {
        return [depth, position, aim];
      }
    },
    [0, 0, 0]
  ),
  R.take(2),
  R.apply(R.multiply),
  R.tap(console.log)
);

const solve = R.pipe(readInput, R.andThen(processInput));

await solve("i");
