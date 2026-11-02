"""Check the CMG CSV export using the original Assignment 16 pressure criteria."""
import csv
import math
from pathlib import Path
import unittest


EXPECTED_PRESSURES = (1000.0, 1191.98, 1340.26, 1440.37)


def get_cmg_pressures(path="assignment16.csv"):
    """Read the last CSV column after CMG's two introductory rows and header."""
    path = Path(path)
    if not path.is_file():
        raise AssertionError("Missing assignment16.csv: export the pressure history from CMG Results")
    with path.open(encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.reader(stream))
    if len(rows) < 3 or not rows[2]:
        raise AssertionError("Missing CSV header after the two CMG introductory rows")
    data = [row for row in rows[3:] if any(field.strip() for field in row)]
    if len(data) != 4:
        raise AssertionError("Expected four pressure rows: initial state and days 1, 2, and 3")
    pressures = []
    for row in data:
        if len(row) != len(rows[2]):
            raise AssertionError("CSV data columns do not match the header")
        try:
            pressure = float(row[-1])
        except ValueError as error:
            raise AssertionError("The last CSV column must contain numeric pressures in psi") from error
        if not math.isfinite(pressure):
            raise AssertionError("Pressures must be finite")
        pressures.append(pressure)
    return pressures


def check_pressures(pressures):
    if len(pressures) != len(EXPECTED_PRESSURES):
        raise AssertionError("Expected four pressure values")
    # Preserve numpy.testing.assert_allclose's original atol=5 and rtol=1e-7.
    for actual, expected in zip(pressures, EXPECTED_PRESSURES):
        if not math.isfinite(actual) or abs(actual - expected) > 5 + 1e-7 * abs(expected):
            raise AssertionError("Exported pressures are outside the 5 psi tolerance")


class TestSolution(unittest.TestCase):
    def test_output_pressures(self):
        check_pressures(get_cmg_pressures())


if __name__ == "__main__":
    unittest.main()
