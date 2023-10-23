# Project Structure Guide 
`- Concise Version`

This guide outlines the folder structure of our project, explaining the purpose behind each folder and the decisions made.

### .github/
For GitHub configurations, mainly GitHub Actions for tasks like CI/CD.

### assets/
Stores static assets for both frontend and backend. A local copy for quicker development, even though we use AWS S3.

### client/
Contains frontend code. A separate space for frontend development.

### database/
Holds database scripts and migrations. Essential for our AWS RDS setup.

### docs/
Where all our project documentation resides.

### events/
For configurations or scripts tied to CloudWatch Events or similar.

### infrastructure/
Contains scripts for AWS setup, like CloudFormation.

### lambdas/
For our AWS Lambda functions. Organized for scalability.

### scripts/
Utility scripts, including Python scrapers, are here.

### server/
For backend code. Separate from `lambdas` to cater to non-serverless tasks.

### tests/
All testing code is here, ensuring organized and accessible tests.

### .gitignore
Prevents certain files/folders, like node modules, from being committed.

### LICENSE
Dictates the project's licensing terms.

### README.md
The main introduction to the repository.

## Decisions & Trade-offs

- **Server vs. Lambdas**: We opted for both. While Lambdas handle most tasks, a traditional server setup is sometimes needed.
  
- **Assets Locally vs. S3**: We chose a local `assets` folder for quicker development, even with our AWS S3 setup.
  
- **Frontend & Backend Separation**: We separated them for clarity and modularity.

The structure is designed for clarity, organization, and scalability.

<br>
<br>
<br>

-------------------------------------------------

<br>
<br>
<br>

## A More Comprehensive Project Structure Explanation

### .github/
This directory is specifically tailored for GitHub-specific configurations. It primarily houses workflows for GitHub Actions, a CI/CD platform integrated within GitHub. By placing all GitHub-related configurations here, we ensure a centralized location for all automation tasks, making it easier for developers to locate and modify workflows as needed.

### assets/
The `assets` directory serves as a repository for static assets like images, stylesheets, and scripts that might be shared across both frontend and backend components. While AWS S3 is our primary storage solution for assets in a production environment, maintaining a local copy of these assets accelerates the development and testing phases, eliminating the need for constant uploads to S3 during these stages.

### client/
The `client` directory is dedicated to all frontend-related code. By isolating frontend code from backend components, we ensure a clear boundary between the two, facilitating easier navigation and development for frontend developers. It also aids in modularizing the application, making it more maintainable.

### database/
Our project leverages AWS RDS for database solutions. The `database` directory is pivotal in this context, containing all database-related scripts, migrations, and seed data. This organization ensures that any changes or additions to the database structure are easily traceable and manageable.

### docs/
Documentation is the backbone of any project, ensuring that developers, both current and future, understand the project's architecture, decisions, and workflows. The `docs` directory is a dedicated space for all project-related documentation, from setup guides to architectural decisions. Additionally, the `docs` directory contains subdirectories mirroring the main project structure, which will house detailed `.md` documents related to each specific component.

### events/
Event-driven architectures are becoming increasingly popular, especially with the rise of serverless computing. Our `events` directory is tailored for configurations or scripts related to AWS CloudWatch Events or any other event-driven mechanisms we might adopt. This separation ensures that event-related logic doesn't clutter the main application code.

### infrastructure/
With our heavy reliance on AWS for infrastructure, the `infrastructure` directory is crucial. It contains scripts and configurations for setting up and managing our AWS resources, be it through CloudFormation, Terraform, or any other Infrastructure as Code (IaC) tool we might use. This directory ensures that our infrastructure setup is version-controlled, organized, and easily replicable.

### lambdas/
Serverless computing, especially AWS Lambda, is at the heart of our backend. The `lambdas` directory is organized to house all our Lambda functions. By giving each function its sub-directory, we ensure that our structure remains scalable and manageable as we add more functions.

### scripts/
Utility scripts, especially those written in Python, find their home in the `scripts` directory. This includes scripts for data scraping, automation tasks, or any other utility functions that don't fit into the main application flow. By separating these scripts, we ensure clarity and prevent the main codebase from becoming cluttered.

### server/
While AWS Lambda handles a significant portion of our backend, there are tasks that might not be suitable for a serverless approach. The `server` directory is dedicated to such tasks, ensuring that any traditional server setup we might need is isolated and easily identifiable.

### tests/
Testing is non-negotiable for any software project. The `tests` directory is organized to contain all our testing code, be it unit tests, integration tests, or end-to-end tests. This organization ensures that tests are easily accessible, runnable, and maintainable.

### .gitignore
The `.gitignore` file is a crucial component of any Git-based project. It ensures that specific files or directories, especially those that are environment-specific or contain sensitive information, are not committed to the repository. This not only keeps the repository clean but also ensures security.

### LICENSE
Open-source or not, every project should clearly define its licensing terms. The `LICENSE` file provides this clarity, dictating how the project can be used, modified, and distributed.

### .gitkeep
While Git does not track empty directories, sometimes it's essential to commit them to maintain a desired project structure. The `.gitkeep` file, though not a standard Git feature, is a convention used to commit an otherwise empty directory. It's a placeholder file that can be added to any directory to ensure Git tracks it.

### README.md
The `README.md` file is often the first point of contact for anyone encountering the repository. It serves as an introduction, providing an overview of the project, setup instructions, and other crucial information.

## In-depth Decisions & Trade-offs

- **Server vs. Lambdas**: The decision to maintain both a traditional server setup alongside AWS Lambda functions was deliberate. While Lambdas are efficient for event-driven tasks and offer scalability, certain tasks, especially those requiring persistent connections or extensive resources, might be better suited for a traditional server setup.

- **Assets Locally vs. S3**: The choice to maintain a local `assets` directory, despite our use of AWS S3, was driven by the development lifecycle. Local assets ensure quicker iterations during development and testing, reducing the dependency on internet connectivity and S3 access.

- **Frontend & Backend Separation**: A clear separation between frontend (`client`) and backend (`server` and `lambdas`) components ensures modularity. This separation not only makes the development process clearer but also aids in scalability and maintainability.

In conclusion, our chosen structure is a testament to our commitment to clarity, organization, and scalability, ensuring that the project remains robust and maintainable as it grows.
