from dataclasses import dataclass
from datetime import date, datetime
from functools import cached_property

from src.config import consts


@dataclass
class UserStats:
    username: str
    password: str
    firstname: str
    lastname: str
    weight: int
    height: int
    birthday: str
    sex: int
    activity: int

    @cached_property
    def age(self):
        today = date.today()
        birthdate = datetime.strptime(self.birthday, "%Y-%m-%d %H:%M:%S")
        current_year = date(today.year, birthdate.month, birthdate.day)
        return (today.year - birthdate.year) - (1 if today < current_year else 0)

    def __post_init__(self):
        self._get_bmi()
        self._get_bmr()
        self._get_calories()
        self._get_energy()

    def _get_bmi(self):
        bmi = self.weight / self.height**2
        self.bmi = round(bmi * 1e4, 2)  # noqa: WPS432

        if self.bmi < consts.BMI_UNDERWEIGHT:
            self.category = 0
            self.goal = 2

        elif consts.BMI_UNDERWEIGHT <= self.bmi < consts.BMI_NORMAL:
            self.category = 1
            self.goal = 1

        elif consts.BMI_NORMAL <= self.bmi < consts.BMI_OVERWEIGHT:
            self.category = 2
            self.goal = 0

        elif consts.BMI_OVERWEIGHT <= self.bmi < consts.BMI_OBESITY_ONE:
            self.category = 3
            self.goal = 0

        elif consts.BMI_OBESITY_ONE <= self.bmi < consts.BMI_OBESITY_TWO:
            self.category = 4
            self.goal = 0

        else:
            self.category = 5
            self.goal = 0

    def _get_bmr(self):
        match self.sex:
            case 0:
                self.bmr = round(
                    consts.BMR_MALE
                    + (consts.BMR_MALE_WEIGHT * self.weight)
                    + (consts.BMR_MALE_HEIGHT * self.height)
                    + (consts.BMR_MALE_AGE * self.age),
                    2,
                )

            case 1:
                self.bmr = round(
                    consts.BMR_FEMALE
                    + (consts.BMR_FEMALE_WEIGHT * self.weight)
                    + (consts.BMR_FEMALE_HEIGHT * self.height)
                    + (consts.BMR_FEMALE_AGE * self.age),
                    2,
                )

    def _get_calories(self):
        calories = (
            self.bmr
            * consts.activities[self.activity]["value"]
            * consts.goals[self.goal]["value"]
        )

        self.calories = round(calories, 2)

    def _get_energy(self):
        def get_daily(num):
            return round(num * self.calories, 2)

        match self.goal:
            case 0:
                self.protein = get_daily(consts.PROTEIN_LOSE)
                self.fat = get_daily(consts.FAT_LOSE)
                self.carbohydrate = get_daily(consts.CARBOHYDRATE_LOSE)

            case 1:
                self.protein = get_daily(consts.PROTEIN_KEEP)
                self.fat = get_daily(consts.FAT_KEEP)
                self.carbohydrate = get_daily(consts.CARBOHYDRATE_KEEP)

            case 2:
                self.protein = get_daily(consts.PROTEIN_GAIN)
                self.fat = get_daily(consts.FAT_GAIN)
                self.carbohydrate = get_daily(consts.CARBOHYDRATE_GAIN)
