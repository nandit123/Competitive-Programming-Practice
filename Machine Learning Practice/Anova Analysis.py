import scipy.stats as stats
treatment1 = [
    60,
    67,
    42,
    67,
    56,
    62,
    64,
    59,
    72,
    71
]
treatment2 =[
    50,
    52,
    43,
    67,
    67,
    59,
    67,
    64,
    63,
    65
]
treatment3 = [
    48,
    49,
    50,
    55,
    56,
    61,
    61,
    60,
    59,
    64
]
treatment4 = [
    47,
    67,
    54,
    67,
    68,
    65,
    65,
    56,
    60,
    65
]

oneWay = stats.f_oneway(treatment1,treatment2,treatment3,treatment4)
print(oneWay)