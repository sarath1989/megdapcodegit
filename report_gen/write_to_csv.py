from datetime import datetime
import file_util.app_config as conf

def report_csv(report_lines):
    config = conf.init()
    f = open(config["REPORTS"]["report"], 'wt')
    f.write(f"Similarity report run on: {datetime.now()}\n")
    f.write("*" * 50 + "\n")
    f.write("Start of report\n")
    f.write("*" * 50 + "\n")
    for rl in report_lines:
        f.write(rl + "\n")