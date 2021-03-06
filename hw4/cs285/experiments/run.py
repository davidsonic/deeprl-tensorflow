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


def run_p_1_1():
    cmd = 'python cs285/scripts/run_hw4_mb.py --exp_name cheetah_n500_arch1x32 --env_name cheetah-cs285-v0 --add_sl_noise --n_iter 1 --batch_size_initial 20000 --num_agent_train_steps_per_iter 500 --n_layers 1 --size 32 --scalar_log_freq -1 --video_log_freq -1'
    os.system(cmd)


def run_p_1_2():
    cmd = 'python cs285/scripts/run_hw4_mb.py --exp_name cheetah_n5_arch2x250 --env_name cheetah-cs285-v0 --add_sl_noise --n_iter 1 --batch_size_initial 20000 --num_agent_train_steps_per_iter 5 --n_layers 2 --size 250 --scalar_log_freq -1 --video_log_freq -1'
    os.system(cmd)


def run_p_1_3():
    cmd = 'python cs285/scripts/run_hw4_mb.py --exp_name cheetah_n500_arch2x250 --env_name cheetah-cs285-v0 --add_sl_noise --n_iter 1 --batch_size_initial 20000 --num_agent_train_steps_per_iter 500 --n_layers 2 --size 250 --scalar_log_freq -1 --video_log_freq -1'
    os.system(cmd)

def run_p_2():
    cmd = 'python cs285/scripts/run_hw4_mb.py --exp_name obstacles_singleiteration --env_name obstacles-cs285-v0 --add_sl_noise --num_agent_train_steps_per_iter 20 --n_iter 1 --batch_size_initial 5000 --batch_size 1000 --mpc_horizon 10'
    os.system(cmd)


def run_p_3_1():
    cmd = 'python cs285/scripts/run_hw4_mb.py --exp_name obstacles --env_name obstacles-cs285-v0 --add_sl_noise --num_agent_train_steps_per_iter 20 --batch_size_initial 5000 --batch_size 1000 --mpc_horizon 10 --n_iter 12'
    os.system(cmd)


def run_p_3_2():
    cmd = 'python cs285/scripts/run_hw4_mb.py --exp_name reacher --env_name reacher-cs285-v0 --add_sl_noise --mpc_horizon 10 --num_agent_train_steps_per_iter 1000 --batch_size_initial 5000 --batch_size 5000 --n_iter 15'
    os.system(cmd)


def run_p_3_3():
    cmd = 'python cs285/scripts/run_hw4_mb.py --exp_name cheetah --env_name cheetah-cs285-v0 --mpc_horizon 15 --add_sl_noise --num_agent_train_steps_per_iter 1500 --batch_size_initial 5000 --batch_size 5000 --n_iter 20'
    os.system(cmd)


exp = {
    'run-p-1-1': run_p_1_1,
    'run-p-1-2': run_p_1_2,
    'run-p-1-3': run_p_1_3,
    'run-p-2': run_p_2,
    'run-p-3-1': run_p_3_1,
    'run-p-3-2': run_p_3_2,
    'run-p-3-3': run_p_3_3,
}

assert args.exp in exp
exp[args.exp]()