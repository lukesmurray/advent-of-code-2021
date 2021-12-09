import json
from pprint import pprint

data = [
    [x.strip().split(), y.strip().split()] for x, y in [l.split("|") for l in open("i")]
]


digit_to_segments = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg",
}
segments_to_digits = {v: k for k, v in digit_to_segments.items()}

digit_to_length = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
length_to_digits = {
    6: [0, 6, 9],
    2: [1],
    5: [2, 3, 5],
    4: [4],
    3: [7],
    7: [8],
}


length_to_options = {
    2: "cf",
    3: "acf",
    4: "bcdf",
    5: "abcdefg",
    6: "abcdefg",
    7: "abcdefg",
}


def limit_options(wire_to_options, inputs):
    # if a wire is in an input, the wires options must be limited to options
    # associated with digits with the same length as the input
    for input in inputs:
        for wire in input:
            wire_to_options[wire] = "".join(
                [
                    option
                    for option in wire_to_options[wire]
                    if option in length_to_options[len(input)]
                ]
            )

    for input in inputs:
        # the set of valid digits
        valid_digits = length_to_digits[len(input)]
        used_options = [
            option for wire, option in wire_to_options.items() if wire in input
        ]
        # if two wires in the input have the same two options, that segment must
        # be used. If any wire has one option, that segment must be used.
        assigned_segments = "".join(
            set(
                "".join(
                    [
                        s
                        for s in used_options
                        if (len(s) == 2 and used_options.count(s) == 2) or len(s) == 1
                    ]
                )
            )
        )
        # digits are only valid if all of the assigned segments are in the digit
        valid_digits = [
            d
            for d in valid_digits
            if all(s in digit_to_segments[d] for s in assigned_segments)
        ]
        valid_segments = "".join(
            set("".join([digit_to_segments[d] for d in valid_digits]))
        )
        for wire in input:
            wire_to_options[wire] = "".join(
                [option for option in wire_to_options[wire] if option in valid_segments]
            )

    all_options = list(wire_to_options.values())
    # if two wires have the same two options, those options cannot be assigned
    # to any other wires
    # if one wire has one option, that option cannot be assigned to any other
    # wire
    assigned_os = [
        o
        for o in all_options
        if (len(o) == 2 and all_options.count(o) == 2) or len(o) == 1
    ]

    for assigned_o in assigned_os:
        assigned_w = [
            wire for wire, option in wire_to_options.items() if option == assigned_o
        ]
        for wire, options in wire_to_options.items():
            if wire in assigned_w:
                continue
            else:
                wire_to_options[wire] = "".join(
                    [o for o in options if o not in assigned_o]
                )


number_outputs = []
for (
    inputs,
    outputs,
) in data:
    wire_to_options = {
        "a": "abcdefg",
        "b": "abcdefg",
        "c": "abcdefg",
        "d": "abcdefg",
        "e": "abcdefg",
        "f": "abcdefg",
        "g": "abcdefg",
    }

    # pprint(wire_to_options, indent=2, width=40)
    prev = json.dumps(wire_to_options)
    while True:

        limit_options(wire_to_options, inputs)
        next = json.dumps(wire_to_options)
        if prev == next:
            break
        prev = next

    real_output = int(
        "".join(
            [
                str(
                    segments_to_digits[
                        "".join(sorted([wire_to_options[wire] for wire in output]))
                    ]
                )
                for output in outputs
            ]
        )
    )
    number_outputs.append(real_output)

print(sum(number_outputs))
