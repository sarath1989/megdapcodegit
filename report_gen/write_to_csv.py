import file_util.app_config as conf


def report_csv(report_lines):
    # config = conf.init()
    f = open(r"C:\Users\Dhanyashree M\PycharmProject\audio_project\reports\Report_80845274.csv", 'wt')
    for rl in report_lines:
        f.write(rl + "\n")