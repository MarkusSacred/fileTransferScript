**File Transfer Script**

This is a basic script for transferring files. If you create an active backup of the database and don't want to perform manual transfers anymore, it's efficient to run a script on your server. In this code, you only need to have the


```Source File
Destination File
File name```
.
In this part of the code, we use os.path.join to check if the folder exists and then use os.path.exists to verify if the folder exists. If it does, we can create another folder and initiate the file transfer using shutl.move. We also use the print function to ensure that it has been successfully committed.
