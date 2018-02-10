# PythonImageGui
KNN colour classifier with GUI

After cloning, you should be able to just run the main in the GUI file. Upload a picture (I think only PNG works) and click around. I find that pictures with really defined colours work best (I added a colour wheel to the repo that works nicely)

Basicaly when the GUI starts, it fires off the scikit-learn KNN model to fit some pickle data sets that I've included. These have the colours red, orange, yellow, green, blue, purple, and pink. Then when you click on a colour, it will pull the pixel rgb values from where you clicked and do a k=5 nearest neighbors prediction. 

I picked KNN because the rgb colours are really just the unit cube scaled up by 255 in every dimension, so Euclidean distance naturally makes sense.

Still to do for this wil be to add some learning into the GUI, basically if you get a colour wrong you can correct it and update the training error. Also just generally refining the GUI and maybe the model once I get alot of data (CNN would be much more efficient but it really needs defined borders to work)
