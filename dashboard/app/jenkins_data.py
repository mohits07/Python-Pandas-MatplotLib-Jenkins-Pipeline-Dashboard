import pandas as pd
import requests
import map
import dateutil.parser

import time
import datetime
import jenkins
from datetime import datetime
import re


#jenkins rest api to fetch pipelines and builds

def demo():
	return "hello"
	
def generateExcel(inst):

	instance = ''
	instance = inst
	
	#instance = 'ci'

	if instance == 'cd':
		response = requests.get(map.url_cd,auth=(map.username_cd, map.password_cd))
	elif instance == 'ci':
		response = requests.get(map.url_ci,auth=(map.username_ci, map.password_ci))
		
	elif instance == 'cmp':
		response = requests.get(map.url_cmp, auth=(map.username_cmp, map.password_cmp))
	else :
		response = requests.get(map.url_b2b, auth=(map.username_b2b, map.password_b2b))


	
	data = response.json()
	#print(data)


	# #working in local
	main_data = data.get('jobs')
	app_name = 'PearlChain'
	#res = {'name':[], 'result':[], 'number': [], 'duration': [], 'url': []}
	res = {'Name':[],'Result':[],'Duration':[],'Number' :[],'Application': [],'JobType':[],'url': []}
	print(main_data)
	days = 30
	for name_dict in main_data:
		if len(name_dict.get('builds', []))==0:
			continue

		for build_num in name_dict['builds'] :


			timefromjenkins = build_num.get('timestamp')
			readable = time.strftime('%m/%d/%Y %H:%M:%S',  time.gmtime(timefromjenkins/1000.))
			insertion_date = dateutil.parser.parse(readable)
			print(insertion_date)
			print(readable)
			time_between_insertion = datetime.now() - insertion_date


			if time_between_insertion.days < days:
				res['Name'].append(name_dict.get('name', 'NA'))
				res['Duration'].append(insertion_date)

				# durationval = build_num.get('duration')
				resultval = build_num.get('result')
				res['Result'].append(resultval)
				numberval = build_num.get('number')
				res['Number'].append(numberval)


				job_name = name_dict.get('name', 'NA')


				application = ['R12', 'PearlChain', 'Artis', 'OKA', 'Webcenter', 'Demantra', 'Jenkins', 'MSSQL',
							   'Webcenter','AppMigrate', 'ORACLE', 'BPM', 'AppInterface', 'Courion', 'ELK', 'TeamForge', 'R12-ATP', 'BI',
							   'DPA', 'Icon', 'MQ', 'Trillium', 'Informatica', 'ICC', 'Weblogic', 'TWS', 'MDM']

				flag_matched = 0
				for applicationname in application:
					str(applicationname)
					str(job_name)
					if re.search(applicationname, job_name, re.IGNORECASE):
						res['Application'].append(applicationname)
						flag_matched = 1
						break
				if flag_matched == 0 :
					if ((job_name == 'Pipeline_Release_Integrations') or (job_name == 'Pipeline_Release_Integrations_PROD') or (
						job_name == 'Pipeline_Release_Integrations_PROD_OLD') or (job_name == 'Pipeline_Startstop_IDM')):
						res['Application'].append('ICC')
					elif ((job_name == 'Adop') or (job_name == 'Adop_ERFDEV') or (job_name == 'DEV QA') or (job_name == 'Sanity')):
						res['Application'].append('R12')
					elif ((job_name == 'Automated_Apply_Datamasking')) :
						res['Application'].append('PearlChain')
					elif ((job_name == 'Automated_SQLServer_Backup' )) :
						res['Application'].append('MSSQL')
					elif (( job_name == 'Automated_WBC_Deploy')):
						res['Application'].append('Webcenter')
					elif ((job_name == 'List') or (job_name == 'Modify') or (job_name == 'Pipeline_Add_SSHKeys_To_Agent') ):
						res['Application'].append('Jenkins')
					elif ((job_name == 'Backup' )) :
						res['Application'].append('Oracle')
					else :
						res['Application'].append('NA')

				if (re.search('Pipeline_ICC_Informatica_Inf_Upgrade_10.2', job_name, re.IGNORECASE) or re.search('Pipeline_ICC_Informatica', job_name, re.IGNORECASE) or re.search('Deploy', job_name, re.IGNORECASE) or re.search('Pipeline_BI_Deploy_AllTech_Inf_Upgrade_10.2', job_name, re.IGNORECASE) or re.search('Pipeline_BPM', job_name, re.IGNORECASE) or re.search('Pipeline_DPA', job_name, re.IGNORECASE) or re.search('Pipeline_PearlChain', job_name, re.IGNORECASE) or re.search('Pipeline_TWS', job_name, re.IGNORECASE) or re.search('R12_Hold_Release', job_name, re.IGNORECASE) or re.search('Automated_Apply_Datamasking', job_name, re.IGNORECASE) or re.search('Adop_ERFDEV', job_name, re.IGNORECASE) or re.search('Install_ELK_agent', job_name, re.IGNORECASE) or re.search('Adop', job_name, re.IGNORECASE) ):
					res['JobType'].append('Deployment')

				elif re.search('Clone', job_name, re.IGNORECASE):
					res['JobType'].append('Clone')

				elif (re.search('Cleanup', job_name, re.IGNORECASE) or re.search('R12_Hold_Release', job_name,re.IGNORECASE) or re.search('Pipeline_R12_Editions', job_name, re.IGNORECASE)):
					res['JobType'].append('Maintenance')

				elif (re.search('ESPM',job_name, re.IGNORECASE) or re.search('Oracle_Get_Nodes',job_name, re.IGNORECASE) or re.search('Automated_Artis_Sqlexecute',job_name, re.IGNORECASE) or re.search('Ceritificate', job_name, re.IGNORECASE) or re.search('Dashboard', job_name,re.IGNORECASE) or re.search('List', job_name,re.IGNORECASE) or re.search('Modify', job_name, re.IGNORECASE) or re.search('Pipeline_BI_Queries', job_name, re.IGNORECASE) or re.search('FNB', job_name, re.IGNORECASE) or re.search('Pipeline_AppInterface_Icon_ATP_Cycle', job_name,
					re.IGNORECASE) or re.search('PC_CheckUsers',job_name,re.IGNORECASE) or  re.search(
			'Get_TeamForge_Data', job_name, re.IGNORECASE)  or re.search('Todays_R12_Patch_Report',job_name,re.IGNORECASE)or re.search('Pipeline_R12_ESPM_Queries', job_name,
																		re.IGNORECASE)):
					res['JobType'].append('Reporting')
				elif (re.search('Health', job_name, re.IGNORECASE) or re.search('Wallet', job_name, re.IGNORECASE)):
					res['JobType'].append('HealthChecks')
				elif (re.search('StartStop', job_name, re.IGNORECASE) or re.search('Start_Stop', job_name, re.IGNORECASE) or re.search('Pipeline_Release_Integrations', job_name,re.IGNORECASE) or re.search('StopStart', job_name,re.IGNORECASE)):
					res['JobType'].append('Start-Stop')
				elif (re.search('Backup', job_name, re.IGNORECASE) or re.search('GRP', job_name, re.IGNORECASE)):
					res['JobType'].append('Backup')
				elif re.search('Sanity', job_name, re.IGNORECASE):
					res['JobType'].append('Sanity')
				else :
					res['JobType'].append('Others')

				urlval = build_num.get('url')
				withlog = urlval+"consoleFull"
				res['url'].append(withlog)




		else:
			print("not found")

	#convert to pandas dataframe
	df = pd.DataFrame(res)
	#creating csv from dataframe
	#df.to_csv("jobs_cd_prd_all_"+str(days)+".csv", index=False)
	df.to_excel("jobs_"+instance+"_prd_"+str(days)+".xlsx", index=False)
	# df = pd.read_csv("jobs_prd.csv")
	# df.to_html("test.html")
	print("reached")
	return df


# Chart work done till now :
# 1. Build result for last 30 days for all jobs/pipelines bar chart for ci/cd
#
# 2. Bar chart showing Average build time for a specific application pipelines/jobs for last 30 days for ci/cd.
#
# 3. Bar chart showing pipelines run in ast 7 days with highest time for ci/cd.

