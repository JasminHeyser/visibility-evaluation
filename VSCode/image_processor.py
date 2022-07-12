import cv2
from FocusMethods.LAP import diagonal_laplacian,modified_laplacian,variance_of_laplacian
import os
import json
from Otsu import find_threshold_otsu
from STAT import calc_grayvalue_variance, calc_histogram_range
from helpers.maskimages import maskimage
from pathlib import Path
from helpers.rescale import rescaleimage
from Var_LAP import variance_of_laplacian
import sys 


def find_mask_image(basepath,maskname):
    mask_base_path = basepath+ '/exported_Toolima_masks'
    for root, dirs, files in os.walk(mask_base_path):
        for dir in dirs:    
           maskpath = os.path.join(root, dir,maskname+'___fullmask.pgm')
           if os.path.exists(maskpath):
               return maskpath, dir
    raise Exception('mask not found')
    

def image_processor(image_path):
    basepath = os.path.abspath(os.path.join(image_path,"..",".."))
    #select the path
    for root, dirs, files in os.walk(image_path):
        for name in files:
            if not name.endswith('jpg'):
                break

            path = os.path.join(root, name)
            img= cv2.imread(path, 0)  #now, we can read each file since we have the full path
            
            #rescale, view and save of in read image
            '''
            #   rescaling of the inread image ( just to view it! otherwise values would be falsified)
            #view_img = rescaleimage(img,scale=0.3)
            
            #   anzeigen des eingelesenen Bildes mit rescale damit überhaupt sichtbar
            #cv2.imshow('Original bild' ,view_img)

            #   speichern des eingelesenen Bildes 
            #cv2.imwrite("C:/Users/jheys/Documents/01_BA/VSCode/TestingStuff/"+name+"___original.jpg", img)
            
            '''
        
            #   creating the  path for the mask image
            Path('file.ext').stem  #  .stem makes sure that only the name is displayed withoud the jpg extension
            maskname = Path(name).stem
            maskpath,mask_subdir = find_mask_image(basepath,maskname)
            # maskpath = basepath+ '/exported_Toolima_masks/79_IDC_delta218_x13/'+maskname+'___fullmask.pgm'
            
            '''
            #   gibt den Namen der Maske aus
            #print("Masken Name", maskname)
            # #   gib den gesamten Maskenpfad aus
            # print("das ist der Maskenpfad", maskpath)
            '''

            #   load mask image
            mask = cv2.imread(maskpath,cv2.IMREAD_UNCHANGED)
            #   rescale of the mask image
            '''
            view_mask = rescaleimage(mask,scale=0.3)
            '''
        

            #   entbinarisieren der Maske und anzeigen
            ret, nonbin_mask = cv2.threshold(mask,0,255,cv2.THRESH_BINARY)
        
            #show and save prepared mask
            '''
            #cv2.imshow("binarisierte Maske",binmask)
            #   save nonbinarized mask image
            #cv2.imwrite("C:/Users/jheys/Documents/01_BA/VSCode/TestingStuff/"+maskname+"___BinMask.jpg", binmask)

            '''
            

            #   maskieren des Bilds 
            ''' 
            #masked_img= maskimage(img,nonbin_mask)
            # cv2.imshow("Maskiertes Bild",maskedimg)
            #   save masked image
            #cv2.imwrite("C:/Users/jheys/Documents/01_BA/VSCode/TestingStuff/"+maskname+"___Maskedimage.jpg", maskedimg)
            '''
        

            #Ergebniss dictionary
            result_dictionary={}


            # #   calculate Laplacian variance of the masked Image
            variance_of_Laplace = variance_of_laplacian(img, nonbin_mask, result_dictionary)
            print('Laplacian variance of the masked image'+name+':' ,variance_of_Laplace)
        
            # # #   calculate Laplacian variance of the masked Image
            # # varlap = variance_of_laplacian(maskedimg)
            # # print("Laplacian variance of the masked Image:",varlap)

            # gray_var = calc_grayvalue_variance(img,nonbin_mask,result_dictionary)
            # print('Gray value variance of the masked image'+name+':' ,gray_var)
            

            # hist_range = calc_histogram_range(img,nonbin_mask,result_dictionary)
            # print('histogram_range of the masked image'+name+':' ,hist_range)
            
                
            # otsu_thresh = find_threshold_otsu(img, nonbin_mask)
            # print ("otsu_thresh" , otsu_thresh)


        #Writing to .json
            os.makedirs(basepath+ "/VSCode/testjson_files/"+mask_subdir,exist_ok=True)
            with open(basepath+ "/VSCode/testjson_files/"+mask_subdir +"/"+ Path(name).stem +".json", "w") as outfile:
                    json.dump(result_dictionary,outfile)

if __name__ == "__main__":
    # main(sys.argv[1])
    image_processor('C:/Users/jheys/Documents/01_BA/Bilddaten/SEP')
