
import os

from flask import Flask, render_template, request
app = Flask(__name__,static_url_path='/static')

# prediction function 
def ValuePredictor(): 

    return 1

@app.route('/')

def index():
    return render_template("index.html", message="Hello Flask!");   
@app.route('/analysis', methods = ['POST']) 
def analysis(): 
    if request.method == 'POST': 
        model_name=request.form['model'] 
        model_num=request.form['model'] 
        city_name=request.form['city']
        #print(model_name)
        #print(city_name)
        result= ValuePredictor() 
        if(model_name=='1'):
        	model_name= 'Waste Management'     
        elif(model_name=='2'):
        	model_name= 'Water Management'
        elif(model_name=='3'):
        	model_name= 'Population Analysis'
        elif(model_name=='4'):
        	model_name= 'Hospitals'
        elif(model_name=='5'):
        	model_name= 'Schools'
        elif(model_name=='6'):
        	model_name= 'All Model Combine'
        else:
        	model_name= 'Air Quality'

        if int(result)== 1: 
            prediction ='Income more than 50K'
        else: 
            prediction ='Income less that 50K'            
        #return render_template("analysis.html", prediction = prediction, model=model_name, city=city_name, model_num=model_num) 

        if(model_num=='1'):
        	report="4650 tons per day collected (550gms/capita),8.7 lakh sewer connections in the city [BWSSB]"
        	conc="More than 80% of Bangalore area dont't have ambient supply for proper waste Management and we had also estimated number of vehicles needed for  "
        	future="More data (current landfills, sewer lines, manpower  etc) need to be collected for effectively utilising available resources. "
        	img1="/static/waste/w1.png"
        	img2=""
        	img3=""
        	return render_template("analysis.html",report=report,conc=conc,future=future, prediction = prediction, model=model_name, city=city_name, model_num=model_num,img1=img1,img2=img2,img3=img3)
     
        elif(model_num=='2'):
        	report="Demand for water in Bangalore south is increasing at highest rate."
        	conc="With rapid growth in population, demand for water is also increasing. Above plot is showing the forecasting for demand in different zones of bangalore. "
        	future="With proper info on Reservoir we can manage distribution of water in all zones."
        	img1="/static/water/w1.png"
        	img2=""
        	img3=""
        	return render_template("analysis.html", prediction = prediction,future=future,conc=conc, report=report,model=model_name, city=city_name, model_num=model_num,img1=img1,img2=img2,img3=img3)

        elif(model_num=='3'):
        	report=" Bengaluru Population : 1.2 Crore, \n Population Growth Rate : 4% per year, \n Most Populated area : Horamavu, Bellandur, Dodda Bidarakallu, CV Raman Nagar"
        	conc="Population densities are growing at fast rate in Bangalore. Average Population density should be around 200 to 500 but in bengaluru almost each and every ward has population density >2000."
        	future="We can use satellite data to analyse Population density in effective way."
        	img1="/static/population/p1.gif"
        	img2=""
        	img3=""
        	return render_template("analysis.html", prediction = prediction, conc=conc,future=future,report=report, model=model_name, city=city_name, model_num=model_num,img1=img1,img2=img2,img3=img3)

        elif(model_num=='4'):
        	report= "Based on analysis of data, most of the accidents occurs in january month and mostly accidents occur between 9 and 10PM.\n  \n Also, there are less hospitals in accidental prone zone."
        	conc="In Recent times, Urban Planners follow population density data for chosing location for new hospital. With our prediction model, hospitals proposed by our density model reduces medical response time (in case of accidents) by 40%"
        	future="We can use satellite data to find crowded places and then based on this data we can provide better location for hospital construction. "
        	img1="/static/hospital/h5.png"
        	img2="/static/hospital/h4.png"
        	img3="/static/hospital/h3.png"
        	img4="/static/hospital/h1.png"
        	img5="/static/hospital/h2.png"
        	return render_template("analysis.html", future=future,img5=img5,prediction = prediction, model=model_name, img4=img4, conc=conc,  city=city_name, model_num=model_num,img1=img1,img2=img2,img3=img3,report=report)

        elif(model_num=='5'):
        	report="Most of the schools are located near highly populated density area."
        	conc="Schools are already located at Good location i.e near high population density area."
        	future="More data is required to know about education quality in schools and then we can suggest which schools need to upgrade."
        	img1="/static/school/s1.png"
        	img2=""
        	img3=""
        	return render_template("analysis.html", prediction = prediction,report=report,conc=conc,future=future, model=model_name, city=city_name, model_num=model_num,img1=img1,img2=img2,img3=img3)

        elif(model_num=='6'):
        	pred=""
        	img1="/static/aqi/aqi.png"
        	img2=""
        	img3=""
        	return render_template("analysis.html", prediction = prediction, model=model_name, city=city_name, model_num=model_num,img1=img1,img2=img2,img3=img3)
        else:
        	report="AQI of bengaluru is in Satisfactory Range. "
        	conc="AQI of bengaluru is in Satisfactory Range. We Should plant more and more tree. "
        	future=".."
        	img1="/static/aqi/aqi.png"
        	img2=""
        	img3=""
        	return render_template("analysis.html", prediction = prediction,report=report,conc=conc,future=future, model=model_name, city=city_name, model_num=model_num,img1=img1,img2=img2,img3=img3)



if __name__ == "__main__":
    app.run(debug=True)