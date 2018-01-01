### Chinese-Readability-Analysis

# Project is intended to analysis Chinese texts for a readability score
# Training set of 200 texts will be given, with scalar training labels that indicate readability score
# Readability score will be scaled to range [0, 1], where 1 indicates maximum readability and 0 indicates no readability

#### Environment ####
Python 3.5 -> will update when possible

#### Required Libraries #####
tensorflow
numpy
xlrd
xlwt
urllib.request
matplotlib

#### Included Files #####
(name | function)
p_ws | defines object class pulls strings of text from online
p_nn | stores information on supervised agent
p_sample_ROTK | training dataset - Chinese novel Romance of the Three Kingdoms (三国演义)
p_sample_JTTW | training dataset - Chinese novel Journey to the West (三国演义)
p_sample_DRM | training dataset - Chinese novel Dream of Red Mansions (三国演义)
p_sample_WM | training dataset - Chinese novel Water Margin (三国演义)

more files to be included....

p_main | executable code which outputs readability scores and other information for the test dataset

# In progress
