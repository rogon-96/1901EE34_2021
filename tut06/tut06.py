import os
import re
def regex_renamer():
	Series = ["Breaking Bad","Game of Thrones","Lucifer"]
	print("1. Breaking Bad")
	print("2. Game of Thrones")
	print("3. Lucifer")
	webseries_num = int(input("Enter the number of the web series that you wish to rename. 1/2/3: "))
	season_padding = int(input("Enter the Season Number Padding: "))
	episode_padding = int(input("Enter the Episode Number Padding: "))
	if webseries_num<0 or webseries_num>len(Series):
		return
	corrected_srt = os.path.join(os.getcwd(),"corrected_srt")
	os.makedirs(corrected_srt,exist_ok = True)
	wrong_srt = os.path.join(os.getcwd(),"wrong_srt")
	wrong_dir = os.path.join(wrong_srt,Series[webseries_num-1])
	file_list = os.listdir(wrong_dir)
	# print(type(file_list))
	string = f'{str(season_padding)}.*{str(episode_padding)} | ..?{str(season_padding)}.*{str(episode_padding)}'
	print(string)
	pattern = re.compile(r'{}'.format(string))
	for files in file_list:
		found = re.finditer(pattern,files)
		for item in found:
			s = item.start()
			e = item.end()
			print(f'Found {files[s:e]} at {s}:{e}')
	corr_dir = os.path.join(corrected_srt,Series[webseries_num-1])
	os.makedirs(corr_dir,exist_ok = True)
	return   
regex_renamer()


