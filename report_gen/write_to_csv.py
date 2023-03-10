import file_util.app_config as conf


def report_csv(report_lines):
    config = conf.init()
    f = open(config["REPORTS"]["report"], 'wt')
    for rl in report_lines:
        f.write(rl + "\n")