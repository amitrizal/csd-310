import pymysql

# Establish database connection
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='Nitika1994',  # Replace with your actual password
    database='BacchusWinery'
)

# Report 1: Supplier Performance Report
def supplier_performance_report():
    query = """
    SELECT Name AS SupplierName, ExpectedDeliveryDate, ActualDeliveryDate,
           DATEDIFF(ActualDeliveryDate, ExpectedDeliveryDate) AS DelayInDays
    FROM Suppliers
    WHERE ActualDeliveryDate > ExpectedDeliveryDate;
    """
    with connection.cursor() as cursor:
        cursor.execute(query)
        results = cursor.fetchall()
        print("Supplier Performance Report:")
        for row in results:
            print(row)

# Report 2: Wine Sales Report
def wine_sales_report():
    query = """
    SELECT Wines.Name AS WineName, SalesVolume, Distributors.Name AS DistributorName
    FROM Wines
    JOIN Distributors ON Wines.DistributorID = Distributors.DistributorID
    ORDER BY SalesVolume DESC;
    """
    with connection.cursor() as cursor:
        cursor.execute(query)
        results = cursor.fetchall()
        print("\nWine Sales Report:")
        for row in results:
            print(row)

# Report 3: Employee Productivity Report
def employee_productivity_report():
    query = """
    SELECT Name AS EmployeeName, Role, SUM(QuarterlyHours) AS TotalHoursWorked
    FROM Employees
    GROUP BY EmployeeID
    ORDER BY TotalHoursWorked DESC;
    """
    with connection.cursor() as cursor:
        cursor.execute(query)
        results = cursor.fetchall()
        print("\nEmployee Productivity Report:")
        for row in results:
            print(row)

# Run all reports
if __name__ == "__main__":
    try:
        supplier_performance_report()
        wine_sales_report()
        employee_productivity_report()
    finally:
        connection.close()
