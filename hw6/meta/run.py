import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('exp')
args = parser.parse_args()

def run_p_1():
    cmd = 'python train_policy.py pm-obs --exp_name pm-obs-1  --history 1 -lr 5e-5 -n 200 --num_tasks 4'
    os.system(cmd)


exp={
    'run-p-1': run_p_1,
}

assert args.exp in exp
exp[args.exp]()