import time
import day1,day2,day3,day4,day5,day6,day7,day8,day9,day10,day11,day12,day13,day14,day15#,day16,day17,day18,day19,day20,day21,day22,day23,day24,day25
modules = [day1,day2,day3,day4,day5,day6,day7,day8,day10,day11,day13,day14,day15]#,day16,day17,day18,day19,day20,day21,day22,day23,day24,day25]

if __name__ == '__main__':
    for day in modules:
        start_one = time.time()
        problem_one = day.solve1()
        end_one = time.time()
        start_two = time.time()
        problem_two = day.solve2()
        end_two = time.time()
        print("%s-1:\t%s\t%.2gs" %(day.name(), problem_one, (end_one-start_one)))
        print("%s-2:\t%s\t%.2gs" %(day.name(), problem_two, (end_two - start_two)))


