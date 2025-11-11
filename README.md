\# AI Business Idea Generator



A professional SaaS application that generates creative business startup ideas using AI, built with React and FastAPI.



\## Table of Contents



\- \[Features](#features)

\- \[Tech Stack](#tech-stack)

\- \[Project Structure](#project-structure)

\- \[Prerequisites](#prerequisites)

\- \[Installation](#installation)

\- \[Running the Application](#running-the-application)

\- \[API Documentation](#api-documentation)

\- \[Deployment](#deployment)

\- \[Contributing](#contributing)

\- \[License](#license)



\## Features



\### Core Features



\- \*\*User Authentication\*\*: Secure sign-up and login functionality

\- \*\*AI-Powered Idea Generation\*\*: Generate business ideas based on keywords and industry

\- \*\*Business Plan Details\*\*: Each idea includes title, description, business model, target audience, SWOT analysis, and market potential

\- \*\*Idea Management\*\*: Save, favorite, and organize generated ideas

\- \*\*Search History\*\*: Track all previous idea generation searches

\- \*\*Analytics Dashboard\*\*: View statistics and trends of your generated ideas

\- \*\*Professional UI\*\*: Beautiful blue and white design with responsive layout

\- \*\*PDF Export\*\*: Download business plans as PDF documents



\### Business Focus Areas



\- \*\*Finance\*\*: Financial technology and investment platforms

\- \*\*Education\*\*: EdTech and learning solutions

\- \*\*Social\*\*: Community and social impact businesses



\## Tech Stack



\### Frontend

\- \*\*React 18\*\*: Modern JavaScript UI library

\- \*\*Tailwind CSS\*\*: Utility-first CSS framework

\- \*\*Lucide React\*\*: Beautiful icon library

\- \*\*Axios\*\*: HTTP client for API requests

\- \*\*React Router\*\*: Client-side routing



\### Backend

\- \*\*FastAPI\*\*: Modern Python web framework

\- \*\*SQLAlchemy\*\*: SQL toolkit and ORM

\- \*\*PostgreSQL\*\*: Relational database

\- \*\*Pydantic\*\*: Data validation using Python type annotations

\- \*\*Python-Jose\*\*: JWT token handling

\- \*\*Passlib\*\*: Password hashing and verification



\### Additional Tools

\- \*\*Uvicorn\*\*: ASGI server for FastAPI

\- \*\*ReportLab\*\*: PDF generation library

\- \*\*Python-dotenv\*\*: Environment variable management



\## Project Structure



```

ai-business-idea-generator/

├── frontend/                      # React application

│   ├── public/

│   ├── src/

│   │   ├── App.js                # Main application component

│   │   ├── index.js              # Application entry point

│   │   └── index.css             # Global styles

│   ├── package.json

│   └── README.md

│

├── backend/                       # FastAPI application

│   ├── app/

│   │   ├── api/                  # API route handlers

│   │   │   ├── auth.py           # Authentication endpoints

│   │   │   ├── ideas.py          # Idea generation endpoints

│   │   │   ├── pdf.py            # PDF export endpoints

│   │   │   └── analytics.py      # Analytics endpoints

│   │   ├── core/

│   │   │   └── config.py         # Configuration settings

│   │   ├── db/

│   │   │   └── database.py       # Database connection

│   │   ├── models/

│   │   │   └── models.py         # SQLAlchemy models

│   │   ├── schemas/

│   │   │   └── schemas.py        # Pydantic schemas

│   │   ├── services/

│   │   │   ├── auth\_service.py   # Authentication logic

│   │   │   ├── ai\_service.py     # AI/idea generation logic

│   │   │   ├── pdf\_service.py    # PDF generation logic

│   │   │   └── db\_service.py     # Database operations

│   │   ├── main.py               # FastAPI application

│   │   └── \_\_init\_\_.py           # Package initialization

│   ├── run.py                    # Development server runner

│   ├── requirements.txt          # Python dependencies

│   └── .env                      # Environment variables

│

├── .env                          # Root environment file

├── .gitignore

└── README.md                     # This file

```



\## Prerequisites



\### System Requirements

\- Python 3.8 or higher

\- Node.js 14 or higher

\- PostgreSQL 12 or higher

\- Git



\### Tools Needed

\- Command Prompt or PowerShell

\- Text editor (VS Code recommended)

\- Postman (optional, for API testing)



\## Installation



\### Step 1: Clone Repository

```bash

git clone https://github.com/yourusername/ai-business-idea-generator.git

cd ai-business-idea-generator

```



\### Step 2: Setup Backend



\#### 2.1 Create Virtual Environment

```bash

cd backend

python -m venv venv

```



\#### 2.2 Activate Virtual Environment

```bash

\# Windows Command Prompt

venv\\Scripts\\activate



\# Windows PowerShell

venv\\Scripts\\Activate.ps1



\# Mac/Linux

source venv/bin/activate

```



\#### 2.3 Install Dependencies

```bash

pip install -r requirements.txt

```



\#### 2.4 Setup Environment Variables

Create `.env` file in backend folder:

```

DATABASE\_URL=postgresql://ai\_admin:admin123@localhost:5432/ai\_idea\_generator

OPENAI\_API\_KEY=sk-proj-your-key-here

SECRET\_KEY=your-secret-key-here

ALGORITHM=HS256

ACCESS\_TOKEN\_EXPIRE\_MINUTES=10080

ENVIRONMENT=development

DEBUG=True

BACKEND\_PORT=8000

FRONTEND\_PORT=3000

```



\#### 2.5 Create PostgreSQL Database

```bash

psql -U postgres

```



Inside PostgreSQL:

```sql

CREATE USER ai\_admin WITH PASSWORD 'admin123';

CREATE DATABASE ai\_idea\_generator OWNER ai\_admin;

GRANT ALL PRIVILEGES ON DATABASE ai\_idea\_generator TO ai\_admin;

\\q

```



\### Step 3: Setup Frontend



\#### 3.1 Navigate to Frontend

```bash

cd ../frontend

```



\#### 3.2 Install Dependencies

```bash

npm install

```



\#### 3.3 Create Environment File

Create `.env` file in frontend folder:

```

REACT\_APP\_API\_URL=http://localhost:8000

```



\## Running the Application



\### Terminal 1: Run Backend

```bash

cd backend

venv\\Scripts\\activate

python run.py

```



Expected output:

```

INFO:     Uvicorn running on http://0.0.0.0:8000

INFO:     Application startup complete

```



\### Terminal 2: Run Frontend

```bash

cd frontend

npm start

```



Expected output:

```

Compiled successfully!

You can now view frontend in the browser at http://localhost:3000

```



\### Access the Application

\- \*\*Frontend\*\*: http://localhost:3000

\- \*\*Backend\*\*: http://localhost:8000

\- \*\*API Docs\*\*: http://localhost:8000/docs



\### Test Login

\- \*\*Username\*\*: Ram

\- \*\*Password\*\*: 123



\## API Documentation



\### Authentication Endpoints



\#### Register User

```

POST /api/v1/auth/register

Content-Type: application/json



{

&nbsp; "username": "newuser",

&nbsp; "email": "user@example.com",

&nbsp; "password": "password123"

}



Response: 201 Created

{

&nbsp; "id": 1,

&nbsp; "username": "newuser",

&nbsp; "email": "user@example.com",

&nbsp; "is\_active": true,

&nbsp; "created\_at": "2025-11-09T10:00:00"

}

```



\#### Login

```

POST /api/v1/auth/login?username=Ram\&password=123



Response: 200 OK

{

&nbsp; "access\_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",

&nbsp; "token\_type": "bearer"

}

```



\### Idea Generation Endpoints



\#### Generate Business Ideas

```

POST /api/v1/ideas/generate

Authorization: Bearer {access\_token}

Content-Type: application/json



{

&nbsp; "keywords": "AI + Education",

&nbsp; "industry": "EdTech",

&nbsp; "num\_ideas": 2

}



Response: 200 OK

\[

&nbsp; {

&nbsp;   "id": 1,

&nbsp;   "title": "AI-Powered EdTech Platform",

&nbsp;   "description": "An innovative education solution using AI...",

&nbsp;   "business\_model": "SaaS subscription model...",

&nbsp;   "target\_audience": "Tech-savvy students and professionals",

&nbsp;   "swot\_analysis": "Strengths: Advanced AI...",

&nbsp;   "market\_potential": "Growing market...",

&nbsp;   "industry": "EdTech",

&nbsp;   "keywords": "AI + Education",

&nbsp;   "is\_favorite": false,

&nbsp;   "created\_at": "2025-11-09T10:00:00",

&nbsp;   "user\_id": 1

&nbsp; }

]

```



\#### Get User Ideas

```

GET /api/v1/ideas/?skip=0\&limit=10

Authorization: Bearer {access\_token}



Response: 200 OK

\[{idea\_objects}]

```



\#### Get Specific Idea

```

GET /api/v1/ideas/{idea\_id}

Authorization: Bearer {access\_token}



Response: 200 OK

{idea\_object}

```



\#### Toggle Favorite

```

POST /api/v1/ideas/{idea\_id}/favorite

Authorization: Bearer {access\_token}



Response: 200 OK

{

&nbsp; "idea": {idea\_object},

&nbsp; "is\_favorite": true

}

```



\#### Delete Idea

```

DELETE /api/v1/ideas/{idea\_id}

Authorization: Bearer {access\_token}



Response: 200 OK

{"message": "Idea deleted successfully"}

```



\### PDF Export Endpoints



\#### Export Single Idea to PDF

```

GET /api/v1/pdf/export/{idea\_id}

Authorization: Bearer {access\_token}



Response: 200 OK

(PDF file download)

```



\#### Export Multiple Ideas to PDF

```

POST /api/v1/pdf/export-multiple

Authorization: Bearer {access\_token}

Content-Type: application/json



{

&nbsp; "idea\_ids": \[1, 2, 3]

}



Response: 200 OK

(PDF file download)

```



\### Analytics Endpoints



\#### Get User Analytics

```

GET /api/v1/analytics/user

Authorization: Bearer {access\_token}



Response: 200 OK

{

&nbsp; "total\_ideas": 5,

&nbsp; "favorite\_ideas": 2,

&nbsp; "user\_id": 1,

&nbsp; "search\_history": \[...]

}

```



\#### Get Platform Analytics

```

GET /api/v1/analytics/platform

Authorization: Bearer {access\_token}



Response: 200 OK

{

&nbsp; "total\_users": 10,

&nbsp; "total\_ideas": 50,

&nbsp; "popular\_industries": \[...]

}

```



\## Deployment



\### Option 1: Docker Deployment



\#### Step 1: Create Dockerfile for Backend

```dockerfile

FROM python:3.9-slim



WORKDIR /app



COPY backend/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt



COPY backend/ .



CMD \["python", "run.py"]

```



\#### Step 2: Create Dockerfile for Frontend

```dockerfile

FROM node:16-alpine AS build

WORKDIR /app

COPY frontend/package.json package-lock.json ./

RUN npm install

COPY frontend/ .

RUN npm run build



FROM nginx:alpine

COPY --from=build /app/build /usr/share/nginx/html

EXPOSE 80

CMD \["nginx", "-g", "daemon off;"]

```



\#### Step 3: Create docker-compose.yml

```yaml

version: '3.8'



services:

&nbsp; db:

&nbsp;   image: postgres:13

&nbsp;   environment:

&nbsp;     POSTGRES\_USER: ai\_admin

&nbsp;     POSTGRES\_PASSWORD: admin123

&nbsp;     POSTGRES\_DB: ai\_idea\_generator

&nbsp;   ports:

&nbsp;     - "5432:5432"

&nbsp;   volumes:

&nbsp;     - postgres\_data:/var/lib/postgresql/data



&nbsp; backend:

&nbsp;   build: ./backend

&nbsp;   ports:

&nbsp;     - "8000:8000"

&nbsp;   environment:

&nbsp;     DATABASE\_URL: postgresql://ai\_admin:admin123@db:5432/ai\_idea\_generator

&nbsp;     OPENAI\_API\_KEY: ${OPENAI\_API\_KEY}

&nbsp;     SECRET\_KEY: ${SECRET\_KEY}

&nbsp;   depends\_on:

&nbsp;     - db



&nbsp; frontend:

&nbsp;   build: ./frontend

&nbsp;   ports:

&nbsp;     - "3000:80"

&nbsp;   depends\_on:

&nbsp;     - backend



volumes:

&nbsp; postgres\_data:

```



\#### Step 4: Build and Run with Docker

```bash

docker-compose up -d

```



\### Option 2: Heroku Deployment



\#### Step 1: Install Heroku CLI

```bash

npm install -g heroku

heroku login

```



\#### Step 2: Create Heroku App

```bash

heroku create your-app-name

```



\#### Step 3: Add PostgreSQL Add-on

```bash

heroku addons:create heroku-postgresql:hobby-dev

```



\#### Step 4: Set Environment Variables

```bash

heroku config:set OPENAI\_API\_KEY=your-key

heroku config:set SECRET\_KEY=your-secret

```



\#### Step 5: Deploy

```bash

git push heroku main

```



\### Option 3: AWS Deployment



Refer to AWS documentation for:

\- EC2 instances for backend

\- S3 for frontend hosting

\- RDS for PostgreSQL database

\- CloudFront for CDN



\## Project Summary for Resume



\### Project Title

\*\*AI Business Idea Generator - Full Stack SaaS Application\*\*



\### Project Description

Developed a comprehensive SaaS application that leverages artificial intelligence to generate creative and viable business startup ideas. Users can search by keywords and industry, receive detailed business plans, and track their idea generation history with analytics.



\### Key Responsibilities

\- Designed and implemented responsive React frontend with Tailwind CSS

\- Built RESTful API backend using FastAPI with JWT authentication

\- Implemented PostgreSQL database with SQLAlchemy ORM

\- Created PDF export functionality for business plans

\- Developed user analytics and search history tracking

\- Integrated mock AI data generation for proof of concept

\- Deployed application with Docker containerization



\### Technologies Used

\- \*\*Frontend\*\*: React, Tailwind CSS, Lucide React, Axios

\- \*\*Backend\*\*: FastAPI, SQLAlchemy, PostgreSQL, Pydantic

\- \*\*Authentication\*\*: JWT tokens, bcrypt password hashing

\- \*\*DevOps\*\*: Docker, Docker Compose, Git



\### Key Features Implemented

1\. User authentication with secure password hashing

2\. AI-powered business idea generation with customizable parameters

3\. CRUD operations for idea management

4\. Advanced analytics dashboard with trends and statistics

5\. PDF export for business plans

6\. Search history tracking and analysis

7\. Responsive UI with professional design

8\. RESTful API with comprehensive documentation



\### Impact

\- Demonstrates full-stack development capabilities

\- Shows understanding of modern web architecture

\- Implements security best practices (JWT, password hashing)

\- Showcases database design and optimization

\- Provides scalable foundation for future enhancements



\### GitHub Repository Link

```

https://github.com/yourusername/ai-business-idea-generator

```



\## Contributing



Contributions are welcome! Please follow these steps:



1\. Fork the repository

2\. Create a feature branch (`git checkout -b feature/AmazingFeature`)

3\. Commit your changes (`git commit -m 'Add some AmazingFeature'`)

4\. Push to the branch (`git push origin feature/AmazingFeature`)

5\. Open a Pull Request



\## License



This project is licensed under the MIT License - see the LICENSE file for details.



\## Contact



For questions or support, please contact:

\- Email: your.email@example.com

\- GitHub: @yourusername

\- LinkedIn: your-linkedin-profile



\## Acknowledgments



\- FastAPI documentation and community

\- React best practices and patterns

\- Tailwind CSS for beautiful styling

\- All open-source contributors

