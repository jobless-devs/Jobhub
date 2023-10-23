# 🌐 System Architecture Overview 🌐
`- Concise Version`

---

### 📌 TODO: add more details in the [Comprehensive Version](https://github.com/sbshaun/JobHub/blob/main/docs/docs/architecture-design.md#-system-architecture-overview--1) 
- add explanations to concepts 
- add links to readings/youtube tutorials

---

<img width="777" alt="JobHub-Architecture-Diagram" src="https://github.com/sbshaun/JobHub/assets/99154887/5de417cc-d087-41e0-9df4-b73d22a52128">

### 🛠️ Key Technical Terms/Techs 🛠️:
- **CloudWatch Events**: 🚨 A monitoring service that triggers a response from AWS resources based on preset rules.
- **Lambda**: 🚀 AWS service that lets you run code without provisioning or managing servers.
- **API Gateway**: 🚪 Fully managed service for creating, maintaining, and securing APIs.
- **Amazon Cognito**: 🔐 Provides authentication, authorization, and user management for web/mobile apps.
- **Step Functions**: 🔄 Coordinate multiple AWS services into serverless workflows.
- **S3 Bucket**: 📦 Scalable storage in the AWS Cloud.
- **AWS Glue ETL**: 🔄 Managed ETL (Extract, Transform, Load) service.
- **RDS (Relational Database Service)**: 🗃️ Managed relational database service.

## 🚶 Workflow Walkthrough 🚶:

1. **Initiation**: ⏰ A CloudWatch Event is triggered, prompting the `Job Scraper Lambda` function.
2. **Data Scraping**: 🕸️ `Job Scraper Lambda` extracts raw job data and stores it in an `S3 Bucket (Raw Job Data)`.
3. **Data Transformation**: 🛠️ `AWS Glue ETL` processes and transforms the raw data.
4. **Processed Data Storage**: 📂 The transformed data is stored in `S3 Bucket (Processed Job Results)`.
5. **User Interaction**: 🖥️ Users access the dashboard/API, interfacing with the system through `API Gateway`.
6. **Authorization**: 🔑 `Amazon Cognito` ensures authenticated and authorized access.
7. **Backend Processing**: ⚙️ `Backend Services Lambda` fetches the transformed job listings from the S3 bucket.
8. **Data Retrieval**: 🔍 The `Job Management Service` facilitates data retrieval, filtering, ranking, and presenting job opportunities via the `Job Evaluation Service`.
9. **Data Persistence**: 💾 The processed job listings are stored in `RDS`.

## 🤔 Decision Making, Suggestions, and Trade-offs 🤔:

### Decision Making:
- **AWS Ecosystem**: ☁️ We embraced AWS due to its scalability, robustness, and the suite of interconnected services it offers.
- **Serverless Architecture**: 🌩️ Leveraging Lambda and Step Functions, we can efficiently scale without managing servers.

### Suggestions:
- **DynamoDB Integration**: 📈 For a more flexible and scalable NoSQL database option, DynamoDB could be considered.
- **Real-time Notifications**: 📣 Integrating AWS SNS would enable real-time notifications for users, enhancing their experience.

### Trade-offs:
- **AWS Glue ETL vs. Custom ETL**: ⚖️ Opting for AWS Glue ETL offers manageability and scalability but may come at an increased cost. A custom ETL solution could offer more flexibility at the cost of development and maintenance time.
- **RDS vs. DynamoDB**: 🔄 While RDS provides structured data management with SQL capabilities, DynamoDB might be more scalable and flexible.

📢 We are continuously seeking feedback to make our architecture resilient, efficient, and user-centric. Your insights and expertise are invaluable as we embark on this journey to refine the job search process for co-op students and beyond. 🌟

------- 

<br>
<br>
<br>

# 🌟 System Architecture Overview 🌟
`- Comprehensive Version` 

Dive deeper into the architectural choices, the rationale behind them, and the broader landscape of our tech stack. 🚀

## 📚 Extended Technical Glossary 📚

### CloudWatch Events
An AWS monitoring tool that listens for system events and triggers automated protocol based on the event type. It's like our project's alarm clock, waking up other services when it's their turn to act.

### Lambda
Imagine writing code and not worrying about where or how it runs. That's the magic of AWS Lambda. It's our go-to for executing backend logic without the fuss of server management.

### API Gateway
The doorman of our system. API Gateway handles all the requests coming in and directs them to the right place, ensuring smooth interactions for our users.

### Amazon Cognito
Our security guard. Cognito makes sure that everyone who's trying to access our system is who they say they are. It's all about keeping things secure and user-friendly.

### Step Functions
Think of this as our project's choreographer, ensuring all AWS services dance in harmony. It sequences multiple services into a streamlined serverless workflow.

### S3 Bucket
Our project's treasure chest. S3 Buckets are where we store all our valuable data, from raw job listings to processed results.

### AWS Glue ETL
The chef of our project. It takes in raw data, cooks (transforms) it, and serves it in a more digestible format.

### RDS (Relational Database Service)
Our organized librarian. RDS keeps our processed job listings neatly cataloged and easy to retrieve.

## 🚶‍♂️ Deep Dive into the Workflow 🚶‍♂️

### Initiation
When the clock strikes (or when a specific event occurs), CloudWatch Events springs into action, signaling the Job Scraper Lambda to start its mission.

### Data Scraping
Our Job Scraper Lambda, like a modern-day treasure hunter, scours the web for job listings, collecting all the golden opportunities into our S3 Bucket.

### Data Transformation
Enter AWS Glue ETL, the master transformer. It refines and reshapes the raw data, making it more meaningful and structured.

### User Interaction
Our users, the heart of our project, interact with our system via a sleek dashboard/API. Behind the scenes, API Gateway ensures their requests are handled smoothly.

### Authorization
No unwanted guests allowed! Amazon Cognito checks every user's credentials, ensuring only authorized users get access.

### Backend Processing
The Backend Services Lambda is our backstage crew, fetching the right data at the right time from our S3 bucket.

### Data Retrieval
Our Job Management Service, the maestro, orchestrates the entire show, ensuring users get the best job opportunities tailored just for them.

### Data Persistence
All the refined job listings find a permanent home in RDS, ready to be retrieved whenever needed.

## 🤔 Decisions, Alternatives, and Future Paths 🤔

### AWS Ecosystem
Choosing AWS was like choosing a Swiss Army knife. It's versatile, reliable, and integrates seamlessly, making our project's journey smoother.

### Serverless Architecture
Why get bogged down with server management when AWS Lambda and Step Functions can handle the heavy lifting? It's all about being lean and efficient.

### DynamoDB Integration
While RDS is great, we're also eyeing DynamoDB. It's like the cool new kid on the block, offering flexibility and scalability in data management.

### Real-time Notifications
Imagine getting instant updates on job listings! Integrating AWS SNS is on our radar to make this dream a reality.

### Trade-offs
Every decision has its pros and cons. While AWS Glue ETL is powerful, it might be pricier. Custom ETL could be more flexible but needs more care. And the eternal debate: RDS or DynamoDB? Each has its charm.

🙌 We're on a mission to revolutionize the job search experience. Your feedback and insights are the compass guiding us forward. Let's make job hunting a breeze together! 🌬️🍃
