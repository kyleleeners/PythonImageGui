# PythonImageGui
KNN colour classifier with GUI

After cloning, you should be able to just run the main in the GUI file. Upload a picture (I think only PNG works) and click around. I find that pictures with really defined colours work best (I added a colour wheel to the repo that works nicely)

When the GUI starts, it fires off the scikit-learn KNN model to fit some pickle data sets that I've included. These have the colours red, orange, yellow, green, blue, purple, pink, and white. Then when you click on a colour, it will pull the pixel rgb values from where you clicked and do a k=9 nearest neighbors prediction (K=9 was chosen via 10-fold cross-validation).

There is also the option to train the model if it seems incorrect. Click the dropdown and select the correct colour, then click the wrong colour button. This will add the current pixel rbg and the colour selected to the current dataset. If the program is exited naturally, any updates to the dataset will be saved and applied to later instances. 

I picked KNN because the rgb colours are really just the unit cube scaled up by 255 in every dimension, so Euclidean distance naturally makes sense.

TODOS:

- Option to customize your own colours
- general cleaup (learn some tkinter best practices)
