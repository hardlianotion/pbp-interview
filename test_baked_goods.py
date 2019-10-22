import unittest
from baked_goods import calculate_purchasing_plan


class TestPlan(unittest.TestCase):

    # def impl(total_days, sellers, output):

    def test_initial_inventory_of_10_loaves(self):
        total_days = 30
        # initial inventory should not last until first seller arrival
        sellers = [(12, 200), (15, 30)]

        self.assertEqual(calculate_purchasing_plan(total_days, sellers), None)

    def test_bread_goes_stale_after_30_days(self):
        total_days = 60
        # some loaves bought would go stale between 9 and 42 days.
        sellers = [(9, 200), (42, 150)]

        self.assertEqual(calculate_purchasing_plan(total_days, sellers), None)

    def test_free_if_total_days_less_than_10(self):
        total_days = 9
        sellers = [(12, 200), (15, 30)]

        self.assertEqual(calculate_purchasing_plan(total_days, sellers), [0, 0])

    def test_replicate_documented_example(self):
        total_days = 60
        sellers = [(10, 200), (15, 100), (35, 500), (50, 30)]
        plan = [5, 30, 5, 10]

        self.assertEqual(calculate_purchasing_plan(total_days, sellers), plan)


if __name__ == "__main__":
    unittest.main()