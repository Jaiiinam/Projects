CREATE TABLE Branch (
  Branch_id INT,
  Branch_city VARCHAR(255),
  Branch_postal_code VARCHAR(50),
  Assets REAL,
  PRIMARY KEY (Branch_id)
  
);


CREATE TABLE Employees (
  Employees_id INT,
  Employees_name VARCHAR(255),
  Employees_city VARCHAR(255),
  Employees_postal_code VARCHAR(10),
  Employees_email VARCHAR(255),
  Employees_phone VARCHAR(100),
  PRIMARY KEY (Employees_id)
);


CREATE TABLE Customers (
  customer_id INT,
  customer_name VARCHAR(255),
  customer_postal_code VARCHAR(10),
  customer_city VARCHAR(255),
  customer_phone_number VARCHAR(20),
  PRIMARY KEY (customer_id)
);


CREATE TABLE Account(
	Account_number VARCHAR(50),
	Account_type VARCHAR(50),
	Balance REAL,
	PRIMARY KEY (Account_number, Account_type)
);

CREATE TABLE Loan (
	Loan_id INT,
	Amount REAL,
	PRIMARY KEY (Loan_id)
);


CREATE TABLE Creditcard (
	Credit_card_number VARCHAR(50),
	Expiry_date DATE,
	Card_limit REAL,
	PRIMARY KEY (Credit_card_number)
);

CREATE TABLE Branch_employees(
	FK_Branch_id INT,
	FK_Employees_id INT,
	FOREIGN KEY(FK_Branch_id) REFERENCES Branch(Branch_id),
	FOREIGN KEY(FK_Employees_id) REFERENCES Employees(Employees_id)
		
);

CREATE TABLE Loan_provider_branch (
	FK_Branch_id INT,
	FK_Loan_id INT,
	Amount REAL,
	FOREIGN KEY(FK_Branch_id) REFERENCES Branch (Branch_id), 
	FOREIGN KEY(FK_Loan_id) REFERENCES Loan (Loan_id) 
);


CREATE TABLE Borrow (
	FK_Loan_id INT,
	FK_customer_id INT,
	FOREIGN KEY(FK_Loan_id) REFERENCES Loan(Loan_id), 
	FOREIGN KEY(FK_customer_id) REFERENCES Customers (customer_id)
);

CREATE TABLE Loan_payment_pending (
	FK_Loan_id INT,
	FK_customer_id INT,
	Amount REAL,
	FOREIGN KEY(FK_Loan_id) REFERENCES Loan(Loan_id),
	FOREIGN KEY(FK_customer_id) REFERENCES Customers (customer_id)
);

CREATE TABLE Money_deposit(
	FK_customer_id INT,
	FK_Account_number VARCHAR(50),
	FK_Account_type VARCHAR(20),
	Deposit_amount REAL,
	FOREIGN KEY(FK_customer_id) REFERENCES Customers (customer_id),
	FOREIGN KEY(FK_account_number) REFERENCES Account (Account_number),
	FOREIGN KEY(FK_Account_type) REFERENCES Account (Account_type)
);

CREATE TABLE Has_credit_card (
	FK_Account_number VARCHAR(255),
	FK_credit_card_number VARCHAR(50),
	FOREIGN KEY(FK_account_number) REFERENCES Account (Account_number),
	FOREIGN KEY(FK_credit_card_number) REFERENCES Creditcard(Credit_card_number)
);

CREATE TABLE Has_account (
	FK_Account_number VARCHAR(255),
	FK_customer_id INT,
	FOREIGN KEY(FK_account_number) REFERENCES Account (Account_number),
	FOREIGN KEY(FK_customer_id) REFERENCES Customers(customer_id)
);