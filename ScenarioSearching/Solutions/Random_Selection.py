# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/29 12:16
# @Author  : Chengjie
# @File    : Random_Selection.py

from jmetal.algorithm.multiobjective.random_search import RandomSearch
from jmetal.util.solution import print_function_values_to_file, print_variables_to_file
from jmetal.util.termination_criterion import StoppingByEvaluations
from ScenarioSearching.Problems.problem import ScenarioSelection
from jmetal.lab.visualization import Plot
from multiprocessing import Process
import time
import os
import pandas as pd


def Random_Selection(store_dir, run_time, select_number, store_: bool = True):
    problem_type = 'Random'
    problem = ScenarioSelection(store_dir, store_, problem_type, run_time, select_number)
    print(problem.path)
    # problem.reference_front = read_solutions(filename='resources/reference_front/ZDT1.pf')

    max_evaluations = 30000
    algorithm = RandomSearch(
        problem=problem,
        termination_criterion=StoppingByEvaluations(max_evaluations=max_evaluations)
    )

    algorithm.run()

    # pd.DataFrame([[round(algorithm.total_computing_time, 3), round(algorithm.total_computing_time * 30, 3),
    #                round(algorithm.total_computing_time * 30 / 3600, 3)]]). \
    #     to_csv(problem.path + problem_type + '_Running_Time_' + str(select_number) + '.csv', mode='a', header=False,
    #            index=False)

    front = algorithm.get_result()

    if store_:
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
        plot_front = Plot(title='Pareto front approximation', axis_labels=['x', 'y', 'z', 'w', 'm'])
        plot_front.plot(front, label='NSGAII-ScenarioSelection' + str(select_number) + '_' + str(run_time),
                        filename=problem.path + 'NSGAII-ScenarioSelection_' + str(
                            select_number) + '_' + str(run_time), format='png')


if __name__ == '__main__':
    path = os.path.dirname(os.path.realpath(__file__))
    store = False
    # p1 = Process(target=Random_Selection, args=(1, 2000))
    # p2 = Process(target=Random_Selection, args=(1, 3000))
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
        p = Process(target=Random_Selection, args=(path, i + 1, select_, store, ))
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
        p = Process(target=Random_Selection, args=(path, i + 11, select_, store, ))
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
        p = Process(target=Random_Selection, args=(path, i + 21, select_, store, ))
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
        p = Process(target=Random_Selection, args=(path, i + 1, select_, store, ))
        p.start()
        process_list.append(p)

    for process in process_list:
        process.join()

    # 10 ~ 19
    process_list = []
    n = 10
    for i in range(n):
        # print(i)
        p = Process(target=Random_Selection, args=(path, i + 11, select_, store, ))
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
        p = Process(target=Random_Selection, args=(path, i + 21, select_, store,))
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
        p = Process(target=Random_Selection, args=(path, i + 1, select_, store,))
        p.start()
        process_list.append(p)

    for process in process_list:
        process.join()

    # 10 ~ 19
    process_list = []
    n = 10
    for i in range(n):
        # print(i)
        p = Process(target=Random_Selection, args=(path, i + 11, select_, store,))
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
        p = Process(target=Random_Selection, args=(path, i + 21, select_, store,))
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
        p = Process(target=Random_Selection, args=(path, i + 1, select_, store,))
        p.start()
        process_list.append(p)

    for process in process_list:
        process.join()

    # 10 ~ 19
    process_list = []
    n = 10
    for i in range(n):
        # print(i)
        p = Process(target=Random_Selection, args=(path, i + 11, select_, store,))
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
        p = Process(target=Random_Selection, args=(path, i + 21, select_, store,))
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
        p = Process(target=Random_Selection, args=(path, i + 1, select_, store,))
        p.start()
        process_list.append(p)

    for process in process_list:
        process.join()

    # 10 ~ 19
    process_list = []
    n = 10
    for i in range(n):
        # print(i)
        p = Process(target=Random_Selection, args=(path, i + 11, select_, store,))
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
        p = Process(target=Random_Selection, args=(path, i + 21, select_, store,))
        p.start()
        process_list.append(p)

    # print(len(process_list))
    for process in process_list:
        process.join()

    e = time.time()
    print(e - s)
    print('Select ' + str(select_) + 'scenarios finished, total time: ', (e - s) / 3600)

