import numpy as np
import skfuzzy as fuzz

METHODS = ("centroid", "bisector", "mom", "som", "lom")


def get_input(prompt: str) -> float:
    return float(input(f"enter {prompt}: "))


class Point(object):
    def __init__(self, x1: float = 0, x2: float = 0) -> None:
        self._x1: float = x1
        self._x2: float = x2

    @property
    def x1(self) -> float:
        return self._x1

    @property
    def x2(self) -> float:
        return self._x2

    def set_point(self) -> None:
        print("x1 and x2 must be 0 < x < 1 !")
        while self._x1 < 0 or self._x1 > 1:
            self._x1 = get_input("x1")
        while self._x2 < 0 or self._x2 > 1:
            self._x2 = get_input("x2")


class Rules(object):
    def __init__(self, *args: list[float]):
        self._rules: list[list[float]] = list(args)

    @property
    def rules(self) -> list[list[float]]:
        return self._rules.copy()

    def set_rules(self) -> None:
        for itr, _ in enumerate(self._rules):
            p1: float = get_input("p11")
            p2: float = get_input("p12")
            t: float = get_input("t")
            self._rules[itr].append(p1)
            self._rules[itr].append(p2)
            self._rules[itr].append(t)


class Task(object):
    rule = Rules()
    x = Point(-1, -1)

    def get_input(self) -> None:
        choice = input("Read from file - 0\nWrite by keyboard - 1\nYour choice: ")

        if int(choice) == 0:
            with open("file_with_numbers.txt", "r") as f:
                arr = [2, 1, 3, 4]
                for itr in range(4):
                    arr[itr] = f.readline()
                    arr[itr] = arr[itr].split()
                    arr[itr] = [int(jtr) for jtr in arr[itr]]
                self.rule = Rules(arr[0], arr[1], arr[2], arr[3])
                arr = f.readline().split()
                self.x = Point(float(arr[0]), float(arr[1]))
                print(arr)
        else:
            self.rule.set_rules()
            self.x.set_point()
        print(self.rule.rules)

    def run(self) -> None:
        choice = int(input("Do by Mamdani - 0\nDo by Larsen - 1\nYour choise: "))
        buffer_rule = self.rule.rules
        a11 = [1, 0, 1 - self.x.x1]
        a21 = [1, 0, 1 - self.x.x2]
        a12 = [0, 1, self.x.x1]
        a22 = [0, 1, self.x.x2]
        alpha_list = []
        arra = []
        b1 = []
        b2 = []
        b = []
        y = []

        step: float = 0
        print("input step for diapazon from 0 to 1! ")
        while (step < 0) or (step > 1):
            step = get_input("step")

        itr = 0
        jtr: int = 0
        while itr <= 1:
            y.append(round(itr, 5))
            b1.append(round(1 - y[jtr], 5))
            b2.append(round(y[jtr], 5))
            itr += step
            jtr += 1
        print(b1, b2)

        print(buffer_rule)
        for itr in range(4):
            buff_a1 = a11[2] if buffer_rule[itr][0] == 0 else a12[2]
            buff_a2 = a21[2] if buffer_rule[itr][1] == 0 else a22[2]
            if choice == 0:
                alpha_list.append(round(min(buff_a1, buff_a2), 5))
            else:
                alpha_list.append(round(buff_a1 * buff_a2, 5))
        print(alpha_list)

        for itr in range(4):
            b[itr] = b1.copy() if buffer_rule[itr][2] == 0 else b2.copy()
            for jtr, _ in enumerate(b[itr]):
                b[itr][jtr] = min(b[itr][jtr], alpha_list[itr])
        print(b)

        b_last = [-1 for _ in range(len(b[0]))]
        for itr, _ in enumerate(b[0]):
            b_last[itr] = max(b_last[itr], b[0][itr])
            b_last[itr] = max(b_last[itr], b[1][itr])
            b_last[itr] = max(b_last[itr], b[2][itr])
            b_last[itr] = max(b_last[itr], b[3][itr])
        y = np.array(y)
        b_last = np.array(b_last)
        print(y, b_last)

        for method in METHODS:
            defff = fuzz.defuzz(y, b_last, method)
            arra.append(defff)
            print(defff)

        answer: str = f"""Rules:
        p = [{buffer_rule[0][0]}, {buffer_rule[0][1]}] -> {buffer_rule[0][2]}
        p = [{buffer_rule[1][0]}, {buffer_rule[1][1]}] -> {buffer_rule[1][2]}
        p = [{buffer_rule[2][0]}, {buffer_rule[2][1]}] -> {buffer_rule[2][2]}
        p = [{buffer_rule[3][0]}, {buffer_rule[3][1]}] -> {buffer_rule[3][2]}
        Point    : x = [{self.x.x1}, {self.x.x2}]
        B1       : {b1}
        B2       : {b2}
        Alpha    : {alpha_list}
        B1*      : {b[0]}
        B2*      : {b[1]}
        B3*      : {b[2]}
        B4*      : {b[3]}
        y        : {y}
        nB       : {b_last}
        Centroid : {arra[0]}
        Bisector : {arra[1]}
        Mom      : {arra[2]}
        Som      : {arra[3]}
        Lom      : {arra[4]}
        """

        with open("answer.txt", "w+") as f:
            f.write(answer)


def main() -> None:
    task = Task()
    task.get_input()
    task.run()


if __name__ == "__main__":
    main()
