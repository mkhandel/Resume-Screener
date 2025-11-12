This is the README for a resume screener. It compares resumes to the job description and returns the similarity the five closest-matching resumes have to the job description.

## Setup Instructions
1. Download the parent folder. If necessary, unzip it. Enter the parent folder on your desktop.

2. Create a virtual environment in Python. The reason we use virtual environments is to isolate this project's environment from other projects' environments. Each Python project we have downloaded on our desktop can run with different versions with isolation. We also won't clutter one environment with dependencies from a bunch of different projects.
Here are the terminal commands to be performed inside the parent folder:
#tell Python to run the virtual environment module, and name that folder venv
python -m venv venv
#activate the virtual environment we just created
#source says use the current shell session, rather than starting a new process
#then, we have the path to the activaation script
source venv/bin/activate #this is for macOS and Linux
venv\Scripts\activate #this is for Windows

3. Install dependencies into virtual environment.
pip install -r requirements.txt

4. Set up OpenAI key
#we copy the template .env.example to our .env file, which we then fill with our personal information
cp .env.example .env

5. Upload resumes as .txt files to example_data/ folder (the folder can be renamed and modified in the scripts. I called it example data because I wasn't using real resumes.)

6. Run the application
streamlit run app.py

## Tradeoffs

Why I migrated from cosine similarity to FAISS:
Both cosine similarity and FAISS are used for calculations performed to determine how similar one vector is to others. Comparing hundreds, thousands, or millions of vectors gets very slow when using cosine similarity because the similarity between vectors has to be calculated on an individual basis. FAISS is scalable while cosine similarity is not. FAISS is also persistent--you can save your FAISS index, a data structure that stores vectors and allows for fast similarity searches. FAISS uses an index, or a data structure containing all the vector information to compare later, that can be saved in a file and retrieved for reuse later.

Why I migrated from Flask to Streamlit:
When users interact with inputs, the script reruns top-to-bottom automatically.
More importantly, it has minimal setup--you don't have to specify routes, HTML/CSS/JavaScript-it's just a lot less code.
