# Data Science Unit 3 Sprint Challenge 2
**IMPORTANT: Use the same name for files and variables that we use within this markdown** :)

## Databases and SQL

A SQL Query walks into a bar. In one corner of the bar are two tables. The Query
walks up to the tables and asks:

...

*"Mind if I join you?"*

---

In this sprint challenge you will write code and answer questions related to databases, with a focus on SQL but an acknowledgment of the broader ecosystem. You may use any tools and references you wish, but your final code should reflect *your* work and be saved in `.py` files (*not* notebooks), and, along with this file including your written answers, uploaded in the Sprint Challenge Submission in Canvas.

For all the code you write, you may only import/use the following:
- other modules you write
- `sqlite3` (from the standard library)

As always, make sure to manage your time - get a section/question to "good enough" and then move on to make sure you do everything. You can always revisit and refactor your code at the end if time allows.

If it helps, consider writing queries in DataGrip or another database browser first.  Once you have done that, copy/paste them into your Python script appropriately (using the exact query names).

Be aware that the *AutoTest functions do not work very well for this Sprint Challenge* and will not reflect your final, reviewed grade for this Sprint Challenge - your instructor or TA will also be reviewing all Sprint Challenges prior to Build Week.  If you think your queries are correct they are most likely correct!

This file is Markdown, so it may be helpful to open with PyCharm, VS Code, or another tool that allows you to view it nicely rendered.

Lastly, **do not forget to complete the Sprint Challenge assessment and retrospectives that go along with the Sprint Challenge!**

Good luck!

### Part 1 - Making and populating a Database

Consider the following data:

| s   | x | y |
|-----|---|---|
| 'g' | 3 | 9 |
| 'v' | 5 | 7 |
| 'f' | 8 | 7 |

Using the standard `sqlite3` module:

- Open a connection to a new (blank) database file `demo_data.sqlite3`
- Make a cursor, and execute an appropriate `CREATE TABLE` statement to accept
  the above data (name the table `demo`)
- Write and execute appropriate `INSERT INTO` statements to add the data (as
  shown above) to the database

Make sure to `commit()` so your data is saved! The file size should be non-zero.

Then write the following queries (also with `sqlite3`) to test the demo database and
save them under the following variables names (PLEASE use the **exact** names):

- `row_count`: Count how many rows you have - it should be 3!
- `xy_at_least_5`: How many rows are there where both `x` and `y` are at least 5?
- `unique_y`: How many unique values of `y` are there (hint - `COUNT()` can accept a keyword
  `DISTINCT`)?

Your code (to reproduce all above steps) should be saved in `demo_data.py` and
turned in along with the generated SQLite database.

### Part 2 - The Northwind Database

Using `sqlite3`, connect to the given `northwind_small.sqlite3` database.

![Northwind Entity-Relationship Diagram](./northwind_erd.png)

Above is an entity-relationship diagram - a picture summarizing the schema and relationships in the database. Note that it was generated using Microsoft
Access, and some of the specific table/field names are different in the provided data. You can see all the tables available to SQLite as follows:

```python
>>> curs.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY
name;").fetchall()
[('Category',), ('Customer',), ('CustomerCustomerDemo',),
('CustomerDemographic',), ('Employee',), ('EmployeeTerritory',), ('Order',),
('OrderDetail',), ('Product',), ('Region',), ('Shipper',), ('Supplier',),
('Territory',)]
```

*Warning*: unlike the diagram, the tables in SQLite are singular and not plural (do not end in `s`). And you can see the schema (`CREATE TABLE` statement) behind any given table with:
```python
>>> curs.execute('SELECT sql FROM sqlite_master WHERE name="Customer";').fetchall()
[('CREATE TABLE "Customer" \n(\n  "Id" VARCHAR(8000) PRIMARY KEY, \n
"CompanyName" VARCHAR(8000) NULL, \n  "ContactName" VARCHAR(8000) NULL, \n
"ContactTitle" VARCHAR(8000) NULL, \n  "Address" VARCHAR(8000) NULL, \n  "City"
VARCHAR(8000) NULL, \n  "Region" VARCHAR(8000) NULL, \n  "PostalCode"
VARCHAR(8000) NULL, \n  "Country" VARCHAR(8000) NULL, \n  "Phone" VARCHAR(8000)
NULL, \n  "Fax" VARCHAR(8000) NULL \n)',)]
```

In particular note that the *primary* key is `Id`, and not `CustomerId`. On other tables (where it is a *foreign* key) it will be `CustomerId`. Also note - the `Order` table conflicts with the `ORDER` keyword! We'll just avoid that particular table, but it's a good lesson in the danger of keyword conflicts.

Answer the following questions (each is from a single table) and then save each query under the following variable name (again, please use the **exact** name):

- `expensive_items`: What are the ten most expensive items (per unit price) in the database? Please return all columns in the table, not just the price and name but all columns.

SELECT Product.Id,ProductName,SupplierId,CategoryId,QuantityPerUnit,UnitPrice,UnitsInStock,UnitsOnOrder,ReorderLevel,Discontinued
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10

Id,ProductName,SupplierId,CategoryId,QuantityPerUnit,UnitPrice,UnitsInStock,UnitsOnOrder,ReorderLevel,Discontinued
38,Côte de Blaye,18,1,12 - 75 cl bottles,263.5,17,0,15,0
29,Thüringer Rostbratwurst,12,6,50 bags x 30 sausgs.,123.79,0,0,0,1
9,Mishi Kobe Niku,4,6,18 - 500 g pkgs.,97,29,0,0,1
20,Sir Rodney's Marmalade,8,3,30 gift boxes,81,40,0,0,0
18,Carnarvon Tigers,7,8,16 kg pkg.,62.5,42,0,0,0
59,Raclette Courdavault,28,4,5 kg pkg.,55,79,0,0,0
51,Manjimup Dried Apples,24,7,50 - 300 g pkgs.,53,20,0,10,0
62,Tarte au sucre,29,3,48 pies,49.3,17,0,0,0
43,Ipoh Coffee,20,1,16 - 500 g tins,46,17,10,25,0
28,Rössle Sauerkraut,12,7,25 - 825 g cans,45.6,26,0,0,1


- `avg_hire_age`: What is the average age of an employee at the time of their hiring? (Hint: a
  lot of arithmetic works with dates.)


- (*Stretch*) `avg_age_by_city`: How does the average age of employee at hire vary by city?


Your code (to load and query the data) should be saved in `northwind.py`, and added to the repository. Do your best to answer in purely SQL, but if necessary use Python/other logic to help.

### Part 3 - Sailing the Northwind Seas

You've answered some basic questions from the Northwind database, looking at individual tables - now it's time to put things together, and `JOIN`!

Using `sqlite3` in `northwind.py`, answer the following:

- `ten_most_expensive`: What are the ten most expensive items (per unit price) in the database *and* their suppliers? Please return all columns in the table, not just the price and name but all columns. The supplier should be the last column.

SELECT Product.Id,ProductName,SupplierId,CategoryId,QuantityPerUnit,UnitPrice,UnitsInStock,UnitsOnOrder,ReorderLevel,Discontinued,CompanyName
FROM Product
left join Supplier on Product.SupplierId = Supplier.Id
ORDER BY UnitPrice DESC
LIMIT 10

38,Côte de Blaye,18,1,12 - 75 cl bottles,263.5,17,0,15,0,Aux joyeux ecclésiastiques
29,Thüringer Rostbratwurst,12,6,50 bags x 30 sausgs.,123.79,0,0,0,1,Plutzer Lebensmittelgroßmärkte AG
9,Mishi Kobe Niku,4,6,18 - 500 g pkgs.,97,29,0,0,1,Tokyo Traders
20,Sir Rodney's Marmalade,8,3,30 gift boxes,81,40,0,0,0,"Specialty Biscuits, Ltd."
18,Carnarvon Tigers,7,8,16 kg pkg.,62.5,42,0,0,0,"Pavlova, Ltd."
59,Raclette Courdavault,28,4,5 kg pkg.,55,79,0,0,0,Gai pâturage
51,Manjimup Dried Apples,24,7,50 - 300 g pkgs.,53,20,0,10,0,"G'day, Mate"
62,Tarte au sucre,29,3,48 pies,49.3,17,0,0,0,Forêts d'érables
43,Ipoh Coffee,20,1,16 - 500 g tins,46,17,10,25,0,Leka Trading
28,Rössle Sauerkraut,12,7,25 - 825 g cans,45.6,26,0,0,1,Plutzer Lebensmittelgroßmärkte AG


- `largest_category`: What is the largest category (by number of unique products in it)?

- (*Stretch*) `most_territories`: Who's the employee with the most territories? Use `TerritoryId` (not name, region, or other fields) as the unique identifier for territories. You should be sure to include the employee id in the select statement and return all columns. 

### Part 4 - Questions (and your Answers)

Answer the following questions, baseline ~3-5 sentences each, as if they were interview screening questions (a form you fill when applying for a job):

- In the Northwind database, what is the type of relationship between the `Employee` and `Territory` tables?
	There isn't a direct relationship between them, but there is a Bridge table (EmployeeTerritory) that pulls in the EmployeeID's and the TerritoryID's. It appears that is used by the Territory table to align Employee ID's to a Territory, which aligns to the Region ID, and would allow the Region to be passed to the Employees table from the EmployeeID, but I don't know for sure without seeing the CREATE Tables if that's how that works. The Schema shows a circular relationship for Employees with itself.

- What is a situation where a document store (like MongoDB) is appropriate, and what is a situation where it is not appropriate?
	The only differentiation I know is important is based on the data types associated with NoSQL (documents) vs RDBMS (atomic|tabular|relational) SQL 		friendly data. Any usecase where you're scanning in large quantities of data in many different forms would need NoSQL in order to allow for the higher level 	grouping of the document types, contents, indexability of them, and then going beyond that into the capabilities to join and query them once they're 		somewhat manageable.

- What is "NewSQL", and what is it trying to achieve?
	It's attempting to be a merger of the Relational DB's ACID consistency, and the NoSQL's scalability for high transaction volumes/OLTP.
	However, it doesn't seem to matter as much as it says it does.

### Part 5 - Turn it in!
Provide all the files you wrote (`demo_data.py`, `northwind.py`, `demo_data.sqlite3`), as well as this file with your answers to part 4. To simplify the grading process, please include the output from your queries as docstring comments above your query variables. Thanks for your hard work!

If you got this far, check out the [larger Northwind database](https://github.com/jpwhite3/northwind-SQLite3/blob/master/Northwind_large.sqlite.zip) -
your queries should run on it as well, with richer results.
