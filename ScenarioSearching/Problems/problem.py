# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/26 14:41
# @Author  : Chengjie
# @File    : problem.py

from jmetal.core.problem import IntegerProblem
from jmetal.core.solution import IntegerSolution
import pandas as pd
# from ScenarioSearching.binary_problem import scenarios, eval_diversity, eval_collision_demand_
import numpy as np
import json
import os

"""
potential: 30290
collision: 2506
high demand: 44400
high demand & potential: 17292
total scenarios: ≈ 80K  (93706)
unique scenario: 57371
"""

# scenarios = pd.read_csv(filepath_or_buffer='../Diversity/Diversity_Final.csv', sep=',')
scenarios = pd.read_csv(
    filepath_or_buffer='D:/RTCM COPY/SSBSE/SearchProject/ScenarioSearching/Diversity/New_Scenarios.csv', sep=',')


# path = os.path.dirname(os.path.realpath(__file__))
# print(path)


def nor(value, minimum, maximum):
    return (value - minimum) / (maximum - minimum)


def eval_all(solution):
    """
    total_collision: total number of collided scenarios (max)
    total_demand: total number of high demand scenarios (max)
    total_potential: total number of potential collided scenarios (max)
    total_scenario: total number of selected scenarios (min)
    diversity: diversity (max)
    :param solution: solution
    :return: evaluation fitness
    """
    collision_number = 0
    high_demand_number = 0
    potential_number = 0

    total_collision = 0
    total_demand = 0
    total_potential = 0
    total_diversity = 0

    weighted_collision = 0
    weighted_demand = 0
    weighted_potential = 0
    weighted_diversity = 0

    # index = [i for i, x in enumerate(solution.variables) if x == True]  # fetch the selected scenarios ID
    index = solution.variables
    length = len(index)
    collision_pro = scenarios['Collision_Probability']
    demand = scenarios['Demand']
    diversity = scenarios['Diversity_']
    ID = 0
    for i in index:
        cp_variable = collision_pro[i]
        weight = (length - ID + 1) / length
        ID += 1
        if cp_variable > 0.89:
            collision_number += 1
            total_collision += 1

        if demand[i] >= 6:
            high_demand_number += 1
            total_demand += demand[i]

        if 0.9 >= cp_variable > 0.3:
            potential_number += 1
            total_potential += cp_variable

        weighted_demand += weight * demand[i]
        weighted_collision += weight * (1 if cp_variable > 0.89 else 0)
        weighted_potential += weight * cp_variable
        weighted_diversity += weight * diversity[i]

        total_diversity += diversity[i]

    # total_collision = 1
    # total_demand = 1
    # total_potential = 1
    # total_diversity = 1

    avg_weight = (
                             weighted_collision / length + weighted_demand / length + weighted_potential / length + weighted_diversity / length) / 4
    # print(avg_weight)
    evaluation = [collision_number, potential_number, high_demand_number, round(total_diversity / length, 3),
                  round(avg_weight, 3)]

    evaluation_nor = [nor(collision_number, 0, length), nor(potential_number, 0, length), nor(high_demand_number, 0, length), round(total_diversity / length, 3),
                      round(avg_weight, 3)]
    return evaluation


class ScenarioSelection(IntegerProblem):

    def __init__(self, store_dir, store, problem_type, run_time, number_of_variables: int = 1000):
        super(ScenarioSelection, self).__init__()
        self.number_of_variables = number_of_variables
        self.number_of_objectives = 5
        self.number_of_constraints = 0
        self.run_time = run_time
        self.problem_type = problem_type
        self.evaluate_number = 0
        self.store = store

        self.path = store_dir.replace('\\', '/') + '/ExperimentData/' + self.problem_type + '/'
        try:
            os.makedirs(self.path)
        except Exception as e:
            print(e)

        if self.store:
            # self.path = store_dir.replace('\\', '/') + '/ExperimentData/' + self.problem_type + '/'
            # try:
            #     os.makedirs(self.path)
            # except Exception as e:
            #     print(e)
            f = open(self.path + self.problem_type + '_Middle_Fun_Result_' + str(
                self.number_of_variables) + '_' + str(self.run_time) + '.txt', 'w',
                     encoding='utf-8')

        self.obj_directions = [self.MINIMIZE, self.MINIMIZE, self.MINIMIZE, self.MINIMIZE, self.MINIMIZE]

        self.lower_bound = self.number_of_variables * [0]
        self.upper_bound = self.number_of_variables * [49999]

    def evaluate(self, solution: IntegerSolution) -> IntegerSolution:
        self.evaluate_number += 1
        fitness = eval_all(solution)
        # print(fitness)
        for i in range(len(fitness)):
            solution.objectives[i] = -fitness[i]

        if self.evaluate_number % 100 == 0:
            print(self.problem_type + '_Selection_' + str(self.number_of_variables) + '_' + str(self.run_time) + ' : ',
                  self.evaluate_number, [i * -1 for i in solution.objectives])

        if self.store:
            f = open(self.path + self.problem_type + '_Middle_Fun_Result_' + str(
                self.number_of_variables) + '_' + str(self.run_time) + '.txt', 'a', encoding='utf-8')
            f.writelines(
                str([i * -1 for i in solution.objectives]).replace('[', '').replace(']', '').replace("'", '').replace(
                    ',',
                    '') + '\n')
            f.close()

        return solution

    def get_name(self):
        return 'NSGA_2 Scenario Selection'


if __name__ == '__main__':
    print(scenarios['Demand'])
