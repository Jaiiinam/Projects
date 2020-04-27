
INSERT INTO Customers(customer_id,customer_name,customer_postol_code,customer_city,customer_phone_number)  VALUES (115,"Yash","M1G398","Colchester","(416)615 9135");


UPDATE Creditcard set Card_limit = '500'
WHERE credit_card_number IN (SELECT FK_credit_card_number FROM Has_credit_card);


UPDATE Account set Balance = Balance  - 0.50 
WHERE Account_type = "Chequing" AND Balance = (SELECT Balance FROM Account WHERE (Balance < 5000));


DELETE FROM Loan_payment_pending WHERE FK_Loan_id = 71;



DELETE FROM Customers
WHERE Customers.customer_id NOT IN
  (SELECT FK_customer_id
   FROM Has_account);