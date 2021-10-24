import os
import re
import shutil
def regex_renamer():
	Series = ["Breaking Bad","Game of Thrones","Lucifer"]
	print("1. Breaking Bad")
	print("2. Game of Thrones")
	print("3. Lucifer")
	webseries_num = int(input("Enter the number of the web series that you wish to rename. 1/2/3: "))
	season_padding = int(input("Enter the Season Number Padding: "))
	episode_padding = int(input("Enter the Episode Number Padding: "))
	if webseries_num<0 or webseries_num>len(Series):
		print("The webseries_num is out of range")
		return
	corrected_srt = os.path.join(os.getcwd(),"corrected_srt")
	os.makedirs(corrected_srt,exist_ok = True)
	corr_dir = os.path.join(corrected_srt,Series[webseries_num-1])
	if os.path.exists(corr_dir):
		return 
	os.makedirs(corr_dir,exist_ok = True)
	wrong_srt = os.path.join(os.getcwd(),"wrong_srt")
	wrong_dir = os.path.join(wrong_srt,Series[webseries_num-1])
	file_names = os.listdir(wrong_dir)
	if webseries_num==1:
		for file_name in file_names:
			x = re.search("s\d\de\d\d",file_name).start()
			season = int(file_name[x+1:x+3])
			episode = int(file_name[x+4:x+6])
			x1 = "{:0{}d}".format(season,season_padding)
			x2 = "{:0{}d}".format(episode,episode_padding)
			final_name = f"{Series[webseries_num-1]} - Season {x1} Episode {x2} -"
			if re.search(".mp4",file_name):
				final_name+=".mp4"
			else:
				final_name+=".srt"
			os.chdir(corr_dir)
			with open(final_name,'w') as file:
				shutil.copy(os.path.join(wrong_dir,file_name),os.path.join(corr_dir,final_name))
			print(final_name)	
		return
	for file_name in file_names:
		k = re.split("-",file_name)
		sea_epi = k[1].strip().split('x')
		epi_ext =  k[2].split(".")
		epi_title =epi_ext[0].strip()+"."+epi_ext[-1].strip()
		x1 = "{:0{}d}".format(int(sea_epi[0]),season_padding)
		x2 = "{:0{}d}".format(int(sea_epi[1]),episode_padding)
		k[1],k[2] = f"- Season {x1} Episode {x2} - ",epi_title
		final_name = ''.join([elem for elem in k])
		os.chdir(corr_dir)
		with open(final_name,'w') as file:
			shutil.copy(os.path.join(wrong_dir,file_name),os.path.join(corr_dir,final_name))
		print(final_name)	
	return   
regex_renamer()

