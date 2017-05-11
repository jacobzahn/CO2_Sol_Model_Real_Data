# CO2_Sol_Model_Real_Data

This model builds off of the first model, which uses a simplified CO2 record to construct the CO2 radiative forcing for Earth, and compares it to solar forcing over the same time period. The only difference for the second model is that it also calculates the CO2 forcing using actual CO2 data from included excel file. This CO2 data is an amalgamation of a variety of different sources. The model 

# There are three modules involved in this model:

# A) CO2_Sol_main.py
This is the main module, and the one you will run. It imports the other modules, and then plots the results. The main difference in this module is that it makes plots for both the real and generalized CO2 data.

# B) CO2_Sol_globals.py
This module initializes the constants and variables that will be used in the model. These can be changed to fit the experiment. The main difference in this module from the first project to this one is that extra variables had to be created for the CO2 concentration and CO2 forcing values associated with the real and generalized CO2 data.

# C) CO2_Sol_calc.py
This module calcuates the Solar and CO2 forcings, which are then plotted against time in CO2_Sol_main.py. It is exactly the same as in the first model, except that CO2 forcings are calculated for real and generalized CO2 data.

# How to run the model
To run this model, first make sure all four of the above files (3 python files and 1 excel file) are in your working directory. Then in ipython or whichever interface you use, type "run CO2_Sol_main.py". The output will be two plots that show Solar Forcing, CO2 Forcing, and their sum over the time period of interest, for the real and generalized CO2 data.
