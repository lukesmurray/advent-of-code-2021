print(
    len(
        [
            output
            for _, outputs in [
                [x.strip().split(), y.strip().split()]
                for x, y in [l.split("|") for l in open("i")]
            ]
            for output in outputs
            if len(output) in (2, 3, 4, 7)
        ]
    )
)
