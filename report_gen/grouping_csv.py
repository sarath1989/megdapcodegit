import numpy as np
import file_util.app_config as conf


def grping(speaker,wavs,grp_dict,sim_grp):
        data_var = []
        fields = []
        file_names = []
        config = conf.init()
        for item in range(np.count_nonzero(wavs)):
            data_var.append(item+1)
            file_names.append(wavs[item]['filename'])
        for key, val in grp_dict.items():
            fields.append(val)
        fields.append(sim_grp)
        curr_res = []
        result = []
        for ele in sorted(map(set, fields), key=len, reverse=True):
            if not any(ele <= req for req in curr_res):
                curr_res.append(ele)
                result.append(list(ele))
        print(result)
        data = 'file_name,'
        for num in range(len(fields)):
            data += "Group" + str(num + 1) + ','
        csv_file = open(config["REPORTS"]["grouping"], 'a+',newline='')
        csv_file.write('*'* 50+'\n')
        csv_file.write(f"Speaker:{speaker}"+'\n')
        csv_file.write('*' * 50 + '\n')
        csv_file.write(data)
        csv_file.write('\n')
        for idx in range(len(data_var)):
            list_of_grps = []
            for lists in range(len(fields)):
                if idx+1 in fields[lists]:
                    res = 'Present'
                else:
                    res = " "
                list_of_grps.append(res)
            list_of_grps.insert(0, wavs[idx]['filename'])
            append_grps = ''
            for ind in range(len(list_of_grps)):
                append_grps += (list_of_grps[ind]+',')
            csv_lines = []
            csv_lines.append(append_grps)
            print(csv_lines)
            for rl in csv_lines:
                csv_file.write(rl + "\n")
