# # CreateDatabase---WebApp

This project was developed for the "Databases" course and aims to **design a model of a database** and **implement it**. Afterwards we should also **develop a simple Python application** for the database. This project is subdivided into two parts.

**Authors:**
- [Magda Costa](https://github.com/Maguids)
- Rafael Pacheco
- Sofia Machado

<br></br>

## Programming Language:

<div style = "display: inline_block"><br/>
  <img align="center" alt="python" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img align="center" alt="html" src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" />
  <img align="center" alt="sqlite" src="https://img.shields.io/badge/SQLite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white" />
    <img align="center" alt="css" src="https://img.shields.io/badge/CSS-239120?&style=for-the-badge&logo=css3&logoColor=white" />
</div><br/>

<br></br>

## Requirements:

- Python 3
- Pip 3 Package Manager
- sqlite3
- Flask
- Jinja Templates

### You can check if you already have this requirements by running:
- Python 3
```bash 
python3 --version
```
- Pip3: 
```bash 
pip3 --version
```
- Flask:
```bash 
flask --version
```
- sqlite3:
```bash 
sqlite3 --version
```

<br></br>

### If you need to install anything just run:
- Python 3 and Pip 3
```bash 
sudo apt-get install python3 python3-pip
```
- Flask: 
```bash 
pip3 install --user Flask
```
- sqlite3:
```bash 
sudo apt install sqlite3
```

**Note:** When you install Flask, Jinja is automatically installed.

<br></br>

## About the Project:

### Part 1 - Design the database:

In the first part of the project, we were expected to **design a database model** for a universe of our choice supported with real data, considering:
- the description of the universe in question and a corresponding **UML class diagram**;
- mapping the UML class model into a **relational model**;

**Worked develop:**
To accomplish this part, we started by doing intensive research on sites like Kaggle to find data that would allow us to carry out the project within the constraints defined in the project statement. To make this possible, we selected a dataset with the 'Disney' theme and completed it so that we could use it.

### Part 2 - Create the Database and an APP :
This part of the project is intended to **implement the database model** proposed in part 1 in an **SQLite database** populated with the data and the **development of a simple python app** of the interface for the database.

**Worked develop:**
We start by creating the SQLite database and then we create the application that allows us to search by character, by the director of the film... It also allows us to see the relationships between each table created in the database model and do different types of searches through data.

<br></br>

## About the repository:
In this repository we have two folders correspondent to the two parts:

🔵 **Part 1:**
- assignment_part_1.pdf ➡️ Description of what is requested for part 1 of the project;
- project_part_1.pdf ➡️ Resolution of part 1;
- Excels ➡️ Folder with the excels extracted from Kaggle;
- CSVs ➡️ Converted excels to CSVs;

🔵 **Part 2:**
- assignment_part_2.pdf ➡️ Description of what is requested for part 2 of the project;
- project_part_1.pdf ➡️ Resolution of part 1;
- project_part_2.pdf ➡️ Resolution of part 2;
- Disney.db ➡️ The database created in SQLiteStudio
- App:
	- static ➡️ Folder with css and an image that was used
	- templates ➡️ HTML files

<br></br>

## Database Configuration: 

Edit the `db.py` file regarding your DB configuration, modifying the `DB_FILE` parameters that indicate the database file. The SQLite file for DB must reside in the same folder as the `app.py` file.

Test access by running:
```bash 
python3 test_db_connection.py TABLE_NAME
```
If the DB access configuration is correct, the contents of the TABLE_NAME table should be listed, for example. the DB Disney Genre table:

```bash 
$ python3 test_db_connection.py Genre
connected <sqlite3.Connection object at 0x7f7a6d146120>
10 results ...
[('IdGenre', 1), ('Name', 'Comedy'), ('Description', 'Intended to be humorous or amusing by inducing laughter')]
[('IdGenre', 2), ('Name', 'Animation'), ('Description', 'A motion picture that is made from a series of drawings, computer graphics, or photographs of inanimate objects (such as puppets) and that simulates movement by slight progressive changes in each frame.')]
[('IdGenre', 3), ('Name', 'Action'), ('Description', 'Action film is\xa0a film genre in which the protagonist is thrust into a series of events that typically involve violence and physical feats.')]
[('IdGenre', 4), ('Name', 'Adventure'), ('Description', 'Characters often exploring places they have not been before or doing things they have not done before.')]
[('IdGenre', 5), ('Name', 'Drama'), ('Description', 'Involves conflicts, emotions, and the portrayal of human experiences through dialogue and action.')]
[('IdGenre', 6), ('Name', 'Musical'), ('Description', 'A film genre in which songs by the characters are interwoven into the narrative, sometimes accompanied by dancing')]
[('IdGenre', 7), ('Name', 'Romance'), ('Description', 'Focus on the relationship and romantic love between two people')]
[('IdGenre', 8), ('Name', 'Fantasy'), ('Description', 'Films that belong to the fantasy genre with fantastic themes, usually magic, supernatural events, mythology, folklore, or exotic fantasy worlds.')]
[('IdGenre', 9), ('Name', 'Mistery'), ('Description', 'A genre of film that revolves around the solution of a problem or a crime')]
[('IdGenre', 10), ('Name', 'Science Fiction'), ('Description', 'Uses speculative, fictional science-based depictions of phenomena that are not fully accepted by mainstream science, such as extraterrestrial lifeforms, spacecraft, robots, cyborgs, mutants...')]
```

<br></br>

## Running Program:

Access the terminal and make sure it is in the 'APP' directory to access it.
Run the command:
```bash 
python3 server.py
```
The following code will be displayed:
```bash 
$ python3 server.py 
connected <sqlite3.Connection object at 0x7fbadc57de40>
2025-01-22 19:30:37 - INFO - Connected to database
 * Serving Flask app 'app'
 * Debug mode: off
2025-01-22 19:30:37 - INFO - WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:9000
 * Running on http://172.23.245.160:9000
```
Then open in your browser http://127.0.0.1:9000 or http://172.23.245.160:9000

<br></br>

## Link to the course: 

This course is part of the **<u>first semester</u>** of the **<u>second year</u>** of the **<u>Bachelor's Degree in Artificial Intelligence and Data Science</u>** at **<u>FCUP</u>** and **<u>FEUP</u>** in the academic year 2023/2024. You can find more information about this course at the following link:

<div style="display: flex; flex-direction: column; align-items: center; gap: 10px;">
  <a href="https://sigarra.up.pt/fcup/pt/UCURR_GERAL.FICHA_UC_VIEW?pv_ocorrencia_id=529854">
    <img alt="Link to Course" src="https://img.shields.io/badge/Link_to_Course-0077B5?style=for-the-badge&logo=logoColor=white" />
  </a>

  <div style="display: flex; gap: 10px; justify-content: center;">
    <a href="https://sigarra.up.pt/fcup/pt/web_page.inicial">
      <img alt="FCUP" src="https://img.shields.io/badge/FCUP-808080?style=for-the-badge&logo=logoColor=grey" />
    </a>
    <a href="https://sigarra.up.pt/feup/pt/web_page.inicial">
      <img alt="FEUP" src="https://img.shields.io/badge/FEUP-808080?style=for-the-badge&logo=logoColor=grey" />
    </a>
  </div>
</div>
