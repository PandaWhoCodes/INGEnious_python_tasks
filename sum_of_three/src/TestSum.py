#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import random

import CorrSum as corr
import sum


class TestSum(unittest.TestCase):
    def test_sum(self):
        lists = [[random.randint(1, 100) for _ in range((3))] for _ in range(random.randint(1, 20))]
        ans = _("The sum of {} is {} and you returned {}.")

        for list in lists:
            stu_ans = sum.sum(list[0], list[1], list[2])
            corr_ans = corr.sum(list[0], list[1], list[2])
            self.assertEqual(corr_ans, stu_ans, ans.format(list, corr_ans, stu_ans))


if __name__ == '__main__':
    unittest.main()
