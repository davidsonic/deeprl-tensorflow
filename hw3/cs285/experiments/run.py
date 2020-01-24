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


def run_dqn():
    cmd = 'python cs285/scripts/run_hw3_dqn.py --env_name PongNoFrameskip-v4 --exp_name test_pong'
    os.system(cmd)


exp = {
    'run-dqn': run_dqn,
}

assert args.exp in exp
exp[args.exp]()