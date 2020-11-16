import os
from os import path
import shutil

"""
I need to add dataset1 and 
part1,2,3,and 4 to each frame.



"""
### dataset1 was the videos (not included) ###
img_folder_path = './dataset1/part1/'
dirListing = os.listdir(img_folder_path)
datasetnumber = "dataset" + str(input("What dataset number will you be working on? ")) + "/"
partnumber = "part" + str(input("What part will you be working on? ")) + "/"
nameoffile = datasetnumber[:-1] + partnumber[:-1]


def makefilestolists(dirListing):
    numbers = []
    newarray = []
    for i in dirListing:
        numbers = [str(i[6:14])] # getting the numbers of the file: ex. 00000800
        
        newarray.append(str(numbers[0]).zfill(8)) # numbers: ['00000217', '00000571'..... ]
    
    newlst = []
    newarray = sorted(newarray) # ['000000001', '00000217', '00000218', 00000218', ..., '00000923']

    for j in range(0, len(newarray)): 
        string = "frame-"  
        newlst.append(string + newarray[j] + nameoffile+ ".jpg")
        #['frame-000000001.jpg',...., 'frame-00000217.jpg', '00000218.jpg', 'frame-00000218.jpg', ..., 'frame-00000923.jpg']
    return newlst
    

newarray = makefilestolists(dirListing)


folderE = "./letterE/"
folderF = "./letterF/"
folderI = "./letterL/"
folderO = "./letterO/"
folderR = "./letterR/"
folderFive = "./numberFive/"
folderFour = "./numberFour/"
folderNine = "./numberNine/"
folderSeven = "./numberSeven/"
folderTen = "./numberTen/"


folders = [folderNine, folderTen, folderFour, folderFive,
folderSeven, folderE, folderI, folderF, folderR, folderO]



def transferFiles(dirListing):
    # for i in range(1,5):
    #     """
    #     You want to go into the dataset#, then go into the 
    #     part# folder, and perform the while loop on line 56.

    #     """


    """
    start = 34
    f = 10800000
    for f in range(1000):
        if (f-start) % 90 in [0,1,2,3,4]:
            print(f,"Keep")




    """
    currentFrame = int(input("What frame will you start on? "))

    while currentFrame < len(makefilestolists(dirListing)):
        for i in range(0,10):
            if currentFrame == 0 + currentFrame:
                for j in range(0,5):
                    shutil.copy('./datasetvideos/' + datasetnumber + partnumber + newarray[j + currentFrame -1], folders[i])
                    if j == 4:
                        currentFrame += 90
            elif currentFrame == 90 + currentFrame:
                for j in range(0,5):
                    shutil.copy('./datasetvideos/'+ datasetnumber + partnumber + newarray[j + currentFrame] , folders[i])
                    if j == 4:
                        currentFrame += 90
            elif currentFrame == 180 + currentFrame:
                for j in range(0,5):
                    shutil.copy('./datasetvideos/' + datasetnumber + partnumber + newarray[j + currentFrame], folders[i])
                    if j == 4:
                        currentFrame += 90            
            elif currentFrame == 270 + currentFrame:
                for j in range(0,5):
                    shutil.copy('./datasetvideos/'  + datasetnumber + partnumber + newarray[j + currentFrame], folders[i])
                    if j == 4:
                        currentFrame += 90
            elif currentFrame == 360 + currentFrame:
                for j in range(0,5):
                    shutil.copy('./datasetvideos/' +  datasetnumber + partnumber  +  newarray[j + currentFrame], folders[i])
                    if j == 4:
                        currentFrame += 90
            elif currentFrame == 450 + currentFrame:
                for j in range(0,5):
                    shutil.copy('./datasetvideos'+ datasetnumber + partnumber +  newarray[j + currentFrame], folders[i])
                    if j == 4:
                        currentFrame += 90
            elif currentFrame == 540 + currentFrame:
                for j in range(0,5):
                    shutil.copy('./datasetvideos/' + datasetnumber + partnumber + newarray[j + currentFrame], folders[i])
                    if j == 4:
                        currentFrame += 90
            elif currentFrame == 630 + currentFrame:
                for j in range(0,5):
                    shutil.copy('./datasetvideos/' +  datasetnumber  + partnumber + newarray[j + currentFrame], folders[i])
                    if j == 4:
                        currentFrame += 90
            elif currentFrame == 720 + currentFrame:
                for j in range(0,5):
                    shutil.copy('./datasetvideos/' +  datasetnumber + partnumber + newarray[j + currentFrame], folders[i])
                    if j == 4:
                        currentFrame += 90
            elif currentFrame == 810 + currentFrame:
                for j in range(0,5):
                    shutil.copy('./datasetvideos/' +  datasetnumber + partnumber  + newarray[j + currentFrame], folders[i])
                    if j == 4:
                        currentFrame += 90
            elif currentFrame == 900 + currentFrame:
                for j in range(0,5):
                    shutil.copy('./datasetvideos/' + datasetnumber + partnumber  +  newarray[j + currentFrame], folders[i])
                    if j == 4:
                        currentFrame += 90
            elif currentFrame == 990 + currentFrame:
                for j in range(0,5):
                    shutil.copy('./datasetvideos/' + datasetnumber + partnumber + newarray[j + currentFrame], folders[i])
                    if j == 4:
                        currentFrame += 90
            elif currentFrame == 1080 + currentFrame:
                for j in range(0,5):
                    shutil.copy('./datasetvideos/' + datasetnumber + partnumber + newarray[j + currentFrame], folders[i])
                    if j == 4:
                        currentFrame += 90
            elif currentFrame == 1170 + currentFrame:
                for j in range(0,5):
                    shutil.copy('./datasetvideos/' + datasetnumber  + partnumber + newarray[j + currentFrame], folders[i])
                    if j == 4:
                        currentFrame += 90
            elif currentFrame == 1260 + currentFrame:
                for j in range(0,5):
                    shutil.copy('./datasetvideos/'+ datasetnumber + partnumber  + newarray[j + currentFrame], folders[i])
                    if j == 4:
                        currentFrame += 90
            else:
                break
transferFiles(newarray)


# for i in range(0, 10):
#     print(dirListing[i])


