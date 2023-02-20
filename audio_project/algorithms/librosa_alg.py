from file_util import read_file as rf
import comparison_calculation as cmp
import log_file as log
from algorithms import processing as dm
import report_gen.grouping_csv as grp_csv
import report_gen.write_to_csv as csv_file


def librosa_alg():
    files = rf.fetch_file()
    log.logger.info("Reading the files from the given directory")
    report_lines = []

    for speaker, wavs in files.items():
        diff_grp = []
        sim_grp = []
        grp_dict = {}
        sim_dict = {}
        report_lines.append(f"Speaker: {speaker.split('_')[0]}")
        report_lines.append("*" * 50)
        report_lines.append("File1, File2, Similarity Score, Compare, Program Result")
        for from_cmp_idx, wav in enumerate(wavs[:-1]):
            for to_cmp_idx in range(from_cmp_idx + 1, len(wavs)):
                log.logger.info(f"comparing file index: {from_cmp_idx} to {to_cmp_idx}")
                log.logger.info(f"comparing file: {wavs[from_cmp_idx]['filename']} to {wavs[to_cmp_idx]['filename']}")
                embedded_data_f1, embedded_data_f2, preprocess_data = dm.check_availability(wavs[from_cmp_idx], wavs[to_cmp_idx])
                utt_sim_matrix = cmp.comparison(preprocess_data,wavs[from_cmp_idx], wavs[to_cmp_idx])
                log.logger.info(f"Similarity: {round(utt_sim_matrix[0][0] * 100, 2)}%")
                grp = [from_cmp_idx + 1, to_cmp_idx + 1]
                result = 'Same' if utt_sim_matrix[0][0] > 0.93 else 'Diff'

                if result == 'Same':
                    for i in range(len(grp)):
                        if grp[i] in diff_grp:
                            print("Already in sim_grp")
                        elif grp[i] not in sim_grp:
                            sim_grp.append(grp[i])
                    print(f"Group 1:{sim_grp}")
                    for k, v in grp_dict.items():
                        if grp[1] in v or grp[0] in v:
                            grp_dict[k] += [grp[0]]
                            set_dict = set(grp_dict[k])
                            grp_dict[k] = list(set_dict)
                    sim_dict = grp_dict
                else:
                    for j in range(len(grp)):
                        if grp[j] in sim_grp:
                            print("Already in sim_grp")
                        elif grp[j] not in diff_grp:
                            diff_grp.append(grp[j])
                        grp_dict = {x: [diff_grp[x]] for x in range(len(diff_grp))}
                        grp_dict.update(sim_dict)
                        print(f"Other groups in dictionary{grp_dict}")
                report_lines.append(f"{wavs[from_cmp_idx]['filename']}, {wavs[to_cmp_idx]['filename']},"
                                    f"{round(utt_sim_matrix[0][0] * 100, 2)}%,{from_cmp_idx+1,to_cmp_idx+1} "
                                    f"{result}")
        report_lines.append("*" * 50)
        grp_csv.grping(speaker,wavs,grp_dict,sim_grp)
    csv_file.report_csv(report_lines)
