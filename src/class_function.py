from datetime import datetime, timedelta
from typing import List

import numpy as np
import pandas as pd


class SyntheticDataGenerator:
    def __init__(self, num_rows: int = 100) -> None:
        self.num_rows = num_rows
        self.data = pd.DataFrame()

    def add_integer(
        self, column_name: str, low: int = 0, high: int = 100
    ) -> None:
        self.data[column_name] = np.random.randint(low, high, self.num_rows)

    def add_float(
        self, column_name: str, low: float = 0.0, high: float = 1.0
    ) -> None:
        self.data[column_name] = np.random.uniform(low, high, self.num_rows)

    def add_categorical(self, column_name: str, categories: List[str]) -> None:
        self.data[column_name] = pd.Categorical(
            np.random.choice(categories, self.num_rows)
        )

    def add_datetime(
        self, column_name: str, start_date: datetime = datetime(2020, 1, 1)
    ) -> None:
        date_range = [
            start_date + timedelta(days=i) for i in range(self.num_rows)
        ]
        self.data[column_name] = np.random.choice(date_range, self.num_rows)

    def add_boolean(self, column_name: str) -> None:
        self.data[column_name] = np.random.choice([True, False], self.num_rows)

    def get_data(self) -> pd.DataFrame:
        return self.data


if __name__ == "__main__":
    generator = SyntheticDataGenerator()
    generator.add_integer("A")
    generator.add_integer("B")
    generator.add_float("C")
    generator.add_categorical("D", ["cat", "dog", "mouse"])
    generator.add_datetime("E")
    generator.add_boolean("F")
    generator.add_categorical("G", ["red", "blue", "green"])
    df = generator.get_data()
    print(df)
