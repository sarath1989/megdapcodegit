import argparse
import sys
from file_util import app_config as conf
from algorithms import librosa_pyannote as lp,librosa_alg as lib,pyannote_ref as pc,pyannote_comparison as pa

if __name__ == "__main__":
    argumentList = sys.argv[0]
    config = conf.init()
    parser = argparse.ArgumentParser()

    parser.add_argument(config['OPTIONS']['algo'], nargs='?',choices=['librosa', 'pyannote','both','refcompare'],help="Choose the algorithm:'librosa,'pyannote','both','refcompare'")
    parser.add_argument(config['OPTIONS']['mode'], nargs='+', choices=['fullcompare', 'refcompare'],help="Choose the mode:'fullcompare','refcompare'")
    parser.add_argument(config['OPTIONS']['refs'], nargs='+',type=int,help="The reference number to be compared")

    args = parser.parse_args()
    if args.algo == 'both':
        lp.lib_pyannote()
    elif args.algo == 'librosa':
        lib.librosa_alg()
    elif args.algo == 'pyannote' and args.mode == ['fullcompare']:
        pa.pyannote_alg()
    elif args.mode == ['refcompare']:
        val = args.refs
        if args.refs is not None:
            pc.pyannote_ref(val[0])
        else:
            pc.pyannote_ref(2)
