import comparison_calculation as cmp
import algorithms.processing as dm
from report_gen import write_to_csv as csv_file
import log_file as log
from file_util import read_file as rf


def pyannote_ref(val):
    files = rf.fetch_file()
    log.logger.info("Reading the files from the given directory")
    report_lines = []
    file_names= []

    for speaker, wavs in files.items():
        report_lines.append(f"Speaker: {speaker.split('_')[0]}")
        report_lines.append("*" * 50)
        for file_name in range(0, val):
            file_names.append(wavs[file_name]['filename'])
        filedata = ','
        for fl in file_names:
            filedata += fl + ','
        report_lines.append(filedata + 'Minimum_Score,Minimum_Score_File_Name,Result')

        for from_cmp_idx in range(val,len(wavs)):
            dist_list = []
            for to_cmp_idx in range(0, val):
                print("compare", from_cmp_idx, to_cmp_idx)
                print("compare", wavs[from_cmp_idx]['filename'], wavs[to_cmp_idx]['filename'])
                embedding1, embedding2, pre_process = dm.check_availability(wavs[from_cmp_idx],wavs[to_cmp_idx])
                dist = cmp.distance_calculation([embedding1], [embedding2])
                print("Distance Score", dist)
                similarity_distance = 1 - dist

                dist_list.append(similarity_distance)
                dist_data = ''
                for dl in dist_list:
                    dist_data += str(dl)+','
                print(dist_data)
                min_idx = dist_list.index(min(dist_list))
                min_file = wavs[min_idx]['filename']
            report_lines.append(wavs[from_cmp_idx]['filename']+','+dist_data+str(min(dist_list))+','+min_file)
        report_lines.append("*" * 50)
    csv_file.report_csv(report_lines)
