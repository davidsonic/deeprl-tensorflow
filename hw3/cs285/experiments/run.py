import shlex, subprocess
import numpy as np
import sys
import os
import argparse
import glob
import json
import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict


parser = argparse.ArgumentParser()
parser.add_argument('exp')
args = parser.parse_args()


def run_dqn_pong():
    cmd = 'python cs285/scripts/run_hw3_dqn.py --env_name PongNoFrameskip-v4 --exp_name test_pong'
    os.system(cmd)


def run_ddqn_pong():
    cmd = 'python cs285/scripts/run_hw3_dqn.py --env_name PongNoFrameskip-v4 --exp_name test_pong --double_q'
    os.system(cmd)


def run_dqn_lander():
    cmd = 'python cs285/scripts/run_hw3_dqn.py --env_name LunarLander-v2 --exp_name test_lander --seed 1'
    os.system(cmd)


def run_ddqn_lander():
    cmd = 'python cs285/scripts/run_hw3_dqn.py --env_name LunarLander-v2 --exp_name test_lander --seed 1 --double_q'
    os.system(cmd)


def run_actor_critic():
    cmd = 'python cs285/scripts/run_hw3_actor_critic.py --env_name CartPole-v0 -n 100 -b 1000 --exp_name 100_1 -ntu 100 -ngsptu 1'
    os.system(cmd)


exp = {
    'run-dqn-pong': run_dqn_pong,
    'run-dqn-lander': run_dqn_lander,
    'run-ddqn-pong': run_ddqn_pong,
    'run-ddqn-lander': run_ddqn_lander,
    'run-actor-critic':run_actor_critic,
}

assert args.exp in exp
exp[args.exp]()