import csv
import glob
import os

joined_files = os.path.join(r"C:\Users\Dhanyashree M\PycharmProject\audio_project\reports", "Report_Inter_Check_Files_Deshbandhu_*.csv")

# A list of all joined files is returned
joined_list = glob.glob(joined_files)
print(joined_list)
for filename in joined_list:
    with open(filename, mode="r",newline='') as old_file:
        reader_obj = csv.reader(old_file)

        with open("Report_Inter_Check_Files_Deshbandhu1.csv", mode="a",newline='') as new_file:
            writer_obj = csv.writer(new_file, delimiter=",")

            for data in reader_obj:
                writer_obj.writerow(data)

