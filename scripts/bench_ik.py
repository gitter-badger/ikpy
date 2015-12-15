import poppy_inverse_kinematics.creature as model_creature
import numpy as np
import cProfile
import pstats
import timeit

# Parameters
# Target
target = [1, 1, 1]
# Profile if True
profile = True
# Count elapsed time if True
bench = True

nb_iterations = 100


def setup():
    robot = model_creature.creature("torso_right_arm")
    robot.target = target
    return robot


def bench_ik(robot):
    return timeit.timeit(lambda: robot.inverse_kinematic(), number=nb_iterations)


def profile_ik(robot):
    cProfile.run("robot.inverse_kinematic()", "output/stats")
    p = pstats.Stats('output/stats')
    p.strip_dirs().sort_stats("cumulative").print_stats()


if __name__ == "__main__":
    # profile_robot()
    robot = setup()
    if bench:
        print("Done %s iterations, in %s seconds" % (nb_iterations, bench_ik(robot)))
    if profile:
        profile_ik(robot)