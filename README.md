# Local-sensitivity-hashing
For the given dataset, use a locality sensitive hashing scheme to search for approximate nearest neghbors. Use the following queryset. You can use any parameter choices to obtain the nearest neighbors. Deliverables: 
1. The approximate nearest neighbors of the queries.                      
2. Describe all the parameters and the reason for choosing them.                     
3. The code for building the hash table and searching the tables.

Dataset - http://www.cs.unm.edu/~mueen/Teaching/CS591/Lectures/Images.zip
Queryset - http://www.cs.unm.edu/~mueen/Teaching/CS591/Lectures/Query.zip



I used LSHash library to perform Local Sensitive Hashing.    
LSHash(3, 255) – Initializing the hash table for 255 dimensions and 3 hash output bits. Since 255 values are returned as histogram out when applied on input BMP Images (32,32,3 dimension vector) .
 3 is the length of resulting Hash binary- I choose this value to obtain maximum similar images with Query function.

I used histogram as a feature for identifying the images in Hashing technique. 
Histogram done with function np.histogram() from numpy
I applied histogram on every image and then this histogram output is inserted in to the hash table one after the other to build the Hash Table.
lsh.index(listing) – inserting one entry after the other and building the Hash table.

For Querying the Hash table every time I am giving input as Histogram of the Query images.
That is I modified the query line 10 times manually for 10 images while giving input in code line  Image.open(queryset+"5"+fileext) , changing the number in red color.

I used lsh.query for querying the Hash Table.
Since the query retrieves all the images with similar histograms I have to filter them with a threshold value observed from the lsh.query(listing,distance_func="l1norm") .
I used manhattan distance, here l1norm  in lsh.query  which gives the distance measure from the input image to the query image. This result is used to filter the Images greater than a threshold i.e remove the images which are returned wrongly. 

Instead of going for these distance measures and threshold filtering, LShash function also support the functionality to find the maximum similar Input by using Rank with which we can get the top similar elements of the Query set with the Rank we require.


Also the output of the query will just return the histogram of image which is similar to the Query Image.  I have observed that the images in Query set are not exactly the same images as in Input Dataset 
The library function does not support to return the index number from which the output is picked. Again I have to check which Image histogram is the returned as output and finally return the original image number.



The code for building the hash table and searching the tables.

lsh = LSHash(3, 255) – For Initializing the Hash function.

lsh.index(listing) – Inserting one entry after the other and building the Hash table.

 K= lsh.query(listing,distance_func="l1norm") – For Querying the Hash table

 K returns the list of results which match with the image from the Query Image, here listing is 
 Input histogram of the Query image for Querying the Hash Table. 

distance_func="l1norm"    I took Manhattan distance as parameter which gives the distance from the Input image to the Query image which I used later to filter the similar images returned with the Query function from the Hash Table.


