from src.lib import Alternative, Criterion, to_frame

CRITERIA: list[Criterion] = [
    Criterion(
        name="C1",
        description="Age",
        weight=1,
        rules={
            1: lambda x: x >= 36,
            2: lambda x: 31 <= x <= 35,
            3: lambda x: 27 <= x <= 30,
            4: lambda x: 24 <= x <= 26,
            5: lambda x: x <= 23,
        },
    ),
    Criterion(
        name="C2",
        description="Education",
        weight=1,
        rules={
            1: lambda x: x == "None",
            2: lambda x: x == "Secondary School",
            3: lambda x: x == "Associate Degree",
            4: lambda x: x == "Bachelor Degree",
            5: lambda x: x == "Graduate",
        },
    ),
    Criterion(
        name="C3",
        description="Experience",
        weight=3,
        rules={
            1: lambda x: x == 0,
            2: lambda x: x <= 1,
            3: lambda x: 1 <= x <= 2,
            4: lambda x: 3 <= x <= 4,
            5: lambda x: x >= 4,
        },
    ),
    Criterion(
        name="C4",
        description="Expertise",
        weight=2,
        rules={
            1: lambda x: x <= 60,
            2: lambda x: 61 <= x <= 70,
            3: lambda x: 71 <= x <= 80,
            4: lambda x: 81 <= x <= 90,
            5: lambda x: x >= 90,
        },
    ),
    Criterion(
        name="C5",
        description="Cooperation",
        weight=3,
        rules={
            1: lambda x: x <= 60,
            2: lambda x: 61 <= x <= 70,
            3: lambda x: 71 <= x <= 80,
            4: lambda x: 81 <= x <= 90,
            5: lambda x: x >= 90,
        },
    ),
]

ALTERNATIVES: list[Alternative] = [
    Alternative(
        name="A1",
        description="Mary",
        values={
            "Age": 37,
            "Education": "Bachelor Degree",
            "Experience": 1,
            "Expertise": 81,
            "Cooperation": 71,
        },
    ),
    Alternative(
        name="A2",
        description="Peter",
        values={
            "Age": 31,
            "Education": "Bachelor Degree",
            "Experience": 5,
            "Expertise": 71,
            "Cooperation": 81,
        },
    ),
    Alternative(
        name="A3",
        description="Susan",
        values={
            "Age": 27,
            "Education": "Associate Degree",
            "Experience": 1,
            "Expertise": 71,
            "Cooperation": 81,
        },
    ),
    Alternative(
        name="A4",
        description="Paul",
        values={
            "Age": 27,
            "Education": "Bachelor Degree",
            "Experience": 1,
            "Expertise": 60,
            "Cooperation": 71,
        },
    ),
    Alternative(
        name="A5",
        description="Lisa",
        values={
            "Age": 37,
            "Education": "Bachelor Degree",
            "Experience": 1,
            "Expertise": 60,
            "Cooperation": 71,
        },
    ),
]

df, weights = to_frame(CRITERIA, ALTERNATIVES)
