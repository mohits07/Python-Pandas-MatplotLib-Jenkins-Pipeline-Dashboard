from flask import Flask, render_template

app = Flask(__name__,  template_folder= './app/templates') 


##webcode = open('webcode.html').read()

@app.route('/dashboard')
def webprint():
    
    return render_template('report.html', url1='/static/jobs_ci_prd_all_24_result.png', url2='/static/jobs_ci_prd_all_30days_count.png', url3='/static/jobs_cd_prd_all_24.png', 
	url4= '/static/jobs_cd_prd_30days_count.png', url5= '/static/jobs_cicd_prd_all_25.png') 

	
	
    # return render_template('report.html', url1='/static/jobs_ci_prd_all_24_result.png', url2='/static/jobs_ci_prd_all_30days_count.png', url3='/static/jobs_cd_prd_all_24.png', 
	# url4= '/static/jobs_cd_prd_all_30days_count.png', url5= '/static/jobs_cicd_prd_all_25.png') 

if __name__ == '__main__':
    app.run()
