# DAGM2007-to-VOC
Generate VOC format dataset from defective images in DAGM2007 dataset.

## Step 1：Download the DAGM2007 dataset
You can download the DAGM2007 dataset from:  
>[DAGM2007](https://hci.iwr.uni-heidelberg.de/node/3616)
---
Then the data directory should looks like:   
```
-DAGM2007\
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
  ![DAGM2007-VOC](https://github.com/Levigty/blob/master/voc.JPG)  
  After getting the VOC format dataset in the save_dir, you can do defect detection.
