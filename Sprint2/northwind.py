import sqlite3
# import northwind_small.sqlite3
#
# data = northwind_small.sqlite3

con = sqlite3.connect('northwind_small.sqlite3')


def run_queries():
    expensive_items = 'SELECT * FROM Product ORDER BY UnitPrice DESC LIMIT 10;'
    '''[(38, 'Côte de Blaye', 18, 1, '12 - 75 cl bottles', 263.5, 17, 0, 15, 0), (29, 'Thüringer Rostbratwurst', 12, 6, '50 bags x 30 sausgs.', 123.79, 0, 0, 0, 1), (9, 'Mishi Kobe Niku', 4, 6, '18 - 500 g pkgs.', 97, 29, 0, 0, 1), (20, "Sir Rodney's Marmalade", 8, 3, '30 gift boxes', 81, 40, 0, 0, 0), (18, 'Carnarvon Tigers', 7, 8, '16 kg pkg.', 62.5, 42, 0, 0, 0), (59, 'Raclette Courdavault', 28, 4, '5 kg pkg.', 55, 79, 0, 0, 0), (51, 'Manjimup Dried Apples', 24, 7, '50 - 300 g pkgs.', 53, 20, 0, 10, 0), (62, 'Tarte au sucre', 29, 3, '48 pies', 49.3, 17, 0, 0, 0), (43, 'Ipoh Coffee', 20, 1, '16 - 500 g tins', 46, 17, 10, 25, 0), (28, 'Rössle Sauerkraut', 12, 7, '25 - 825 g cans', 45.6, 26, 0, 0, 1)]'''
    avg_hire_age = 'SELECT AVG(HireDate - BirthDate) FROM Employee;'
    '''[(37.22222222222222,)]'''
    top_10_expensive = ('SELECT ProductName, UnitPrice, CompanyName '
                        'FROM Product, Supplier WHERE SupplierId = Supplier.Id ' 
                        'ORDER BY Product.UnitPrice DESC LIMIT 10;')
    '''[('Côte de Blaye', 263.5, 'Aux joyeux ecclésiastiques'),
     ('Thüringer Rostbratwurst', 123.79, 'Plutzer Lebensmittelgroßmärkte AG'), ('Mishi Kobe Niku', 97, 'Tokyo Traders'),
     ("Sir Rodney's Marmalade", 81, 'Specialty Biscuits, Ltd.'), ('Carnarvon Tigers', 62.5, 'Pavlova, Ltd.'),
     ('Raclette Courdavault', 55, 'Gai pâturage'), ('Manjimup Dried Apples', 53, "G'day, Mate"),
     ('Tarte au sucre', 49.3, "Forêts d'érables"), ('Ipoh Coffee', 46, 'Leka Trading'),
     ('Rössle Sauerkraut', 45.6, 'Plutzer Lebensmittelgroßmärkte AG')]'''

    largest_category = ('SELECT CategoryName, COUNT(DISTINCT Product.Id) '
                        'FROM Category, Product WHERE Category.Id = CategoryId ' 
                        'GROUP BY 1 ORDER BY 2 DESC LIMIT 1;')
    '''[('Confections', 13)]'''
    queries = (expensive_items,avg_hire_age,top_10_expensive,largest_category)
    curs = con.cursor()
    for query in queries:
        print(curs.execute(query).fetchall())

if __name__ == "__main__":
  run_queries()
