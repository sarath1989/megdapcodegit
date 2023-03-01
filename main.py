import argparse
import sys
from file_util import app_config as conf
from algorithms import librosa_pyannote as lp,librosa_alg as lib,pyannote_ref as pc,pyannote_comparison as pa

if __name__ == "__main__":
    argumentList = sys.argv[0]
    config = conf.init()
    parser = argparse.ArgumentParser()

    parser.add_argument(config['OPTIONS']['algo'], nargs='?',choices=['librosa', 'pyannote','both'],help="Choose the algorithm:'librosa,'pyannote','both','refcompare'")
    parser.add_argument(config['OPTIONS']['mode'], nargs='+', choices=['fullcompare', 'refcompare'],help="Choose the mode:'fullcompare','refcompare'")
    parser.add_argument(config['OPTIONS']['refs'], nargs='+',type=int,help="The reference number to be compared")
    parser.add_argument(config['OPTIONS']['min'], nargs='+',type=int,help="The min number to be compared")
    parser.add_argument(config['OPTIONS']['max'], nargs='+',type=int,help="The max number to be compared")

    args = parser.parse_args()
    if args.algo == 'both':
        lp.lib_pyannote()
    elif args.algo == 'librosa':
        lib.librosa_alg()
    elif args.algo == 'pyannote' and args.mode == ['fullcompare']:
        pa.pyannote_alg()
    elif args.mode == ['refcompare']:
        val = args.refs
        min_no = args.min
        max_no = args.max
        pc.pyannote_ref(val[0],min_no[0],max_no[0])

