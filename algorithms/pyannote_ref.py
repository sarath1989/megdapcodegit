import pandas as pd
import comparison_calculation as cmp
import algorithms.processing as dm
import log_file as log
from file_util import read_file as rf


def pyannote_ref(cnt,min_no,max_no):
    files = rf.fetch_file()
    log.logger.info("Reading the files from the given directory")

    for speaker, wavs in files.items():
        file_names = []
        report_lines = []
        val = round((cnt / 100)*len(wavs))
        print("val:",val)
        if val >= max_no:
            indx = max_no
        elif val < min_no:
            indx = min_no
        elif val in range(min_no,max_no+1):
            indx = val
        print("indx:",indx)
        for file_name in range(0, indx):
            file_names.append(wavs[file_name]['filename'])
        filedata = ','
        for fl in file_names:
            filedata += fl + ','
        report_lines.append(filedata + 'Maximum_Score,Maximum_Score_File_Name')

        for from_cmp_idx in range(indx,len(wavs)):
            dist_list = []
            for to_cmp_idx in range(0, indx):
                print("compare", from_cmp_idx, to_cmp_idx)
                print("compare", wavs[from_cmp_idx]['filename'], wavs[to_cmp_idx]['filename'])
                embedding1, embedding2, pre_process = dm.check_availability(wavs[from_cmp_idx],wavs[to_cmp_idx])
                sim_dist = cmp.distance_calculation([embedding1], [embedding2])
                print("Distance Score", sim_dist)
                dist = 1- sim_dist
                dist_list.append(dist)
                dist_data = ''
                for dl in dist_list:
                    dist_data += str(dl)+','
                print(dist_data)
                max_idx = dist_list.index(max(dist_list))
                max_file = wavs[max_idx]['filename']
            report_lines.append(wavs[from_cmp_idx]['filename']+','+dist_data+str(max(dist_list))+','+max_file)

        file_nam = (file_names[0]).split('_', 3)
        f = open(f"{file_nam[0]}_{file_nam[1]}_{file_nam[2]}_Intra.csv", 'wt')
        # print(report_lines)
        for rl in report_lines:
            f.write(rl + "\n")
        f.close()
        result = []
        for count in range(len(wavs) - indx):
            if count < indx:
                result.append('yes')
            else:
                result.append('')
        df = pd.read_csv(f"{file_nam[0]}_{file_nam[1]}_{file_nam[2]}_Intra.csv")
        sorted_df = df.sort_values(by=["Maximum_Score"], ascending=False)
        sorted_df.columns.values[0] = ""
        sorted_df['Result'] = result
        sorted_df.to_csv(f"{file_nam[0]}_{file_nam[1]}_{file_nam[2]}_Intra.csv", index=False)