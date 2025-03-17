# **Case Study: Bank Account Management Using OOP**

## **Objective**  
This case study explores Object-Oriented Programming (OOP) concepts such as **instance methods, class methods, and static methods** using a **Bank Account Management System**.

---

## **Scenario**  
A bank offers different types of accounts (**Savings, Current**). Customers can:  
✅ Open an account  
✅ Deposit money  
✅ Withdraw money  
✅ Transfer money between accounts  
✅ Check their balance  
✅ View transaction history  

Additionally, the bank tracks:  
✅ The **total number of accounts**  
✅ A **transaction log** for each account  

---

## **Concepts Used**
- **Instance Methods**: Perform actions specific to an account (deposit, withdraw, transfer, check balance).  
- **Class Methods**: Keep track of the total number of accounts.  
- **Static Methods**: Validate inputs before performing operations.  

---

## **Tasks**
### **1️⃣ Basic Understanding Tasks**
- [ ] **Task 1:** Explain the difference between instance methods, class methods, and static methods.  
- [ ] **Task 2:** Identify and explain the use of `self`, `cls`, and `@staticmethod` in the given code.  
- [ ] **Task 3:** Modify the `BankAccount` class to print a message whenever a new account is created.  

### **2️⃣ Feature Enhancement Tasks**
- [ ] **Task 4:** Implement a transaction fee of ₹10 per withdrawal.  
- [ ] **Task 5:** Implement a `transfer` method to send money between accounts.  
- [ ] **Task 6:** Add an account type (`Savings` or `Current`) and ensure **minimum balance for Savings Accounts**.  
- [ ] **Task 7:** Implement an **interest calculation** feature where Savings Accounts earn **5% annual interest**.  

### **3️⃣ Validation & Error Handling Tasks**
- [ ] **Task 8:** Reject deposits or withdrawals greater than ₹50,000 (fraud prevention).  
- [ ] **Task 9:** Prevent withdrawals if the account balance would become **negative**.  
- [ ] **Task 10:** Ensure that the **account holder’s name** is not empty when creating a new account.  

### **4️⃣ Advanced Tasks (OOP Enhancements)**
- [ ] **Task 11:** Convert `BankAccount` into a **parent class** and create `SavingsAccount` and `CurrentAccount` as subclasses.  
- [ ] **Task 12:** Store all transactions (deposits, withdrawals, transfers) in a **list** and implement a `get_transaction_history()` method.  
- [ ] **Task 13:** Maintain a **log of all accounts** using a class variable.  

### **5️⃣ Unit Testing & UI Tasks**
- [ ] **Task 14:** Write **unit tests** for deposit, withdrawal, and transfer functions.  
- [ ] **Task 15:** Implement a **CLI interface** to allow users to create accounts and perform transactions.  

---


