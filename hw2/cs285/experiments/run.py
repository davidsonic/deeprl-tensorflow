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

def run_sec_6():
    cmds = [
        'python cs285/scripts/run_hw2_policy_gradient.py --env_name CartPole-v0 -n 100 -b 1000 -dsa --exp_name sb_no_rtg_dsa',
        'python cs285/scripts/run_hw2_policy_gradient.py --env_name CartPole-v0 -n 100 -b 1000 -rtg -dsa --exp_name sb_rtg_dsa',
        'python cs285/scripts/run_hw2_policy_gradient.py --env_name CartPole-v0 -n 100 -b 1000 -rtg --exp_name sb_rtg_na',
        'python cs285/scripts/run_hw2_policy_gradient.py --env_name CartPole-v0 -n 100 -b 5000 -dsa --exp_name lb_no_rtg_dsa',
        'python cs285/scripts/run_hw2_policy_gradient.py --env_name CartPole-v0 -n 100 -b 5000 -rtg -dsa --exp_name lb_rtg_dsa',
        'python cs285/scripts/run_hw2_policy_gradient.py --env_name CartPole-v0 -n 100 -b 5000 -rtg --exp_name lb_rtg_na',
    ]
    for cmd in cmds:
        subprocess.run(shlex.split(cmd))


def run_sec_6_1():
    cmd = 'python cs285/scripts/run_hw2_policy_gradient.py --env_name CartPole-v0 -n 100 -b 1000 -dsa --exp_name sb_no_rtg_dsa'
    os.system(cmd)


# no standardize, no reward to go
def run_sec_6_1_1():
    cmd = 'python cs285/scripts/run_hw2_policy_gradient.py --env_name CartPole-v0 -n 10 -b 1000 -dsa --exp_name sb_no_rtg_dsa'
    os.system(cmd)


# with standardize, on reward to go
def run_sec_6_1_2():
    cmd = 'python cs285/scripts/run_hw2_policy_gradient.py --env_name CartPole-v0 -n 100 -b 1000  --exp_name sb_no_rtg'
    os.system(cmd)


def run_sec_6_2():
    cmd = 'python cs285/scripts/run_hw2_policy_gradient.py --env_name CartPole-v0 -n 100 -b 1000 -rtg -dsa --exp_name sb_rtg_dsa'
    os.system(cmd)

# large batch, no reward to go, no standardize
def run_sec_6_3_1():
    cmd = 'python cs285/scripts/run_hw2_policy_gradient.py --env_name CartPole-v0 -n 10 -b 5000  -dsa --exp_name lb_no_rtg_dsa'
    os.system(cmd)


def run_sec_6_seed():
    seeds = range(3)
    template = 'python cs285/scripts/run_hw2_policy_gradient.py --env_name CartPole-v0_seed_{seed} -n 100 -b 1000 -dsa --exp_name sb_no_rtg_dsa --seed {seed}'
    for seed in seeds:
        command = template.format(seed=seed)
        os.system(command)

def vis_sec_6_seed():
    seeds = range(3)
    folders = defaultdict(list)
    for folder in glob.glob('cs285/data/*'):
        if '_seed_' in folder:
            tokens = folder.split('_')
            index = int(tokens[2])
            folders[index].append(folder)
    print('folders: {}'.format(folders))
    returns = []
    for folder in folders[i]:
        metric_file = os.path.join(folder, 'metrics_0.json')
        with open(metric_file, 'r') as f:
            logs = json.load(f)
            mean = logs['Eval_Averagereturn']
            std = logs['Eval_StdReturn']
            returns.append(mena)
    print('returns: {}'.format(returns))


# problem 4
def run_p_4():
    cmd = 'python cs285/scripts/run_hw2_policy_gradient.py --env_name InvertedPendulum-v2  --discount 0.9 -n 100 -l 2 -s 64  -lr  1e-2 -rtg --exp_name ip_b1000_r1e-2 -eb 1000 --ep_len 1000 -b 1000 --video_log_freq 10'
    os.system(cmd)


def run_p_6():
    cmd = 'python cs285/scripts/run_hw2_policy_gradient.py --env_name LunarLanderContinuous-v2 --ep_len 1000 --discount 0.99 -n 100 -l 2 -s 64 -b 40000 -lr 0.005 -rtg --nn_baseline --exp_name ll_b40000_r0.005'
    os.system(cmd)


def run_p_7():
    cmd = 'python cs285/scripts/run_hw2_policy_gradient.py --env_name HalfCheetah-v2 --ep_len 150 --discount 0.95 -n 100 -l 2 -s 32 -b 10000 -lr 0.02 --video_log_freq -1 --reward_to_go --nn_baseline --exp_name hc_b10000_lr0.02_nnbaseline'
    os.system(cmd)


exp = {
    'run-sec-6-1-1': run_sec_6_1_1,
    'run-sec-6-1-2': run_sec_6_1_2,
    'run-sec-6-3-1': run_sec_6_3_1,
    'run-sec-6': run_sec_6,
    'run-sec-6-1': run_sec_6_1,
    'run-sec-6-2': run_sec_6_2,
    'run-p-4': run_p_4,
    'run-p-6': run_p_6,
    'run-p-7': run_p_7,
}
assert args.exp in exp
exp[args.exp]()