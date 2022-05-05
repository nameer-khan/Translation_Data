# Translation_Data


```diff

+ Convert farmer details from English to different languages.

```

## IMPLEMENTATION:
## -------------------------------------------------------------------------------------


### STEP 1 - UPLOAD CSV
##### 1. First step is to create upload CSV mechanism, which is done in the uploadcsv() function. 
##### 2.Streamlit has the functionality to help with the upload mechanism, we can mention explicitly the type of file that we have to upload and look for. 
##### 3.We have mentioned csv for the same. After the file uploads , the resultant dataframe is made using pandas library and we display the same dataframe on the web app.



### STEP 2 - CHOOSE LANGUAGE FROM MENU
##### 1. Now we create the dropdown bar, which displays the languages Hindi, Punjab, Telugu and Marathi. 
##### 2. The function choose_language() with parameters (list_of_language,list_code_language) does the job. 
##### 3. list_of_language has languages(Hindi, Punjab, Telugu and Marathi) stores in a list , and list_code_language has corresponding code of the languages mentioned in it.('pa','mr','te','hi'). 
##### 4. So when the user selects a particular language , for ex : Punjab , 'pa' will then be passed to the function which is working with Googletrans which is a free python library that uses Google Translate API




### STEP 3 - TRANSLATION
##### 1. We make a translator object with the help of googletrans and will use the same to translate words from english to other languages.
##### 2. The function translation_work does the job here.
##### 3. Parameters provided are the dataframe, and the language code we got from previous step.
##### 4. We simply iterate over columns whose value is not of type int64 and get unique elements list from each column.
##### 5. Now translate each element from this list by passing it to the translate's objects' function which is translate as parameter and mention the destination language code 
##### 6. Response looks like this 
##### Translated(src=en, dest=pa, text=ਅੰਗਰੇਜ਼ੀ, pronunciation=Agarēzī, extra_data="{'confiden...")
##### 7. Save the result to a dictionary
##### 8. Reflect the changes back to dataframe using the dictionary



### STEP 4 - DOWNLOAD
##### 1. Now we have created a class FileDownloader with the constructor and function download()
##### 2. Provide the hyperlink properties and name in the href variable which will be passed in streamlits markdown() function
##### 3. Give the filename, and pass it streamlit function markdown()
## -----------------------------------------------------------------------------------


## We are done with the implementation


## ------------------------------------------------------------------------------------
# Before running make sure these libs are installed
## 1. pip install googletrans==4.0.0-rc1
## 2. pip install streamlit

# To Run , simply open command prompt, or anaconda prompt if using Anaconda, go to directory you have saved the files in, and run command
# streamlit run SDETask.py
# it will automatically open and redirect to http://localhost:8501/ with the frontend mechanism

## ------------------------------------------------------------------------------------

## SNAPSHOTS: 
![1](https://user-images.githubusercontent.com/45340840/166883118-d1b5e21c-83e2-4ee3-8fc4-d503c81674d9.png)
![Screenshot (11)](https://user-images.githubusercontent.com/45340840/166883136-dda3b816-5dc3-499d-aa5e-d778320ffce1.png)
![Screenshot (37)](https://user-images.githubusercontent.com/45340840/166883147-d5986bb7-616a-44d9-acea-6d14440ff911.png)
![Screenshot (38)](https://user-images.githubusercontent.com/45340840/166883174-9b572849-82d8-44b1-978c-666679ef390a.png)
![Screenshot (47)](https://user-images.githubusercontent.com/45340840/166883194-8f3d2537-2e9d-4b39-8890-60148a11383b.png)
![Screenshot (48)](https://user-images.githubusercontent.com/45340840/166883200-be41c564-0a43-4a6a-ba11-5e6456fb4a33.png)
![Screenshot (50)](https://user-images.githubusercontent.com/45340840/166883212-02888e32-af02-4d85-a2fc-792060db6461.png)



