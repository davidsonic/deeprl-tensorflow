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


def run_ac_easy():
    cmd = 'python cs285/scripts/run_hw3_actor_critic.py --env_name CartPole-v0 -n 100 -b 1000 --exp_name 100_1 -ntu 10 -ngsptu 10 --video_log_freq 30'
    os.system(cmd)



def run_ac_hard():
    cmd = 'python cs285/scripts/run_hw3_actor_critic.py --env_name InvertedPendulum-v2 --ep_len 1000 --discount 0.95 -n 100 -l 2 -s 64 -b 5000 -lr 0.01 --exp_name IP_5000 -ntu 10 -ngsptu 10 --video_log_freq 10'
    os.system(cmd)


def run_ac_harder():
    cmd = 'python cs285/scripts/run_hw3_actor_critic.py --env_name HalfCheetah-v2 --ep_len 150 --discount 0.90 --scalar_log_freq 1 -n 150 -l 2 -s 32 -b 30000 -eb 1500 -lr 0.02 --exp_name cheetah_30000 -ntu 10 -ngsptu 10 --video_log_freq 10'
    os.system(cmd)

exp = {
    'run-dqn-pong': run_dqn_pong,
    'run-dqn-lander': run_dqn_lander,
    'run-ddqn-pong': run_ddqn_pong,
    'run-ddqn-lander': run_ddqn_lander,
    'run-ac-easy':run_ac_easy,
    'run-ac-hard': run_ac_hard,
    'run-ac-harder': run_ac_harder,
}

assert args.exp in exp
exp[args.exp]()