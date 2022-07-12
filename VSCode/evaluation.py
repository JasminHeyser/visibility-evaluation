import json
import os
from pathlib import Path
import matplotlib.pyplot as plt
import re
import numpy as np
import pandas as pd
from sklearn import linear_model
import statistics
from get_angle_range import get_angle_range

defect_key = "7_SEP_delta102_x100"
result_json_files = ('C:/Users/jheys/Documents/01_BA/VSCode/json_files/')



# ---------------plot domelight influence------------------------------
def influence_of_domelight(result_json_files,defect_key):
  i = 0
  theta_with_do = []
  du_with_do = []
  var_lap_with_do = []

  theta_without_do = []
  du_without_do = []
  var_lap_without_do = []

  for root, dirs, files in os.walk(result_json_files + defect_key): 
      for name in files:    
         path = os.path.join(root, name)
         
         with open(result_json_files + defect_key +'/'+name) as results:
            json_result_dict = json.load(results)
            #print(name)
            match_str = r".*?_a_matrix_(\d+)_([A-Z]{3})_delta(\d+)_x(\d+)_theta(\d+)_do(\d+)_du(\d\.\d+)_.*?.json$"

            res = re.match(match_str, name)
            if not res :
               print ('Bei dieser Datei wurde abgebrochen :', name)
               break
            
            theta = int(res.group(5))
            do = int(res.group(6))
            du = float(res.group(7))   

            if get_angle_range(defect_key,theta) ==True :
               if du>=0.2 and theta==0:
                  if do == 1   :
                     theta_with_do.insert(i,theta)
                     du_with_do.insert(i,du)
                     var_lap_with_do.insert(i,json_result_dict['var_laplacian']['var_results'])
                     i= i+1

                  else:
                     theta_without_do.insert(i,theta)
                     du_without_do.insert(i,du)
                     var_lap_without_do.insert(i,json_result_dict['var_laplacian']['var_results'])
                     i= i+1


#   print ("1st Input array : ", var_lap_with_do)
#   print ("2nd Input array : ", var_lap_without_do)
      
  dome_influence = np.subtract(var_lap_with_do, var_lap_without_do) 
  print ("domlight array: ", dome_influence)

       #--------------------Ergebnisse in 3DPlot anzeigen-------------------------
  fig = plt.figure(defect_key+"_3DPlot")
  ax = fig.add_subplot(111, projection='3d')
  ax.scatter(theta_with_do, du_with_do, var_lap_with_do, marker="*", c="blue", label= "Dom=an, Dunkelfeld=an (steigend)")
  ax.scatter(theta_without_do,du_without_do,var_lap_without_do, marker=".", c="red", label= "Dom=aus, Dunkelfeld=an (steigend)")
  ax.scatter(theta_without_do,du_without_do,dome_influence, marker="^", c="green", label= "Dom=an, Dunkelfeld=aus (errechnet)")
  ax.set_xlabel("Einfallswinkel")
  ax.set_ylabel("Intensität Dunkelfeldbeleuchtung")
  ax.set_zlabel("Laplace Varianz") 
  ax.legend()
  ax.set_title(defect_key)
  plt.show()

   #--------------------Ergebnisse in 2DPlot anzeigen-------------------------
   # plotting points as a scatter plot
  fig = plt.figure(defect_key+"_2DPlot")
  plt.scatter(du_with_do, var_lap_with_do,label= 'Dom=an, Dunkelfeld=an (steigend)', color= "blue",
               marker= "*", s=30)
  plt.scatter(du_without_do, var_lap_without_do ,label= 'Dom=aus, Dunkelfeld=an (steigend)', color= "red",
               marker= ".", s=30)
  plt.scatter(du_without_do,dome_influence, marker="^", c="green", label= "Dom=an, Dunkelfeld=aus (errechnet)")
   # x-axis label
  plt.xlabel('Intensität Dunkelfeldbeleuchtung')
   # frequency label
  plt.ylabel('Laplace Varianz')
   # plot title
  plt.title(defect_key)
   # showing legend
  plt.legend(loc="upper left")
      # function to show the plot
  plt.show()


def statistic(result_json_files,defect_key):
  i = 0
  theta_with_do = []
  du_with_do = []
  var_lap_with_do = []

  theta_without_do = []
  du_without_do = []
  var_lap_without_do = []
  
  for root, dirs, files in os.walk(result_json_files): 
      for name in files: 

       current_defect_directory = os.path.basename(os.path.dirname(root +'/'+name))
       
         
       with open(result_json_files+ '/' + current_defect_directory + '/' + name) as results:
            json_result_dict = json.load(results)
            print(name)
            match_str = r".*?_a_matrix_(\d+)_([A-Z]{3})_delta(\d+)_x(\d+)_theta(\d+)_do(\d+)_du(\d\.\d+)_.*?.json$"

            res = re.match(match_str, name)
            if not res :
               print ('Bei dieser Datei wurde abgebrochen :', name)
               break
            
            theta = int(res.group(5))
            do = int(res.group(6))
            du = float(res.group(7))   
            
            if get_angle_range(defect_key,theta) ==True :
               if du>=0.2:
                  if do == 1   :
                     theta_with_do.insert(i,theta)
                     du_with_do.insert(i,du)
                     var_lap_with_do.insert(i,json_result_dict['var_laplacian']['var_results'])
                     i= i+1

                  else:
                     theta_without_do.insert(i,theta)
                     du_without_do.insert(i,du)
                     var_lap_without_do.insert(i,json_result_dict['var_laplacian']['var_results'])
                     i= i+1
 
 
  var_lap_with_do_mean = statistics.median(var_lap_with_do)
  var_lap_without_do_mean = statistics.median(var_lap_without_do)
 
  statistic_dictionary={}

  median_ = {}
  median_ ["median_with_do"] = var_lap_with_do_mean
  median_ ["median_without_do"] = var_lap_without_do_mean





 
#   print(var_lap_with_do_mean)
#   
#   print(var_lap_without_do_mean)

  with open(result_json_files + "statistic_dict_alldefects.json", "w") as outfile:
          json.dump(statistic_dictionary,outfile)

def plot_3D_visible_angles(result_json_files,defect_key):

  i = 0
  theta_with_do = []
  du_with_do = []
  var_lap_with_do = []

  theta_without_do = []
  du_without_do = []
  var_lap_without_do = []

  for root, dirs, files in os.walk(result_json_files + defect_key): 
      for name in files:    
         path = os.path.join(root, name)
         
         with open(result_json_files+defect_key+'/'+name) as results:
            json_result_dict = json.load(results)
            #print(name)
            match_str = r".*?_a_matrix_(\d+)_([A-Z]{3})_delta(\d+)_x(\d+)_theta(\d+)_do(\d+)_du(\d\.\d+)_.*?.json$"

            res = re.match(match_str, name)
            if not res :
               print ('Bei dieser Datei wurde abgebrochen :', name)
               break
            
            theta = int(res.group(5))
            do = int(res.group(6))
            du = float(res.group(7))

            
             #--------------------winkelbereich bestimmen-------------------------
        
            if get_angle_range(defect_key,theta) ==True :
               if do == 1 :
                  theta_with_do.insert(i,theta)
                  du_with_do.insert(i,du)
                  var_lap_with_do.insert(i,json_result_dict['var_laplacian']['var_results'])
                  i= i+1

               else:
                  theta_without_do.insert(i,theta)
                  du_without_do.insert(i,du)
                  var_lap_without_do.insert(i,json_result_dict['var_laplacian']['var_results'])
                  i= i+1

  
      #--------------------Ergebnisse in 3DPlot anzeigen-------------------------
  fig = plt.figure(defect_key+"_3DPlot")
  ax = fig.add_subplot(111, projection='3d')
  ax.scatter(theta_with_do, du_with_do, var_lap_with_do, marker="*", c="blue", label= "Dom=1, Dunkelfeld")
  ax.scatter(theta_without_do,du_without_do,var_lap_without_do, marker=".", c="red", label= "Dom=0, Dunkelfeld")
  ax.set_xlabel("Einfallswinkel")
  ax.set_ylabel("Intensität Dunkelfeldbeleuchtung")
  ax.set_zlabel("Laplace Varianz") 
  ax.legend()
  ax.set_title(defect_key)
  plt.show()

   #--------------------Ergebnisse in 2DPlot anzeigen-------------------------
   # plotting points as a scatter plot
  fig = plt.figure(defect_key+"_2DPlot")
  plt.scatter(du_with_do, var_lap_with_do,label= 'Dom=1, Dunkelfeld', color= "blue",
               marker= "*", s=30)
  plt.scatter(du_without_do, var_lap_without_do ,label= 'Dom=0, Dunkelfeld', color= "red",
               marker= ".", s=30)
    # x-axis label
  plt.xlabel('Intensität Dunkelfeldbeleuchtung')
   # frequency label
  plt.ylabel('Laplace Varianz')
   # plot title
  plt.title(defect_key)
   # showing legend
  plt.legend(loc="upper left")
      # function to show the plot
  plt.show()


def plot_3D_all_angles(result_json_files,defect_key):

  i = 0
  theta_with_do = []
  du_with_do = []
  var_lap_with_do = []

  theta_without_do = []
  du_without_do = []
  var_lap_without_do = []

  for root, dirs, files in os.walk(result_json_files + defect_key): 
      for name in files:    
         path = os.path.join(root, name)
         
         with open(result_json_files+ defect_key +'/'+name) as results:
            json_result_dict = json.load(results)
            print(name)
            match_str = r".*?_a_matrix_(\d+)_([A-Z]{3})_delta(\d+)_x(\d+)_theta(\d+)_do(\d+)_du(\d\.\d+)_.*?.json$"

            res = re.match(match_str, name)
            if not res :
               print ('Bei dieser Datei wurde abgebrochen :', name)
               break
            
            theta = int(res.group(5))
            do = int(res.group(6))
            du = float(res.group(7))             
            
            if do == 1 :
               theta_with_do.insert(i,theta)
               du_with_do.insert(i,du)
               var_lap_with_do.insert(i,json_result_dict['var_laplacian']['var_results'])
               i= i+1

            else:
               theta_without_do.insert(i,theta)
               du_without_do.insert(i,du)
               var_lap_without_do.insert(i,json_result_dict['var_laplacian']['var_results'])
               i= i+1


      #--------------------Ergebnisse in 3DPlot anzeigen-------------------------
  fig = plt.figure(defect_key+"_3DPlot")
  ax = fig.add_subplot(111, projection='3d')
  ax.scatter(theta_with_do, du_with_do, var_lap_with_do, marker="*", c="blue", label= "Dom=1, Dunkelfeld")
  ax.scatter(theta_without_do,du_without_do,var_lap_without_do, marker=".", c="red", label= "Dom=0, Dunkelfeld")
  ax.set_xlabel("Einfallswinkel")
  ax.set_ylabel("Intensität Dunkelfeldbeleuchtung")
  ax.set_zlabel("Laplace Varianz") 
  ax.legend()
  ax.set_title(defect_key)
  plt.show()

   #--------------------Ergebnisse in 2DPlot anzeigen-------------------------
   # plotting points as a scatter plot
  fig = plt.figure(defect_key+"_2DPlot")
  plt.scatter(du_with_do, var_lap_with_do,label= 'Dom=1, Dunkelfeld', color= "blue",
               marker= "*", s=30)
  plt.scatter(du_without_do, var_lap_without_do ,label= 'Dom=0, Dunkelfeld', color= "red",
               marker= ".", s=30)
    # x-axis label
  plt.xlabel('Intensität Dunkelfeldbeleuchtung')
   # frequency label
  plt.ylabel('Laplace Varianz')
   # plot title
  plt.title(defect_key)
   # showing legend
  plt.legend(loc="upper left")
      # function to show the plot
  plt.show()


#-------------------plot_2D_light_statistic-------------------------------------

def plot_2D_light_statistic(result_json_files,defect_key):
   i = 0
   x_with_do = []
   y_with_do = []
   x_without_do = []
   y_without_do = []

   for root, dirs, files in os.walk(result_json_files): # hier immer den passenden Ordner Auswählen für die !Session!
      for name in files:    
         path = os.path.join(root, name)
         with open(result_json_files +'/'+name) as f:
            json_result_dict = json.load(f)
           # print(name)
            match_str = r".*?_a_matrix_(\d+)_([A-Z]{3})_delta(\d+)_x(\d+)_theta(\d+)_do(\d+)_du(\d\.\d+)_.*?.json$"

            res = re.match(match_str, name)

            if not res :
               print ('Bei dieser Datei wurde abgebrochen :', name)
               break

            Stent_ID = int(res.group(1))
            defect_ID = res.group(2)
            delta = int(res.group(3))
            x = int(res.group(4))
            theta = int(res.group(5))
            do = int(res.group(6))
            du = float(res.group(7))
            
         

            if do == 1 :
               x_with_do.insert(i,du)
               y_with_do.insert(i,json_result_dict['var_laplacian']['var_results'])  
               i= i+1

            else:
               x_without_do.insert(i,du)
               y_without_do.insert(i,json_result_dict['var_laplacian']['var_results'])  
               i= i+1

   
   # plotting points as a scatter plot
   plt.scatter(x_with_do, y_with_do,label= 'with do = true', color= "blue",
               marker= "*", s=30)
   
   plt.scatter(x_without_do, y_without_do ,label= 'with do = false', color= "red",
               marker= ".", s=30)

   # x-axis label
   plt.xlabel('light intesity of darkfield')
   # frequency label
   plt.ylabel('Laplacian Variance')
   # plot title
   plt.title('Laplacian Variance scatter plot')
   # showing legend
   plt.legend()
      # function to show the plot
   plt.show()



#-------------------multiple_regression------------------------------------

def multiple_regression(result_json_files, defect_key):
  i = 0
  theta_list = []
  do_list = []
  du_list = []
  var_lap_list = []
  for root, dirs, files in os.walk(result_json_files+defect_key): # hier immer den passenden Ordner Auswählen für die !Session!
      for name in files:    
         path = os.path.join(root, name)
         
         with open(result_json_files+ defect_key +'/'+name) as f:
            json_result_dict = json.load(f)
            print(name)
            match_str = r".*?_a_matrix_(\d+)_([A-Z]{3})_delta(\d+)_x(\d+)_theta(\d+)_do(\d+)_du(\d\.\d+)_.*?.json$"

            res = re.match(match_str, name)
            if not res :
               print ('Bei dieser Datei wurde abgebrochen :', name)
               break

            theta = int(res.group(5))
            do = int(res.group(6))
            du = float(res.group(7))


            #buiding the dataset
            theta_list.insert(i,theta)
            do_list.insert(i,do)
            du_list.insert(i,du)
            var_lap_list.insert(i,json_result_dict['var_laplacian']['var_results'])  
            i= i+1



  X = [[theta_list], 
       [do_list], [du_list]
      ]   

  y = [var_lap_list]
  
  regr = linear_model.LinearRegression()
  regr.fit(X, y)


  print('Intercept: \n', regr.intercept_)
  print('Coefficients: \n', regr.coef_)


#-------------------Auswahl Auswertung------------------------------------


#angle_analysis(result_json_files,defect_key)
#plot_2D_light_statistic(result_json_files,defect_key)
#multiple_regression(result_json_files,defect_key)
#plot_3D_all_angles(result_json_files,defect_key)
#plot_3D_visible_angles(result_json_files,defect_key)
influence_of_domelight(result_json_files,defect_key)
#statistic(result_json_files,defect_key)
