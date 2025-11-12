This is the README for a resume screener. It compares resumes to the job description and returns the similarity the five closest-matching resumes have to the job description.

## Setup Instructions
1. Download the parent folder. If necessary, unzip it. Enter the parent folder on your desktop.

2. Create a virtual environment in Python. The reason we use virtual environments is to isolate this project's environment from other projects' environments. Each Python project we have downloaded on our desktop can run with different versions with isolation. We also won't clutter one environment with dependencies from a bunch of different projects.

  a. tell Python to run the virtual environment module, and name that folder venv:
python -m venv venv

  b. activate the virtual environment we just created

For macOS nd Linux, source venv/bin/activate

For Windows, env\Scripts\activate

3. Install dependencies into virtual environment.
pip install -r requirements.txt


4. Set up OpenAI key
  
  a. copy the template .env.example to our .env file, which we then fill with our personal information
cp .env.example .env

  b. replace spaceholder api key with your openai key

5. Upload resumes as .txt files to example_data/ folder. There are already some sample resumes inside the folder.

6. Run the application.
streamlit run app.py


## Migrations
Why I migrated from cosine similarity to FAISS:
Both cosine similarity and FAISS are used for calculations performed to determine how similar one vector is to others. Comparing hundreds, thousands, or millions of vectors gets very slow when using cosine similarity because the similarity between vectors has to be calculated on an individual basis. FAISS is scalable while cosine similarity is not. FAISS is also persistent--you can save your FAISS index, a data structure that stores vectors and allows for fast similarity searches. FAISS uses an index, or a data structure containing all the vector information to compare later, that can be saved in a file and retrieved for reuse later.

Why I migrated from Flask to Streamlit:
When users interact with inputs, the script reruns top-to-bottom automatically.
More importantly, it has minimal setup--you don't have to specify routes, HTML/CSS/JavaScript-it's just a lot less code.
