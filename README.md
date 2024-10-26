# design-pattern-practice
## Banking System Assignment
### Problem Statement:
You are tasked with building a simplified banking system for a bank. The system should follow OOP principles, adhere to SOLID design principles, and utilize appropriate Design Patterns. The system will allow customers to manage bank accounts, process transactions, and handle different types of accounts (e.g., savings, checking). Your solution should demonstrate Encapsulation, Abstraction, Inheritance, and Polymorphism, as well as follow SOLID principles and incorporate Design Patterns where applicable.

### Requirements:
#### Bank Account Types:
- There should be different types of bank accounts such as Savings Account and Checking Account.
- Each account type should have specific features like:
- Savings accounts accrue interest.
- Checking accounts allow overdrafts.

#### Transaction Handling:
- Customers can deposit, withdraw, and transfer money between accounts.
- Each transaction should be logged.

#### Interest Calculation:
- For savings accounts, interest should be calculated periodically.
- The interest rate may vary between different savings accounts.

#### Notifications:
- Implement a notification system that informs customers when a transaction is completed.
- Notification types can be email or SMS.

#### SOLID Principles:
- Single Responsibility: Each class should have a single responsibility.
- Open/Closed: The system should be open for extension but closed for modification (e.g., adding new account types).
- Liskov Substitution: Subtypes must be substitutable for their base types.
- Interface Segregation: Clients should not be forced to depend on methods they do not use (e.g., notifications).
- Dependency Inversion: High-level modules should not depend on low-level modules. Use abstraction to decouple dependencies (e.g., use an interface for notifications).

#### Design Patterns:
- Factory Pattern to create bank accounts.
- Observer Pattern for the notification system.
- Strategy Pattern for interest calculation in savings accounts.
- Adapter Pattern for external payment gateway integration (e.g., transferring funds to another bank).