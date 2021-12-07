# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/1 21:47
# @Author  : Chengjie
# @File    : NSGA_2_Selection.py

from jmetal.algorithm.multiobjective import NSGAII
from jmetal.operator import IntegerSBXCrossover, IntegerPolynomialMutation
from ScenarioSearching.Problems.problem import ScenarioSelection

from jmetal.util.termination_criterion import StoppingByEvaluations
from jmetal.lab.visualization import Plot
from jmetal.util.solution import get_non_dominated_solutions, print_function_values_to_file, \
    print_variables_to_file
import time
from multiprocessing import Process
import os
import pandas as pd


def NSGA_Selection(store_dir, run_time, select_number, store_: bool = True):
    problem_type = 'NSGA_2'
    # select = 500
    problem = ScenarioSelection(store_dir, store_, problem_type, run_time, select_number)
    print(problem.path)
    # open('./ExperimentData/' + problem_type + '/' + problem_type + '_Selected_Variables_' + str(run_time), 'w', encoding='utf-8')

    algorithm = NSGAII(
        problem=problem,
        population_size=100,
        offspring_population_size=100,
        mutation=IntegerPolynomialMutation(probability=1 / problem.number_of_variables, distribution_index=20),
        crossover=IntegerSBXCrossover(0.9, 20),
        termination_criterion=StoppingByEvaluations(max_evaluations=30000)
    )

    # start = time.time()
    algorithm.run()
    # pd.DataFrame([[round(algorithm.total_computing_time, 3), round(algorithm.total_computing_time * 30, 3), round(algorithm.total_computing_time * 30 / 3600, 3)]]).\
    #     to_csv(problem.path + problem_type + '_Running_Time_' + str(select_number) + '.csv', mode='a', header=False, index=False)

    front = get_non_dominated_solutions(algorithm.get_result())

    # print(front[0].objectives)
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

    # end = time.time()
    #
    # print('NSGA_Selection ' + str(select_number) + '_' + str(run_time) + ' running time: ', end - start)


if __name__ == '__main__':
    path = os.path.dirname(os.path.realpath(__file__))
    store = False
    # p1 = Process(target=NSGA_Selection, args=(1, 2000))
    # p2 = Process(target=NSGA_Selection, args=(1, 3000))
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
        p = Process(target=NSGA_Selection, args=(path, i + 1, select_, store, ))
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
        p = Process(target=NSGA_Selection, args=(path, i + 11, select_, store, ))
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
        p = Process(target=NSGA_Selection, args=(path, i + 21, select_, store, ))
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
        p = Process(target=NSGA_Selection, args=(path, i + 1, select_, store, ))
        p.start()
        process_list.append(p)

    for process in process_list:
        process.join()

    # 10 ~ 19
    process_list = []
    n = 10
    for i in range(n):
        # print(i)
        p = Process(target=NSGA_Selection, args=(path, i + 11, select_, store, ))
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
        p = Process(target=NSGA_Selection, args=(path, i + 21, select_, store,))
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
        p = Process(target=NSGA_Selection, args=(path, i + 1, select_, store,))
        p.start()
        process_list.append(p)

    for process in process_list:
        process.join()

    # 10 ~ 19
    process_list = []
    n = 10
    for i in range(n):
        # print(i)
        p = Process(target=NSGA_Selection, args=(path, i + 11, select_, store,))
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
        p = Process(target=NSGA_Selection, args=(path, i + 21, select_, store,))
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
        p = Process(target=NSGA_Selection, args=(path, i + 1, select_, store,))
        p.start()
        process_list.append(p)

    for process in process_list:
        process.join()

    # 10 ~ 19
    process_list = []
    n = 10
    for i in range(n):
        # print(i)
        p = Process(target=NSGA_Selection, args=(path, i + 11, select_, store,))
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
        p = Process(target=NSGA_Selection, args=(path, i + 21, select_, store,))
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
        p = Process(target=NSGA_Selection, args=(path, i + 1, select_, store,))
        p.start()
        process_list.append(p)

    for process in process_list:
        process.join()

    # 10 ~ 19
    process_list = []
    n = 10
    for i in range(n):
        # print(i)
        p = Process(target=NSGA_Selection, args=(path, i + 11, select_, store,))
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
        p = Process(target=NSGA_Selection, args=(path, i + 21, select_, store,))
        p.start()
        process_list.append(p)

    # print(len(process_list))
    for process in process_list:
        process.join()

    e = time.time()
    print(e - s)
    print('Select ' + str(select_) + 'scenarios finished, total time: ', (e - s) / 3600)

