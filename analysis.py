# Author: Michael Crampton
# All of the code below is written by me, none of it comes from an outside source, though I will reference where anyone assisted
# me where I had issues getting the code to run.

# Importing required modules
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Reading in the csv file of the data set
df = pd.read_csv (r'C:\Users\lenovo\OneDrive\Desktop\Important Documents\College Stuff\Programming and Scripting\pands-problem-sheet\IRIS.csv')

# Creating variables of sub data frames for use later in the code
sepal_length = df.sepal_length
sepal_width = df.sepal_width
petal_length = df.petal_length
petal_width = df.petal_width

# Creating varibles of the sepal and petal lengths and widths by species based on their location in the csv file
SepLenIrSet = (sepal_length[0:50])
SepWidIrSet = (sepal_width[0:50])
PetLenIrSet = (petal_length[0:50])
PetWidIrSet = (petal_width[0:50])
SepLenIrVer = (sepal_length[50:100])
SepWidIrVer = (sepal_width[50:100])
PetLenIrVer = (petal_length[50:100])
PetWidIrVer = (petal_width[50:100])
SepLenIrVir = (sepal_length[100:150])
SepWidIrVir = (sepal_width[100:150])
PetLenIrVir = (petal_length[100:150])
PetWidIrVir = (petal_width[100:150])

# Creating variables of the means and standard deviations for use in the Variable Summary.txt document
SLSetM = round(np.mean(SepLenIrSet), 2)
SWSetM = round(np.mean(SepWidIrSet), 2)
PLSetM = round(np.mean(PetLenIrSet), 2)
PWSetM = round(np.mean(PetWidIrSet), 2)
SLVerM = round(np.mean(SepLenIrVer), 2)
SWVerM = round(np.mean(SepWidIrVer), 2)
PLVerM = round(np.mean(PetLenIrVer), 2)
PWVerM = round(np.mean(PetWidIrVer), 2)
SLVirM = round(np.mean(SepLenIrVir), 2)
SWVirM = round(np.mean(SepWidIrVir), 2)
PLVirM = round(np.mean(PetLenIrVir), 2)
PWVirM = round(np.mean(PetWidIrVir), 2)

SLSetStd = round(np.std(SepLenIrSet), 2)
SWSetStd = round(np.std(SepWidIrSet), 2)
PLSetStd = round(np.std(PetLenIrSet), 2)
PWSetStd = round(np.std(PetWidIrSet), 2)
SLVerStd = round(np.std(SepLenIrVer), 2)
SWVerStd = round(np.std(SepWidIrVer), 2)
PLVerStd = round(np.std(PetLenIrVer), 2)
PWVerStd = round(np.std(PetWidIrVer), 2)
SLVirStd = round(np.std(SepLenIrVir), 2)
SWVirStd = round(np.std(SepWidIrVir), 2)
PLVirStd = round(np.std(PetLenIrVir), 2)
PWVirStd = round(np.std(PetWidIrVir), 2)

# This is argueably a slightly cumbersome way of writing to the text document, but it does work.
with open('VariableSummary.txt', 'w+') as f:
    print("Iris Setosa has a mean sepal length/sepal width/petal length/petal width of " + str(SLSetM) + "/" + str(SWSetM) + "/" 
    + str(PLSetM) + "/" + str(PWSetM) + " with a standard deviation of " + str(SLSetStd) + "/" + str(SWSetStd) + "/" 
    + str(PLSetStd) + " and " + str(PWSetStd) + " respectively.", file = f)
    print("Iris Versicolor has a mean sepal length/sepal width/petal length/petal width of " + str(SLVerM) + "/" + str(SWVerM) + "/" 
    + str(PLVerM) + "/" + str(PWVerM) + " with a standard deviation of " + str(SLVerStd) + "/" + str(SWVerStd) + "/" 
    + str(PLVerStd) + " and " + str(PWVerStd) + " respectively.", file = f)
    print("Iris Virginia has a mean sepal length/sepal width/petal length/petal width of " + str(SLVirM) + "/" + str(SWVirM) + "/" 
    + str(PLVirM) + "/" + str(PWVirM) + " with a standard deviation of " + str(SLVirStd) + "/" + str(SWVirStd) + "/" 
    + str(PLVirStd) + " and " + str(PWVirStd) + " respectively.", file = f)

# Creating the histograms of the species specific data to give a visual of the distribution. I initially tried to do a nested
# loop for the following histograms but that proved too complicated. Credit to "Azekawa", a friend from a discord server, for
# sugesting I simply use plt.clf() as an end function after each plt.savefig for simplicity.
plt.hist(SepLenIrSet)
plt.xlabel ("Length(cm)")
plt.ylabel ("Distribution")
plt.title ("Sepal Length of Iris Setosa")
plt.savefig('SepLen Iris Setosa.png')
plt.clf()

plt.hist(SepWidIrSet)
plt.xlabel ("Width(cm)")
plt.ylabel ("Distribution")
plt.title ("Sepal Width of Iris Setosa")
plt.savefig('SepWid Iris Setosa.png')
plt.clf()

plt.hist(PetLenIrSet)
plt.xlabel ("Length(cm)")
plt.ylabel ("Distribution")
plt.title ("Petal Length of Iris Setosa")
plt.savefig('PetLen Iris Setosa.png')
plt.clf()

plt.hist(PetWidIrSet)
plt.xlabel ("Width(cm)")
plt.ylabel ("Distribution")
plt.title ("Petal Width of Iris Setosa")
plt.savefig('PetWid Iris Setosa.png')
plt.clf()

plt.hist(SepLenIrVer)
plt.xlabel ("Length(cm)")
plt.ylabel ("Distribution")
plt.title ("Sepal Length of Iris Versicolor")
plt.savefig('SepLen Iris Versicolor.png')
plt.clf()

plt.hist(SepWidIrVer)
plt.xlabel ("Width(cm)")
plt.ylabel ("Distribution")
plt.title ("Sepal Width of Iris Versicolor")
plt.savefig('SepWid Iris Versicolor.png')
plt.clf()

plt.hist(PetLenIrVer)
plt.xlabel ("Length(cm)")
plt.ylabel ("Distribution")
plt.title ("Petal Length of Iris Versicolor")
plt.savefig('PetLen Iris Versicolor.png')
plt.clf()

plt.hist(PetWidIrVer)
plt.xlabel ("Width(cm)")
plt.ylabel ("Distribution")
plt.title ("Petal Width of Iris Versicolor")
plt.savefig('PetWid Iris Versicolor.png')
plt.clf()

plt.hist(SepLenIrVir)
plt.xlabel ("Length(cm)")
plt.ylabel ("Distribution")
plt.title ("Sepal Length of Iris Virginia")
plt.savefig ('SepLen Iris Virginia.png')
plt.clf()

plt.hist(SepWidIrVir)
plt.xlabel ("Width(cm)")
plt.ylabel ("Distribution")
plt.title ("Sepal Width of Iris Virginia")
plt.savefig('SepWid Iris Virginia.png')
plt.clf()

plt.hist(PetLenIrVir)
plt.xlabel ("Length(cm)")
plt.ylabel ("Distribution")
plt.title ("Petal Length of Iris Virginia")
plt.savefig('PetLen Iris Virginia.png')
plt.clf()

plt.hist(PetWidIrVir)
plt.xlabel ("Width(cm)")
plt.ylabel ("Distribution")
plt.title ("Petal Width of Iris Virginia")
plt.savefig('PetWid Iris Virginia.png')
plt.clf()



# I used regression plots in seaborn as opposed to scatterplots in matplotlib as seaborn just produces nicer graphs and plots
# and requires less code to get the regression line, which I wanted in the graph to give a better visual of the relationship
# between the variables. Also matplotlib was causing some issues with some of the regression lines in the scatterplots
# despite the fact the same code was being used to calculate the regression line.
# I just used plt.show() here as the brief only wanted the plots to be displayed as opposed to be saved as png files.
sns.regplot(x=SepLenIrSet, y=SepWidIrSet, line_kws={"color":"r"})
plt.xlabel("Length(cm)")
plt.ylabel("Width(cm)")
plt.title("Sepal Dimensions of Iris Setosa")
plt.show()

sns.regplot(x=SepLenIrVer, y=SepWidIrVer, line_kws={"color":"r"})
plt.xlabel("Length(cm)")
plt.ylabel("Width(cm)")
plt.title("Sepal Dimensions of Iris Versicolor")
plt.show()

sns.regplot(x=SepLenIrVir, y=SepWidIrVir, line_kws={"color":"r"})
plt.xlabel("Length(cm)")
plt.ylabel("Width(cm)")
plt.title("Sepal Dimensions of Iris Virginia")
plt.show()



sns.regplot(x=PetLenIrSet, y=PetWidIrSet, line_kws={"color":"r"})
plt.xlabel("Length(cm)")
plt.ylabel("Width(cm)")
plt.title("Petal Dimensions of Iris Setosa")
plt.show()

sns.regplot(x=PetLenIrVer, y=PetWidIrVer, line_kws={"color":"r"})
plt.xlabel("Length(cm)")
plt.ylabel("Width(cm)")
plt.title("Petal Dimensions of Iris Versicolor")
plt.show()

sns.regplot(x=PetLenIrVir, y=PetWidIrVir, line_kws={"color":"r"})
plt.xlabel("Length(cm)")
plt.ylabel("Width(cm)")
plt.title("Petal Dimensions of Iris Virginia")
plt.show()



sns.regplot(x=SepLenIrSet, y=PetLenIrSet, line_kws={"color":"r"})
plt.xlabel("Sepal Length(cm)")
plt.ylabel("Petal Length(cm)")
plt.title("Iris Setosa Sepal & Petal Lengths")
plt.show()

sns.regplot(x=SepLenIrVer, y=PetLenIrVer, line_kws={"color":"r"})
plt.xlabel("Sepal Length(cm)")
plt.ylabel("Petal Length(cm)")
plt.title("Iris Versicolor Sepal & Petal Lengths")
plt.show()

sns.regplot(x=SepLenIrVir, y=PetLenIrVir, line_kws={"color":"r"})
plt.xlabel("Sepal Length(cm)")
plt.ylabel("Petal Length(cm)")
plt.title("Iris Virginia Sepal & Petal Lengths")
plt.show()



sns.regplot(x=SepWidIrSet, y=PetWidIrSet, line_kws={"color":"r"})
plt.xlabel("Sepal Width(cm)")
plt.ylabel("Petal Width(cm)")
plt.title("Iris Setosa Sepal & Petal Widths")
plt.show()

sns.regplot(x=SepWidIrVer, y=PetWidIrVer, line_kws={"color":"r"})
plt.xlabel("Sepal Width(cm)")
plt.ylabel("Petal Width(cm)")
plt.title("Iris Versicolor Sepal & Petal Widths")
plt.show()

sns.regplot(x=SepWidIrVir, y=PetWidIrVir, line_kws={"color":"r"})
plt.xlabel("Sepal Width(cm)")
plt.ylabel("Petal Width(cm)")
plt.title("Iris Virginia Sepal & Petal Widths")
plt.show()



sns.regplot(x=SepLenIrSet, y=PetWidIrSet, line_kws={"color":"r"})
plt.xlabel("Sepal Length(cm)")
plt.ylabel("Petal Width(cm)")
plt.title("Iris Setosa Sepal Lengths & Petal Widths")
plt.show()

sns.regplot(x=SepLenIrVer, y=PetWidIrVer, line_kws={"color":"r"})
plt.xlabel("Sepal Length(cm)")
plt.ylabel("Petal Width(cm)")
plt.title("Iris Versicolor Sepal Lengths & Petal Widths")
plt.show()

sns.regplot(x=SepLenIrVir, y=PetWidIrVir, line_kws={"color":"r"})
plt.xlabel("Sepal Length(cm)")
plt.ylabel("Petal Width(cm)")
plt.title("Iris Virginia Sepal Lengths & Petal Widths")
plt.show()


sns.regplot(x=PetLenIrSet, y=SepWidIrSet, line_kws={"color":"r"})
plt.xlabel("Petal Length(cm)")
plt.ylabel("Sepal Width(cm)")
plt.title("Iris Setosa Petal Lengths & Sepal Widths")
plt.show()

sns.regplot(x=PetLenIrVer, y=SepWidIrVer, line_kws={"color":"r"})
plt.xlabel("Petal Length(cm)")
plt.ylabel("Sepal Width(cm)")
plt.title("Iris Versicolor Petal Lengths & Sepal Widths")
plt.show()

sns.regplot(x=PetLenIrVir, y=SepWidIrVir, line_kws={"color":"r"})
plt.xlabel("Petal Length(cm)")
plt.ylabel("Sepal Width(cm)")
plt.title("Iris Virginia Petal Lengths & Sepal Widths")
plt.show()