from public.i18n import translations

SECONDS_IN_DAY = 86400

BMI_UNDERWEIGHT = 18.5
BMI_NORMAL = 25
BMI_OVERWEIGHT = 30
BMI_OBESITY_ONE = 35
BMI_OBESITY_TWO = 40

BMR_MALE = 88.362
BMR_MALE_WEIGHT = 13.397
BMR_MALE_HEIGHT = 4.799
BMR_MALE_AGE = 5.677

BMR_FEMALE = 447.593
BMR_FEMALE_WEIGHT = 9.247
BMR_FEMALE_HEIGHT = 3.097
BMR_FEMALE_AGE = 4.33

PROTEIN_LOSE = 0.1
FAT_LOSE = 0.25
CARBOHYDRATE_LOSE = 0.6

PROTEIN_KEEP = 0.15
FAT_KEEP = 0.25
CARBOHYDRATE_KEEP = 0.7

PROTEIN_GAIN = 0.15
FAT_GAIN = 0.3
CARBOHYDRATE_GAIN = 0.75

CALORIE = 4.1868
CALORIE_PROTEIN = 17.2
CALORIE_FAT = 38.9
CALORIE_CARBOHYDRATE = 17.2

sexes = [
    {"type": translations.sex_male},
    {"type": translations.sex_female},
]

activities = [
    {"type": translations.activity_low, "value": 1.2},
    {"type": translations.activity_normal, "value": 1.375},
    {"type": translations.activity_average, "value": 1.55},
    {"type": translations.activity_high, "value": 1.725},
    {"type": translations.activity_abnormal, "value": 1.9},
]

goals = [
    {"type": translations.goal_lose, "value": 0.85},
    {"type": translations.goal_keep, "value": 1},
    {"type": translations.goal_gain, "value": 1.15},
]

categories = [
    {"type": translations.category_underweight},
    {"type": translations.category_normal},
    {"type": translations.category_overweight},
    {"type": translations.category_obesity_one},
    {"type": translations.category_obesity_two},
    {"type": translations.category_obesity_three},
]
