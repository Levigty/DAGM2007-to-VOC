# DAGM2007-to-VOC
Generate VOC format dataset from defective images in DAGM2007 dataset.

## Step 1：Download the DAGM2007 dataset
You can download the DAGM2007 dataset from:  
>[DAGM2007](https://hci.iwr.uni-heidelberg.de/node/3616)
---
Then the data directory should looks like:   
```
-raw_dataset\
    -Class1\
        -Train\
        -Test\
    -Class2\
        -Train\
        -Test\
    ...
    -Class10\
        -Train\
        -Test\
```
 ## Step 2: Conversion
 You can change the save_dir (line 9) to the fold name you like.
 ```
    run main.py to make the conversion
 ```

 ## Step 3: Doing something
 Using [labelImg](https://github.com/tzutalin/labelImg), we can see that the format and annotation of the dataset are correct, but some bounding-boxes may be too large.  
  <img src="https://github.com/Levigty/DAGM2007-to-VOC/blob/master/DAGM-VOC.JPG" width="320" alt="DAGM2007-VOC" align="middle"/>
  After getting the VOC format dataset in the save_dir, you can do defect detection.
