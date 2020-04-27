 
SELECT customer_name
FROM Customers
WHERE customer_id IN (SELECT FK_customer_id FROM Money_deposit);


SELECT FK_account_number,sum(deposit_amount) AS Total_deposit
FROM Money_deposit 
GROUP BY deposit_amount;



SELECT customer_name, COUNT(Deposit_amount), FK_Account_type
FROM Customers, Money_deposit 
WHERE Customers.customer_id = Money_deposit.FK_customer_id
GROUP BY Deposit_amount;



SELECT customer_id,customer_name,customer_postol_code,customer_city,customer_phone_number
FROM Customers, Has_account
WHERE (Customers.customer_id IN (Has_account.FK_customer_id)) AND ((Has_account.FK_Account_number) IN (SELECT FK_account_number FROM Has_credit_card));


SELECT Branch_id, COUNT(Employees_id)
FROM Branch_employees, Branch, Employees
WHERE (Branch.Branch_id = (Branch_employees.FK_Branch_id)) AND (Employees.Employees_id = (Branch_employees.FK_Employees_id))
GROUP BY (Branch_id);


