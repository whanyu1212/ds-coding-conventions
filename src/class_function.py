from datetime import datetime, timedelta
from typing import List

import numpy as np
import pandas as pd


class SyntheticDataGenerator:
    """
    A class used to generate synthetic data of various types.

    Attributes
    ----------
    num_rows : int
        number of rows to generate for each column
    data : pd.DataFrame
        DataFrame to store the generated data

    Methods
    -------
    add_integer(column_name, low=0, high=100):
        Adds a column of random integers to the data.
    add_float(column_name, low=0.0, high=1.0):
        Adds a column of random floats to the data.
    add_categorical(column_name, categories):
        Adds a column of random categories to the data.
    add_datetime(column_name, start_date=datetime(2020, 1, 1)):
        Adds a column of random datetime values to the data.
    add_boolean(column_name):
        Adds a column of random booleans to the data.
    get_data():
        Returns the DataFrame with the generated data.
    """

    def __init__(self, num_rows: int = 100) -> None:
        """Initializes the SyntheticDataGenerator with the specified
        number of rows."""
        self.num_rows = num_rows
        self.data = pd.DataFrame()

    def add_integer(
        self, column_name: str, low: int = 0, high: int = 100
    ) -> None:
        """Adds a column of random integers within the specified range
        to the data."""
        self.data[column_name] = np.random.randint(low, high, self.num_rows)

    def add_float(
        self, column_name: str, low: float = 0.0, high: float = 1.0
    ) -> None:
        """Adds a column of random floats within the specified range to
        the data."""
        self.data[column_name] = np.random.uniform(low, high, self.num_rows)

    def add_categorical(self, column_name: str, categories: List[str]) -> None:
        """Adds a column of random categories from the specified list to
        the data."""
        self.data[column_name] = pd.Categorical(
            np.random.choice(categories, self.num_rows)
        )

    def add_datetime(
        self, column_name: str, start_date: datetime = datetime(2020, 1, 1)
    ) -> None:
        """Adds a column of random datetime values starting from the
        specified date to the data."""
        date_range = [
            start_date + timedelta(days=i) for i in range(self.num_rows)
        ]
        self.data[column_name] = np.random.choice(date_range, self.num_rows)

    def add_boolean(self, column_name: str) -> None:
        """Adds a column of random booleans to the data."""
        self.data[column_name] = np.random.choice([True, False], self.num_rows)

    def get_data(self) -> pd.DataFrame:
        """Returns the DataFrame with the generated data."""
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
