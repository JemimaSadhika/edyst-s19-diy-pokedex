<h3>A simple API is built which returns details of pokemon in JSON when an id for a particular integer is called for a specific pokemon.</h3>

<h3>How to setup the project:</h3>


1. Initially install VS Code,Python

2. Use virtual environments to run the application to run the application independently in a virtual environment without affecting the global environment

3. Install and activate virtual environment in your project folder.

4. Install "flask" and "requests" in the environment where the required packages are mentioned in requirements.txt file.

5. Install Postman which provides better interface to observe the URL outputs.



<h3>How to run the project:</h3>

1. Save app.py in VS Code and activate your virtualvenv .

2. The name of the virtualenv appears in left of prompt which shows virtualenv is active and then run the file app.py.

3. The file runs on the port <b>8006</b>.

4. Open Postman and type URL "http://localhost:8006/api/pokemon/1" in GET method which displays the details of pokemon with id=1 in JSON format.

5. Depending on integer value given as <b>id(range is 1-151)</b> in the URL, different pokemon details will be displayed.

6. This works even in the browser too with the same URL.

7. After running the application deactivate your virtualvenv.

<h3>Error Cases Handled:</h3>

1. If an id outside the range 1-151 is given in the URL like "http://localhost:8006/api/pokemon/249" then an error message <i>"The requested id is not valid. Please enter an id in between 1 and 151"</i> is displayed with <b>404 status code</b>.

2. If id provided is not of type integer then error message is displayed <i>"The id provided must be an integer value."</i> with <b>status code 500</b>.

3. All <b>404 errors</b> arised during execution display the error message <i>"The entered URL is not valid. Please enter a valid one."</i>
   These errors arise when the URL mentioned contains "http://localhost:8006/----"
   
4. For any other internal errors no specific error message is written which by default shows internal server error.   
   
