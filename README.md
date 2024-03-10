# Creating a Virtual Environment and Installing Requirements 

To ensure a smooth and controlled development environment, I'll walk you through the steps of creating a
virtual environment and installing the project's dependencies from the ```requirements.txt``` file.

* Navigate to the project directory using the cd
```cd /path-to-your/Boolean-Retrieval_Model```

* Once inside your project directory, create a new virtual environment by running the following command:
    * On Windows: ```cd /path-to-your/Boolean-Retrieval_Model```
    * On macOS and Linux: ```python3 -m venv venv```
  
* Now that you've created your virtual environment, you need to activate it:
    * On Windows: ```venv\Scripts\activate```
    * On macOS and Linux: ```source venv/bin/activate```

* With your virtual environment active, you can install all the required packages listed in the requirements.txt file:
    
    ```pip install -r requirements.txt```

This command will go through the requirements.txt file and install each package, ensuring that this project has all the 
necessary dependencies. 

Finally, execute the ``` main.py ```. That's it! 💻🚀 
