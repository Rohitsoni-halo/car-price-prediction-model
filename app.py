import streamlit as st
import joblib
from PIL import Image
model=joblib.load('car-price-predictor')

st.title("Welcome to car price predictor")
st.header("In this model we will predict the price of car according to the specifications you want")


#st.success("This is used to display Success messages in a green box")
#st.warning("This is used to display Warning message in orange box")
#st.error("This is used to display Error messages in red box")
#st.info("This is used to display Information in a blue box")
with st.container():
    image=Image.open('pexels-jay-pizzle-3802510.jpg')
    st.image(image)

    st.text("Enter the specifications you want in you car")

    fuel_type= st.radio("Fuel Type", ('Diesel','Gas'))
    if fuel_type=='Diesel':
        fuel_type_encode=0  
    else:
        fuel_type_encode=1

aspiration= st.radio("Aspiration", ('Standard','Turbo'))
if aspiration=='Turbo':
    aspiration_encode=0  
else:
    aspiration_encode=1

door_number= st.radio("Number of doors", ('Two','Four'))
if door_number=='Four':
    door_number_encode=0  
else:
    door_number_encode=1

car_body= st.radio("Car Type", ('Convertible','Hard Top','Hatch Back','Sedan','Wagon'))
if car_body=='Convertible':
    car_body_encode=0  
elif car_body=='Hard Top':
    car_body_encode=1
elif car_body=='Hatch Back':
    car_body_encode=2
elif car_body=='Sedan':
    car_body_encode=3
else:
    car_body_encode=4

drive_wheel= st.radio("Drive Wheel", ('Rear Wheel Drive','Front Wheel Drive','Four Wheel Drive'))
if drive_wheel=='Rear Wheel Drive':
    drive_wheel_encode=2
elif drive_wheel=='Front Wheel Drive':
    drive_wheel_encode=1
else:
    drive_wheel_encode=0

engine_location= st.radio("Engine Location", ('Front','Rear'))
if engine_location=='Front':
    engine_location_encode=0  
else:
    engine_location_encode=1

engine_type= st.radio("Engine Type", ('DOHC','OHCV','OHC','L','Rotor','OHCF','DOHCV'))
engine_dict={'DOHC':0, 'OHCV':5, 'OHC':3, 'L':2, 'Rotor':6, 'OHCF':4, 'DOHCV':1}
engine_type_encode=engine_dict[engine_type]

cylinder_number= st.radio("Number of cylinders", ('4 Cylinders','6 Cylinders','5 Cylinders','3 Cylinders','12 Cylinders','2 Cylinders','8 Cylinders'))
cylinder_dict={'4 Cylinders':2, '6 Cylinders':3,'5 Cylinders':1,'3 Cylinders':4,'12 Cylinders':5,'2 Cylinders':6,'8 Cylinders':0}
cylinder_number_encode=cylinder_dict[cylinder_number]

fuel_system= st.radio("Fuel System", ('MPFI','2BBL','MFI','1BBL','SPFI','4BBL','ID','SPDI'))
fuel_dict={'1BBL':0,'2BBL':1,'4BBL':2,'ID':3,'MFI':4,'MPFI':5,'SPDI':6,'SPFI':7}
fuel_system_encode=fuel_dict[fuel_system]



compression_ratio=st.slider('Enter Compression Ratio',5,25)
if(compression_ratio>25 or compression_ratio<5):
    st.warning("Please enter the value of Compression Ratio between 5 and 25")
    flagcr=1
else:
    flagcr=0

horse_power=st.slider('Enter Horse Power',50,300)
if(horse_power>300 or horse_power<50):
    st.warning("Please enter the value of Horse Power between 50 and 300")
    flaghp=1
else:
    flaghp=0

peak_rpm=st.slider('Enter Peak rpm',4000,7000)
if(peak_rpm>7000 or peak_rpm<4000):
    st.warning("Please enter the value of Peak rpm between 4000 and 7000")
    flagpr=1
else:
    flagpr=0

city_mpg=st.slider('Enter City Mileage',10,50)
if(city_mpg>50 or city_mpg<10):
    st.warning("Please enter the value of City Mileage between 10 and 50")
    flagcm=1
else:
    flagcm=0

highway_mpg=st.slider('Enter Highway Mileage',15,55)
if(highway_mpg>55 or highway_mpg<15):
    st.warning("Please enter the value of Higheay Mileage between 15 and 55")
    flaghm=1
else:
    flaghm=0

#gender=st.selectbox('Select Gender',['Male','Female'])
submit_btn =st.button("Show Expected Price of vehicle")

if submit_btn==True:
    if(flagcr!=0 or flagcm!=0 or flaghm!=0 or flaghp!=0 or flagpr!=0):
        st.error("Kindly enter appropriate input values input values")
    else:
        intake=[[fuel_type_encode,aspiration_encode,door_number_encode,car_body_encode,drive_wheel_encode,engine_location_encode,engine_type_encode,cylinder_number_encode,fuel_system_encode,compression_ratio,horse_power,peak_rpm,city_mpg,highway_mpg]]
        result=model.predict(intake)[0]
        result=result*80
        st.write("The predicted price is ",result)

#st.selectbox('Select', [1,2,3])

#df=pd.read_csv('CarPrice.csv')
#newdf=df[['Price']]

#st.button('Hit me')
#st.data_editor('Edit data', data)
#st.checkbox('Check me out')
#st.radio('Pick one:', ['nose','ear'])
#st.selectbox('Select', [1,2,3])
#st.multiselect('Multiselect', [1,2,3])
#st.slider('Slide me', min_value=0, max_value=10)
#st.select_slider('Slide to select', options=[1,2,3,4,5,6],value=('red','blue','a','b','c','d'))
#st.write("You selected the option",option)
#st.text_input('Enter some text')
#st.number_input('Enter a number')
#st.text_area('Area for textual entry')
#st.date_input('Date input')
#st.time_input('Time entry')
#st.file_uploader('File uploader')
#st.download_button('On the dl', data)
#st.camera_input("一二三,茄子!")
#st.color_picker('Pick a color')

#gose jose portelia introduction to machine learning and data science amster class
