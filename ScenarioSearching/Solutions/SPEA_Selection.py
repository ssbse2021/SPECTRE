# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/9 22:00
# @Author  : Chengjie
# @File    : SPEA_Selection.py


from jmetal.operator import IntegerSBXCrossover, IntegerPolynomialMutation
from ScenarioSearching.Problems.problem import ScenarioSelection
from jmetal.util.solution import get_non_dominated_solutions
import time
from multiprocessing import Process
import os
import pandas as pd
from jmetal.algorithm.multiobjective.spea2 import SPEA2
from jmetal.util.solution import read_solutions, print_function_values_to_file, print_variables_to_file
from jmetal.util.termination_criterion import StoppingByEvaluations


def SPEA2_Selection(store_dir, run_time, select_number, store_: bool = True):
    problem_type = 'SPEA_2'
    # select = 500
    problem = ScenarioSelection(store_dir, store_, problem_type, run_time, select_number)
    print(problem.path)
    algorithm = SPEA2(
        problem=problem,
        population_size=100,
        offspring_population_size=100,
        mutation=IntegerPolynomialMutation(probability=1.0 / problem.number_of_variables, distribution_index=20),
        crossover=IntegerSBXCrossover(probability=0.9, distribution_index=20),
        termination_criterion=StoppingByEvaluations(max_evaluations=30000)
    )

    # start = time.time()
    algorithm.run()

    # pd.DataFrame([[round(algorithm.total_computing_time, 3), round(algorithm.total_computing_time * 30, 3), round(algorithm.total_computing_time * 30 / 3600, 3)]]).\
    #     to_csv(problem.path + problem_type + '_Running_Time_' + str(select_number) + '.csv', mode='a', header=False, index=False)

    front = get_non_dominated_solutions(algorithm.get_result())

    if store_:
        # print(front[0].objectives)
        for fr in front:
            fr.objectives = [-i for i in fr.objectives]
        # save to files
        print_function_values_to_file(front,
                                      problem.path + problem_type + '_Final_Fun_Result_' + str(
                                          select_number) + '_' + str(run_time))
        print_variables_to_file(front,
                                problem.path + problem_type + '_VAR.NSGAII.ScenarioSelection' + str(
                                    select_number) + '_' + str(run_time))

        # plot figure
        # plot_front = Plot(title='Pareto front approximation', axis_labels=['x', 'y', 'z', 'w', 'm'])
        # plot_front.plot(front, label='NSGAII-ScenarioSelection' + str(select_number) + '_' + str(run_time),
        #                 filename=problem.path + 'NSGAII-ScenarioSelection_' + str(
        #                     select_number) + '_' + str(run_time), format='png')


if __name__ == '__main__':
    # path = os.path.dirname(os.path.realpath(__file__))
    # SPEA2_Selection(path, 1, 1000, False)
    path = os.path.dirname(os.path.realpath(__file__))
    store = True
    # p1 = Process(target=SPEA2_Selection, args=(1, 2000))
    # p2 = Process(target=SPEA2_Selection, args=(1, 3000))
    # p1.start()
    # p2.start()
    #
    # aaa

    """
    Select 5000 scenarios
    """
    select_ = 5000
    # 0 ~ 9
    process_list = []
    n = 10
    s = time.time()
    for i in range(n):
        # print(i)
        p = Process(target=SPEA2_Selection, args=(path, i + 1, select_, store, ))
        p.start()
        process_list.append(p)

    for process in process_list:
        process.join()

    # e = time.time()
    # print((e - s) * 250 / 3600)

    # 10 ~ 19
    process_list = []
    n = 10
    for i in range(n):
        # print(i)
        p = Process(target=SPEA2_Selection, args=(path, i + 11, select_, store, ))
        p.start()
        process_list.append(p)

    # print(len(process_list))
    for process in process_list:
        process.join()

    # 20 ~ 29
    process_list = []
    n = 10
    for i in range(n):
        # print(i)
        p = Process(target=SPEA2_Selection, args=(path, i + 21, select_, store, ))
        p.start()
        process_list.append(p)

    # print(len(process_list))
    for process in process_list:
        process.join()

    e = time.time()
    print(e - s)
    print('Select ' + str(select_) + 'scenarios finished, total time: ', (e - s) / 3600)

    """
    Select 4000 scenarios
    """
    select_ = 4000
    # 0 ~ 9
    process_list = []
    n = 10
    s = time.time()
    for i in range(n):
        # print(i)
        p = Process(target=SPEA2_Selection, args=(path, i + 1, select_, store, ))
        p.start()
        process_list.append(p)

    for process in process_list:
        process.join()

    # 10 ~ 19
    process_list = []
    n = 10
    for i in range(n):
        # print(i)
        p = Process(target=SPEA2_Selection, args=(path, i + 11, select_, store, ))
        p.start()
        process_list.append(p)

    # print(len(process_list))
    for process in process_list:
        process.join()

    # 20 ~ 29
    process_list = []
    n = 10
    for i in range(n):
        # print(i)
        p = Process(target=SPEA2_Selection, args=(path, i + 21, select_, store,))
        p.start()
        process_list.append(p)

    # print(len(process_list))
    for process in process_list:
        process.join()

    e = time.time()
    print(e - s)
    print('Select ' + str(select_) + 'scenarios finished, total time: ', (e - s) / 3600)

    """
    Select 3000 scenarios
    """
    select_ = 3000
    # 0 ~ 9
    process_list = []
    n = 10
    s = time.time()
    for i in range(n):
        # print(i)
        p = Process(target=SPEA2_Selection, args=(path, i + 1, select_, store,))
        p.start()
        process_list.append(p)

    for process in process_list:
        process.join()

    # 10 ~ 19
    process_list = []
    n = 10
    for i in range(n):
        # print(i)
        p = Process(target=SPEA2_Selection, args=(path, i + 11, select_, store,))
        p.start()
        process_list.append(p)

    # print(len(process_list))
    for process in process_list:
        process.join()

    # 20 ~ 29
    process_list = []
    n = 10
    for i in range(n):
        # print(i)
        p = Process(target=SPEA2_Selection, args=(path, i + 21, select_, store,))
        p.start()
        process_list.append(p)

    # print(len(process_list))
    for process in process_list:
        process.join()

    e = time.time()
    print(e - s)
    print('Select ' + str(select_) + 'scenarios finished, total time: ', (e - s) / 3600)

    """
    Select 2000 scenarios
    """
    select_ = 2000
    # 0 ~ 9
    process_list = []
    n = 10
    s = time.time()
    for i in range(n):
        # print(i)
        p = Process(target=SPEA2_Selection, args=(path, i + 1, select_, store,))
        p.start()
        process_list.append(p)

    for process in process_list:
        process.join()

    # 10 ~ 19
    process_list = []
    n = 10
    for i in range(n):
        # print(i)
        p = Process(target=SPEA2_Selection, args=(path, i + 11, select_, store,))
        p.start()
        process_list.append(p)

    # print(len(process_list))
    for process in process_list:
        process.join()

    # 20 ~ 29
    process_list = []
    n = 10
    for i in range(n):
        # print(i)
        p = Process(target=SPEA2_Selection, args=(path, i + 21, select_, store,))
        p.start()
        process_list.append(p)

    # print(len(process_list))
    for process in process_list:
        process.join()

    e = time.time()
    print(e - s)
    print('Select ' + str(select_) + 'scenarios finished, total time: ', (e - s) / 3600)

    """
    Select 1000 scenarios
    """
    select_ = 1000
    # 0 ~ 9
    process_list = []
    n = 10
    s = time.time()
    for i in range(n):
        # print(i)
        p = Process(target=SPEA2_Selection, args=(path, i + 1, select_, store,))
        p.start()
        process_list.append(p)

    for process in process_list:
        process.join()

    # 10 ~ 19
    process_list = []
    n = 10
    for i in range(n):
        # print(i)
        p = Process(target=SPEA2_Selection, args=(path, i + 11, select_, store,))
        p.start()
        process_list.append(p)

    # print(len(process_list))
    for process in process_list:
        process.join()

    # 20 ~ 29
    process_list = []
    n = 10
    for i in range(n):
        # print(i)
        p = Process(target=SPEA2_Selection, args=(path, i + 21, select_, store,))
        p.start()
        process_list.append(p)

    # print(len(process_list))
    for process in process_list:
        process.join()

    e = time.time()
    print(e - s)
    print('Select ' + str(select_) + 'scenarios finished, total time: ', (e - s) / 3600)

