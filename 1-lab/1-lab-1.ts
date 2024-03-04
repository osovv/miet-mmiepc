function isValidPositiveInteger(input: string): boolean {
  const n = parseInt(input);
  return Number.isInteger(n) && n > 0;
}

function inputNumber(message: string): number {
  while (true) {
    const userInput = prompt(message) ?? "";
    if (isValidPositiveInteger(userInput)) {
      return parseInt(userInput);
    } else {
      console.log("Ошибка: Введите положительное целое число.");
    }
  }
}

function extendedEuclideanAlgorithm(e: number, n: number): number {
  let [oldR, r] = [e, n];
  let [oldS, s] = [1, 0];
  let [oldT, t] = [0, 1];

  while (r !== 0) {
    const quotient = Math.floor(oldR / r);
    [oldR, r] = [r, oldR - quotient * r];
    [oldS, s] = [s, oldS - quotient * s];
    [oldT, t] = [t, oldT - quotient * t];
  }

  if (oldR !== 1) {
    throw new Error("No multiplicative inverse exists.");
  }

  return oldS < 0 ? oldS + n : oldS;
}

function main() {
  const e = inputNumber("Введите число e:");
  const n = inputNumber("Введите число n:");

  try {
    const d = extendedEuclideanAlgorithm(e, n);
    console.log("d =", d);
  } catch (error) {
    console.log(error.message);
  }
}

main();
