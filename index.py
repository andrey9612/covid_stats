from flask import Flask, render_template, url_for,request, jsonify,send_file
from flask.helpers import send_file
import mysql.connector
import numpy as np
import pandas as pd

mydb= mysql.connector.connect(host="platform1.cy44rwtecws8.us-east-2.rds.amazonaws.com",user="admin",passwd="CStats_2021", database="Covid_Stat")
cursor= mydb.cursor()   


app = Flask(__name__)
#model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/impact')    
def impact():
    return render_template('impact.html')

@app.route('/survey')
def survey():
    return render_template('survey.html')

@app.route('/encuesta',methods=['POST'])
def predict():

    int_features = [int(x) for x in request.form.values()]
    #final_features = [np.array(int_features)]
    #print(final_features) 
    
    
    #------------------------------------------------
    #prediction = model.predict(final_features)
    #output = round(prediction[0], 2)
    #-----------------------------------------------
    
    genero=(int_features[0]) #1 femenino, 2 masculino
    edad=(int_features[1])
    grado=(int_features[2])
    p1=(int_features[3])
    p2=(int_features[4])
    p3=(int_features[5])
    p4=(int_features[6])
    p5=(int_features[7])
    p6=(int_features[8])
    p7=(int_features[9])
    p8=(int_features[10])
    p9=(int_features[11])
    p10=(int_features[12])
    p11=(int_features[13])
    p12=(int_features[14])
    p13=(int_features[15])
    p14=(int_features[16])
    p15=(int_features[17])
    p16=(int_features[18])
    p17=(int_features[19])
    p18=(int_features[20])
    p19=(int_features[21])
    p20=(int_features[22])
    p21=(int_features[23])
    p22=(int_features[24])
    p23=(int_features[25])
    p24=(int_features[26])
    p25=(int_features[27])
    p26=(int_features[28])
    p27=(int_features[29])
    
    resul_dis=(p1+p2+p3+p4+p6+p10+p11+p12+p16+p17+p18+p19+p20+p21+p22+p26+p27)
    resul_aut=(p5+p7+p8+p9+p13+p14+p15+p23+p24+p25)
    result=(resul_dis+resul_aut)
    

    query0="INSERT INTO comportamiento(id_comportamiento,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,p22,p23,p24,p25,p26,p27) VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(query0,(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,p22,p23,p24,p25,p26,p27))
    mydb.commit()

    #id, edad, genero, grado, Disforia, B_auto, total

    query1="INSERT INTO Kids(id, edad, genero, grado, Disforia, B_auto, total) VALUES(NULL,%s,%s,%s,%s,%s,%s)"
    cursor.execute(query1,(edad,genero,grado,resul_dis,resul_aut,result))
    mydb.commit()
    #Covid_Stat

    return render_template('survey.html')
    
    
@app.route('/result')
def result():
    df=pd.read_sql_query("SELECT * from Kids",mydb)

    x1=len(df[(df['edad']==7) & (df['Disforia']>8) & (df['genero']==1)])
    x2=len(df[(df['edad']==8) & (df['Disforia']>8) & (df['genero']==1) ])
    x3=len(df[(df['edad']==9) & (df['Disforia']>8) & (df['genero']==1) ])
    x4=len(df[(df['edad']==10) & (df['Disforia']>8) & (df['genero']==1) ])
    x5=len(df[(df['edad']==11) & (df['Disforia']>8) & (df['genero']==1) ])
    x6=len(df[(df['edad']==12) & (df['Disforia']>8) & (df['genero']==1)])

    x7=len(df[(df['edad']==7) & (df['Disforia']>8) & (df['genero']==2)])
    x8=len(df[(df['edad']==8) & (df['Disforia']>8) & (df['genero']==2) ])
    x9=len(df[(df['edad']==9) & (df['Disforia']>8) & (df['genero']==2) ])
    x10=len(df[(df['edad']==10) & (df['Disforia']>8) & (df['genero']==2) ])
    x11=len(df[(df['edad']==11) & (df['Disforia']>8) & (df['genero']==2) ])
    x12=len(df[(df['edad']==12) & (df['Disforia']>8) & (df['genero']==2)])

    x13=len(df[(df['edad']==7) & (df['B_auto']>8) & (df['genero']==1) ])
    x14=len(df[(df['edad']==8) & (df['B_auto']>8) & (df['genero']==1) ])
    x15=len(df[(df['edad']==9) & (df['B_auto']>8) & (df['genero']==1) ])
    x16=len(df[(df['edad']==10) & (df['B_auto']>8) & (df['genero']==1) ])
    x17=len(df[(df['edad']==11) & (df['B_auto']>8) & (df['genero']==1) ])
    x18=len(df[(df['edad']==12) & (df['B_auto']>8) & (df['genero']==1) ])

    x19=len(df[(df['edad']==7) & (df['B_auto']>8) & (df['genero']==2) ])
    x20=len(df[(df['edad']==8) & (df['B_auto']>8) & (df['genero']==2) ])
    x21=len(df[(df['edad']==9) & (df['B_auto']>8) & (df['genero']==2) ])
    x22=len(df[(df['edad']==10) & (df['B_auto']>8) & (df['genero']==2) ])
    x23=len(df[(df['edad']==11) & (df['B_auto']>8) & (df['genero']==2) ])
    x24=len(df[(df['edad']==12) & (df['B_auto']>8) & (df['genero']==2) ])

    x25=len(df[(df['edad']==7) & (df['total']>=19) & (df['genero']==1)])
    x26=len(df[(df['edad']==8) & (df['total']>=19) & (df['genero']==1)])
    x27=len(df[(df['edad']==9) & (df['total']>=19) & (df['genero']==1)])
    x28=len(df[(df['edad']==10) & (df['total']>=19) & (df['genero']==1)])
    x29=len(df[(df['edad']==11) & (df['total']>=19) & (df['genero']==1)])
    x30=len(df[(df['edad']==12) & (df['total']>=19) & (df['genero']==1)])

    x31=len(df[(df['edad']==7) & (df['total']>=19) & (df['genero']==2)])
    x32=len(df[(df['edad']==8) & (df['total']>=19) & (df['genero']==2)])
    x33=len(df[(df['edad']==9) & (df['total']>=19) & (df['genero']==2)])
    x34=len(df[(df['edad']==10) & (df['total']>=19) & (df['genero']==2)])
    x35=len(df[(df['edad']==11) & (df['total']>=19) & (df['genero']==2)])
    x36=len(df[(df['edad']==12) & (df['total']>=19) & (df['genero']==2)])    

    x37=len(df[(df['edad']==7)])
    x38=len(df[(df['edad']==8)])
    x39=len(df[(df['edad']==9)])
    x40=len(df[(df['edad']==10)])
    x41=len(df[(df['edad']==11)])
    x42=len(df[(df['edad']==12)])


    data0 = {'Edad' : 'participantes', 'Siete años':x1,'Ocho años':x2,'Nueve años':x3,'Diez años':x4,'Once años':x5,'Doce años':x6}
    data1 = {'Edad' : 'participantes', 'Siete años':x7,'Ocho años':x8,'Nueve años':x9,'Diez años':x10,'Once años':x11,'Doce años':x12}
    data2 = {'Edad' : 'participantes', 'Siete años':x13,'Ocho años':x14,'Nueve años':x15,'Diez años':x16,'Once años':x17,'Doce años':x18}
    data3 = {'Edad' : 'participantes', 'Siete años':x19,'Ocho años':x20,'Nueve años':x21,'Diez años':x22,'Once años':x23,'Doce años':x24}
    data4 = {'Edad' : 'participantes', 'Siete años':x25,'Ocho años':x26,'Nueve años':x27,'Diez años':x28,'Once años':x29,'Doce años':x30}
    data5 = {'Edad' : 'participantes', 'Siete años':x31,'Ocho años':x32,'Nueve años':x33,'Diez años':x34,'Once años':x35,'Doce años':x36}
    data6 = {'Edad' : 'participantes', 'Siete años':x37,'Ocho años':x38,'Nueve años':x39,'Diez años':x40,'Once años':x41,'Doce años':x42}
    
    return render_template('result.html',data=data0,data1=data1,data2=data2,data3=data3,data4=data4,data5=data5,data6=data6)


if __name__ == '__main__':
    app.run(debug=True)
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
