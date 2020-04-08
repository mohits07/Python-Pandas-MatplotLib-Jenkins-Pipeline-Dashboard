from flask import Flask, render_template
import matplotlib.pyplot as plt
import pandas as pd
from io import  BytesIO
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

#import jenkins_data as jd

import app.jenkins_data as jd

app = Flask(__name__, template_folder = './app/templates' ) 


##webcode = open('webcode.html').read()


df2 = jd.generateExcel('cd')
df1 = jd.generateExcel('ci')


def cdBar():
	import matplotlib.pyplot as plt
	import pandas as pd
	plt.xticks(rotation='vertical')
	plt.xlabel('Number of Builds')
	plt.ylabel('No of builds')
	plt.title('Build result for last 30 days for Jenkins CD Prod')
	
	df2 = jd.generateExcel('cd')
	
	
	#df2 = df2[(~df2.Name.str.contains('Health')) & (~df2.Name.str.contains('Modify')) &  (~df2.Name.str.contains('StartStop')) ]
	
	df2 = df2[(~df2.Name.str.contains('Health')) & (~df2.Name.str.contains('Modify')) &  (~df2.Name.str.contains('StartStop')) & (~df2.Name.str.contains('Dashboard')) & 
       (~df2.Name.str.contains('Clone')) & (~df2.Name.str.contains('Scheduled')) & (~df2.Name.str.contains('List'))]

	
	
	groups = df2.groupby(['Name']).size().sort_values(ascending=False).head(10)
	

	groups.plot.barh()

	
	print("reachedhere_cd")
	plt.savefig("/usr/src/app/static/jobs_cd_prd_bar.png", bbox_inches='tight')
	plt.clf()
	
	

def cdPie():

	import matplotlib.pyplot as plt
	import pandas as pd

	# #FOR CD_PIE chart

	#df = pd.read_excel(r"C:\Users\msomaiya\Desktop\dashboard\jobs_cd_prd_30.xlsx")
		
	plt.xticks(rotation='vertical')
	plt.title('Build result for last 30 days for Jenkins CD Prod',y=1.08)
	
	#df2 = jd.generateExcel('cd')
	
	pie = pd.value_counts(df2['Result']).plot.pie(shadow=False,
												 # with colors
												 colors=['green', 'red', 'grey'],
												 # with one slide exploded out
												 explode=(0, 0, 0),
												 # with the start angle at 90%
												 startangle=90,
												 subplots=True, figsize=(6, 3),
												 # with the percent listed as a fraction
												 autopct='%1.1f%%', )
	plt.axis('equal')


	# View the plot
	plt.tight_layout()
	#plt.show()
	fig = pie[0].get_figure()
	print("reached cd_pie")
	fig.savefig("/usr/src/app/static/jobs_cd_prd_pie.png")
	plt.clf()
	
	
def ciPie():
	
		plt.xticks(rotation='vertical')
		plt.title('Build result for last 30 days for Jenkins CI Prod',y=1.08)
		
		df1 = jd.generateExcel('ci')
		
		df1 =  df1[(~df1.Result.str.contains('NOT_BUILT'))]
		
		pie = pd.value_counts(df1['Result']).plot.pie(shadow=False,
													 # with colors
													 colors=['green', 'red', 'grey'],
													 # with one slide exploded out
													 
													 explode=(0, 0, 0),
													 # with the start angle at 90%
													 startangle=90,
													 subplots=True, figsize=(6, 3),
													 # with the percent listed as a fraction
													 autopct='%1.1f%%', )
		plt.axis('equal')

		# View the plot
		plt.tight_layout()
		#plt.show()
		fig = pie[0].get_figure()
		fig.savefig("/usr/src/app/static/jobs_ci_prd_pie.png")
		plt.clf()
			

	
			
			

def ciBar():
    import matplotlib.pyplot as plt
    import pandas as pd
    plt.xticks(rotation='vertical')
    plt.xlabel('Number of Builds')
    plt.ylabel('Pipelines')
    plt.title('Build result for last 30 days for Jenkins CI Prod')

    df1 = jd.generateExcel('ci')
    df1 = df1[(~df1.Name.str.contains('BI_Automated_Deployment_Tag_Creation_And_Association')) & (~df1.Name.str.contains('BI_Build_Tag_INF_Upgrade_10.2')) & (
        ~df1.Name.str.contains('BI_Build_Tag')) & (~df1.Name.str.contains('R12_PatchBuilder')) &
              (~df1.Name.str.contains('TWS_Export_Create_Tag')) & (~df1.Name.str.contains('R12_Tag_Foundation'))]
    groups = df1.groupby(['Name']).size().sort_values(ascending=False).head(10)
    groups.plot.barh()

    # plt.savefig(r"C:\Users\msomaiya\Desktop\experiment\gg.png", bbox_inches='tight')
    print("reachedhere_ci")
    #plt.savefig("/usr/src/app/static/jobs_ci_prd_bar.png", bbox_inches='tight')
    plt.savefig("/usr/src/app/static/jobs_ci_prd_bar.png", bbox_inches='tight')
    # plt.show()
    plt.clf() 
		   			

#print(jd.generateExcel())

def cicdOne():
	
	#df = pd.read_excel("C:\\Users\\hasolank\\PycharmProjects\\flask\\files\\jobs_cd_prd_all_24.xlsx")
	#df2 = jd.generateExcel('cd')

	#df1 = pd.read_excel("C:\\Users\\hasolank\\PycharmProjects\\flask\\files\\jobs_ci_prd_all_24.xlsx")
	#df1 = jd.generateExcel('ci')

	df2['week'] = pd.to_datetime(df2['Duration'])
	df1['week'] = pd.to_datetime(df1['Duration'])
	# create a Series, grouping by week
	# replace datetimes with the week number
	# weekly_series.index = weekly_series.index.week
	# plt.ylabel('Count of success/failure builds')

	weekly_series = pd.concat({
		'CI': df1.groupby(pd.Grouper(key='week', freq='W'))['Name'].count(),
		'CD': df2.groupby(pd.Grouper(key='week', freq='W'))['Name'].count()
	}, axis=1)
	# and plot it
	# weekly_series.plot(kind='bar')

	weekly_series.index = weekly_series.index.week
	weekly_series.plot(kind='bar')
	plt.title('Build result for last 30 days  for Jenkins CI-CD Prod ')
	plt.ylabel('Number Of Builds')
	plt.savefig("/usr/src/app/static/jobs_cicd_prd_all.png", bbox_inches='tight')
	print("reached end")
	plt.clf()
	
	

@app.route('/dashboard')
def webprint():
	
		#print(jd.generateExcel())
    
	
	#df1 = jd.generateExcel('ci')
	#df2 = jd.generateExcel('cd')
	
	
	
	
	
	
	
	 #print(df)
	 
	 
#FOR CD_PIE chart
	
	cdPie()	
	
#FOR CI_PIE chart

	ciPie()
	
#FOR CI_bar graph
	
	ciBar()

#FOR CD_bar graph
	
	cdBar()
	
	
	
	
	
	#df = pd.read_excel(r"C:\Users\msomaiya\Desktop\data\jobs_cd_prd_all_30.xlsx")
	


	#For CI-CD in one chart
	cicdOne()

    
    
	return render_template('report.html', url1='/static/jobs_ci_prd_pie.png', url2='/static/jobs_ci_prd_bar.png', url3='/static/jobs_cd_prd_pie.png', 
	url4= '/static/jobs_cd_prd_bar.png', url5= '/static/jobs_cicd_prd_all.png') 



	
if __name__ == '__main__':
	app.run("0.0.0.0", 5002)
