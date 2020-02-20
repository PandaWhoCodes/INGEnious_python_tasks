#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import random

import CorrArea as corr
import area


class TestSum(unittest.TestCase):
    def test_sum(self):
        lists = [[random.randint(1, 100) for _ in range((2))] for _ in range(random.randint(1, 20))]
        ans = _("The sum of {} is {} and you returned {}.")

        for list in lists:
            stu_ans = area.area(list[0], list[1])
            corr_ans = corr.area(list[0], list[1])
            self.assertEqual(corr_ans, stu_ans, ans.format(list, corr_ans, stu_ans))


if __name__ == '__main__':
    unittest.main()