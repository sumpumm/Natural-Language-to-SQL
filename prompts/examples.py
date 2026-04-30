data = [
    {
        "input": "Get all customers",
        "result": "SELECT * FROM customers;"
    },
    {
        "input": "Get all products with their names and prices",
        "result": "SELECT productname, buyprice FROM products;"
    },
    {
        "input": "Find all customers from USA",
        "result": "SELECT * FROM customers WHERE country = 'USA';"
    },
    {
        "input": "List all orders with their order date",
        "result": "SELECT ordernumber, orderdate FROM orders;"
    },
    {
        "input": "Count total number of customers",
        "result": "SELECT COUNT(*) FROM customers;"
    },
    {
        "input": "Find total number of orders",
        "result": "SELECT COUNT(*) FROM orders;"
    },
    {
        "input": "Get customers sorted by credit limit descending",
        "result": "SELECT customername, creditlimit FROM customers ORDER BY creditlimit DESC;"
    },
    {
        "input": "Find top 5 most expensive products",
        "result": "SELECT productname, buyprice FROM products ORDER BY buyprice DESC LIMIT 5;"
    },
    {
        "input": "Get total payments made by each customer",
        "result": "SELECT customernumber, SUM(amount) AS total_payment FROM payments GROUP BY customernumber;"
    },
    {
        "input": "Find average product price by product line",
        "result": "SELECT productline, AVG(buyprice) AS avg_price FROM products GROUP BY productline;"
    },
    {
        "input": "List orders along with customer names",
        "result": "SELECT o.ordernumber, c.customername FROM orders o JOIN customers c ON o.customernumber = c.customernumber;"
    },
    {
        "input": "Find total quantity ordered per product",
        "result": "SELECT productcode, SUM(quantityordered) AS total_quantity FROM orderdetails GROUP BY productcode;"
    },
    {
        "input": "Get customers who have made payments greater than 10000",
        "result": "SELECT DISTINCT c.customername FROM customers c JOIN payments p ON c.customernumber = p.customernumber WHERE p.amount > 10000;"
    },
    {
        "input": "Find total revenue per order",
        "result": "SELECT ordernumber, SUM(quantityordered * priceeach) AS revenue FROM orderdetails GROUP BY ordernumber;"
    },
    {
        "input": "Find top 5 customers by total spending",
        "result": "SELECT c.customername, SUM(p.amount) AS total_spent FROM customers c JOIN payments p ON c.customernumber = p.customernumber GROUP BY c.customername ORDER BY total_spent DESC LIMIT 5;"
    },
    {
        "input": "Get the most ordered product",
        "result": "SELECT productcode, SUM(quantityordered) AS total_quantity FROM orderdetails GROUP BY productcode ORDER BY total_quantity DESC LIMIT 1;"
    },
    {
        "input": "Find employees and the number of customers they manage",
        "result": "SELECT e.employeenumber, e.firstname, COUNT(c.customernumber) AS total_customers FROM employees e LEFT JOIN customers c ON e.employeenumber = c.salesrepemployeenumber GROUP BY e.employeenumber, e.firstname;"
    },
    {
        "input": "Find customers who have not made any payments",
        "result": "SELECT c.customername FROM customers c LEFT JOIN payments p ON c.customernumber = p.customernumber WHERE p.customernumber IS NULL;"
    },
    {
        "input": "Find monthly revenue",
        "result": "SELECT DATE_TRUNC('month', paymentdate) AS month, SUM(amount) AS revenue FROM payments GROUP BY month ORDER BY month;"
    },
    {
        "input": "Find most profitable order based on product margin",
        "result": "SELECT o.ordernumber, SUM((od.priceeach - p.buyprice) * od.quantityordered) AS profit FROM orders o JOIN orderdetails od ON o.ordernumber = od.ordernumber JOIN products p ON od.productcode = p.productcode GROUP BY o.ordernumber ORDER BY profit DESC LIMIT 1;"
    },
    {
        "input": "Find customers whose total payments exceed their credit limit",
        "result": "SELECT c.customername, SUM(p.amount) AS total_paid, c.creditlimit FROM customers c JOIN payments p ON c.customernumber = p.customernumber GROUP BY c.customername, c.creditlimit HAVING SUM(p.amount) > c.creditlimit;"
    }
]