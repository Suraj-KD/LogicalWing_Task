# LogicalWing_Task
Practical task assigned by LogicalWings



Steps to execute the project :
------------------------------

1 : Make a directory with any name (ex : mkdir example ) and enter into the directory

2 : create a virtual environment using below command
      . virtualenv venv(environment name, can be any other name also)

3 : Enter into virtal environment (Go to the directory  which contains venv file)
      . source venv/bin/activate

4 : Clone the project from Git Repo usingbelow command
      . git clone https://github.com/Suraj-KD/LogicalWing_Task.git

5 : Enter into project directory ( cd Suraj_03_01_2019_Practical/ )

6 : Install all the rquirements
      . pip install -r requirements.txt



Project Execution Details :
--------------------------

It contains 2 app named medicine and employee. 

Enter the following url to get the app working
   medicine : 
      index : http://127.0.0.1:8000/medicine/
      medicine : http://127.0.0.1:8000/medicine/(?P<medicine_type>\w+)/$
      add_medicine_type : http://127.0.0.1:8000/medicine/add_medicine_type$
      add_medicine_details : http://127.0.0.1:8000/medicine/(?P<medicine_type>\w+)/add_medicine_detail$

   employee :
      employee_list : http://127.0.0.1:8000/employee/
      employee_detail : http://127.0.0.1:8000/employee/<int:pk>


http command to access the api : 
---------------------------------
   install httpie : pip install httpie
   
    Get employee List : http http://127.0.0.1:8000/employee/

    Get Employee Details : http http://127.0.0.1:8000/employee/1/
