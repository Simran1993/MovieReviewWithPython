# Using MongoDB with Python: A Web Catalog Implementation

**Course Code (CST8276-010)**  
**Submitted to:** Professor Douglas King  
**Team Members:**  
- Kunal Sharma (041102881)  
- Prabjot Singh (041102644)  
- Harsimran Singh (041100738)  
- Rohit Sharma (041103208)  
- Balraj Singh (041078071)  
- Parteek Singh (041102157)  

## Content
1. [Introduction](#introduction)  
   - [Topic Description](#topic-description)  
   - [Why We Chose This Topic](#why-we-chose-this-topic)  
2. [Problem Description](#problem-description-background-and-context)  
   - [Who: Who Cares and Who Does it Affect](#who-who-cares-and-who-does-it-affect)  
   - [What: What is the Data Aspect of the Issue](#what-what-is-the-data-aspect-of-the-issue)  
   - [Where: Location](#where-location-client-side-replication-server-capacity-etc)  
   - [When: Timing Considerations](#when-timing-considerations)  
   - [Why: Compliance with Laws, Regulations, or Other Constraints](#why-compliance-with-laws-regulations-or-other-constraints)  
   - [How: How Does the Problem Occur and Are It Fixed?](#how-how-does-the-problem-occur-and-are-it-fixed)  
3. [Solution Description & Results](#solution-description--results)  
   - [Solution Demonstration](#solution-demonstration)  
     - [What You Did for the Solution](#what-you-did-for-the-solution)  
     - [Components, Scripts, Database Setup, etc.](#components-scripts-database-setup-etc)  
     - [Screenshots and Details](#screenshots-and-details)  
4. [Work Plan](#work-plan)  
   - [Table with Components and Deliverables](#table-with-components-and-deliverables)  
     - [Detailed Breakdown](#detailed-breakdown)  
5. [Lessons Learned](#lessons-learned)  
   - [Risks That Needed to be Mitigated](#risks-that-needed-to-be-mitigated)  
   - [Overall Experience](#overall-experience)  
6. [References](#references)  
7. [Appendix](#appendix)  

## Introduction

Data management has become a cornerstone of modern web applications, especially in an era dominated by user-generated content. With the rise of platforms for reviews, discussions, and feedback, managing diverse, large-scale data efficiently is a growing challenge. Relational databases do not have significant issues, but current unstructured and dynamic data’s requirements of scale, schema, and performance are difficult to manage by relational databases.

This is where NoSQL databases like MongoDB dive into the game. The fact is, MongoDB is schema-less and offers enormous flexibility for handling both different data formats, as well as high-performance operations at the scale. Our project leverages MongoDB and Python to build a feature-rich movie review platform. Using Flask, a lightweight and extensible web framework, we aim to develop an intuitive interface that enables users to perform full CRUD (Create, Read, Update, Delete) operations on movie reviews.

The interaction between web-app and MongoDB is bridged by PyMongo, a powerful package to integrate the application, ensuring effective querying and data manipulation. Flask’s modular architecture facilitates seamless integration of RESTful APIs, ensuring scalability and compatibility with modern web standards. This platform is designed to showcase the potential of combining MongoDB's dynamic data handling capabilities with Python’s robust ecosystem. The result is an efficient, scalable, and user-friendly application tailored for real-time movie review management and exploration.

### Why We Chose This Topic

There are ample reasons which made us choose this topic:

- **Data Management:** The ever-increasing complexity and speed of data in modern applications demand scalable and flexible solutions that traditional relational databases struggle to provide as businesses produce and evaluate large amounts of data, so MongoDB with Python is the best approach to management and modernization.  
- **Skill Development:** Implementing Flask in this project with the integration of a cloud-based database will surely widen our prospects in terms of web development. Moreover, this project helps to improve our technical knowledge regarding MongoDB and programming in Python.  
- **Team Collaboration:** Python is the most common asynchronous language used these days, as we know it's efficient in AI-related logic building and data management.  
- **Efficient Data Storage:** MongoDB’s design of not being concerned with the definition of the schema makes it less important to use several joins as well as normalization which slow down most traditional databases.  
- **Data Variety:** A unique approach to data storage, such as MongoDB where other data types such as nested JSON documents can be stored, makes perfect sense when working with Python which also supports complex data models.  

## Problem Description (Background and Context)

### 1. Scalability Issues  
- **Problem:** Traditional relational databases (RDBMS) often face challenges with horizontal scalability, making it hard to manage large data volumes and high traffic.  
- **Impact:** This results in difficulties distributing data across multiple servers, leading to reduced performance as data and user activity increase.  

### 2. Complex Data Models  
- **Problem:** Web catalogs require flexible and dynamic data models, which are hard to achieve with the fixed schema of RDBMS.  
- **Impact:** Inability to adapt to changes in data structure increases management complexity and reduces efficiency.  

### Who: Who Cares and Who Does it Affect  
- **Individuals:** Movie enthusiasts who value a smooth and intuitive experience for reading and writing reviews.  
- **Business Owners/Managers:** Ultimately, website owners who intend to obtain more visitors/consumers and keep them coming back.  
- **Developers and IT Teams:** The IT staff that needs to maintain and grow the back end of the business.  

### What: What is the Data Aspect of the Issue  
- We're dealing with tons of stuff here - movie info, user reviews, ratings, viewing habits, etc.  
- MongoDB handles this messy data very effectively, storing it in a way that makes sense and is easy to work with.  

### Where: Location  
- **Client-side problem:** Delivering a responsive and visually appealing interface for users to browse, search, and submit reviews.  
- **Server-side problem:** Handling the API calls for searching and posting reviews while maintaining availability.  

### Why: Compliance with Laws, Regulations, or Other Constraints  
- **User Consent:** Clear opt-in mechanisms for collecting review data and personal information.  
- **Data Access Rights:** Users can request their review history and personal data.  

### How: How Does the Problem Occur and Are It Fixed?  
- **Problem:** Lack of ORM (Object Relational Mapping) is designed for SQL-based databases, not NoSQL-based databases.  
- **Mitigation:** Flask has no default ORM, allowing it to work directly with MongoDB using the powerful library PyMongo.  

## Solution Description & Results  

### Solution Demonstration  

#### What You Did for the Solution  
We implemented the Flask Framework based on Python and used PyMongo, a powerful module to interact between MongoDB and the web application.  

#### Steps:  
1. **Environment Setup:**  
   - Python virtual environment was activated to install required libraries.  
   - MongoDB cloud-based service (Atlas) was used.  

   ![Environment Setup](Figure_1_Environment_setup.png)  

2. **Database Design:**  
   - Schema-less model to improve code readability.  

   ![User Model](Figure_3_User_model.png)  

3. **Data Insertion:**  
   - Routes mapped to handle data storage.  

   ![Sample Data](Figure_4_sample_data.png)  

4. **API Integration:**  
   - Utilized an API library to fetch real-time movie data.  

5. **CRUD Operations:**  
   - Users can search, write, update, and delete reviews.  

   ![Delete Route](Figure_5_delete_route.png)  

#### Components, Scripts, Database Setup  
- **Database:** MongoDB Atlas with collections for users, reviews, and profiles.  
- **Indexes:** Created to improve query performance.  

   ![Indexing](Figure_11_Indexing.png)  

- **Aggregation:** Used for complex queries.  

   ![Aggregation](Figure_12_Aggregation.png)  

#### Screenshots and Details  
- **Registration Form:**  

   ![Registration Form](Figure_15_Registration_form.png)  

- **Login Form:**  

   ![Login Form](Figure_17_Login_form.png)  

- **Home Page:**  

   ![Homepage](Figure_19_Homepage.png)  

## Work Plan  

| Component/Deliverable Name | Time Period    | Hours Expected per Person | Names                     |  
|---------------------------|---------------|--------------------------|---------------------------|  
| Architecture Discussion    | Week 2-3      | 15                       | All members               |  
| Configuring API and Atlas  | Week 3-4      | 12                       | Kunal, Harsimran          |  

## Lessons Learned  

### Risks That Needed to be Mitigated  
- **Database Setup Error:** Debugged connection strings and verified network settings.  
- **API Configuration Error:** Implemented error-handling logic.  

### Overall Experience  
The project provided hands-on experience with MongoDB, Flask, and PyMongo, enhancing our understanding of NoSQL databases and web development.  

## References  
1. Gulshan, "What is a collection in MongoDB?," GeeksforGeeks. [Online]. Available: [https://www.geeksforgeeks.org/what-is-a-collection-in-mongodb/](https://www.geeksforgeeks.org/what-is-a-collection-in-mongodb/)  
2. Admin, "Indexes," MongoDB. [Online]. Available: [https://www.mongodb.com/docs/manual/indexes/](https://www.mongodb.com/docs/manual/indexes/)  

## Appendix  
### Acronyms Used  
- **API (Application Interface):** Set of rules for software communication.  
- **MONGO_URI:** Connection string for MongoDB.  
