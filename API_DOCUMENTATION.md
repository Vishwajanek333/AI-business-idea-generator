\# API Documentation



Complete API reference for AI Business Idea Generator



\## Base URL

```

http://localhost:8000

```



\## Production URL

```

https://your-app-name.herokuapp.com

```



\## Authentication



All protected endpoints require Bearer token in Authorization header:

```

Authorization: Bearer {access\_token}

```



Get token from login endpoint.



---



\## Authentication Endpoints



\### 1. Register New User



\*\*Endpoint\*\*: `POST /api/v1/auth/register`



\*\*Description\*\*: Create a new user account



\*\*Request Body\*\*:

```json

{

&nbsp; "username": "newuser",

&nbsp; "email": "user@example.com",

&nbsp; "password": "securepassword123"

}

```



\*\*Success Response\*\* (201 Created):

```json

{

&nbsp; "id": 1,

&nbsp; "username": "newuser",

&nbsp; "email": "user@example.com",

&nbsp; "is\_active": true,

&nbsp; "created\_at": "2025-11-09T10:00:00.000000"

}

```



\*\*Error Response\*\* (400 Bad Request):

```json

{

&nbsp; "detail": "Username already registered"

}

```



\*\*cURL Example\*\*:

```bash

curl -X POST http://localhost:8000/api/v1/auth/register \\

&nbsp; -H "Content-Type: application/json" \\

&nbsp; -d '{

&nbsp;   "username": "newuser",

&nbsp;   "email": "user@example.com",

&nbsp;   "password": "securepassword123"

&nbsp; }'

```



---



\### 2. Login User



\*\*Endpoint\*\*: `POST /api/v1/auth/login`



\*\*Description\*\*: Authenticate user and receive access token



\*\*Query Parameters\*\*:

\- `username` (string, required): Username

\- `password` (string, required): Password



\*\*Success Response\*\* (200 OK):

```json

{

&nbsp; "access\_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJuZXd1c2VyIiwiZXhwIjoxNzMxMTI3MjAwfQ.XXXXX",

&nbsp; "token\_type": "bearer"

}

```



\*\*Error Response\*\* (401 Unauthorized):

```json

{

&nbsp; "detail": "Invalid username or password"

}

```



\*\*cURL Example\*\*:

```bash

curl -X POST "http://localhost:8000/api/v1/auth/login?username=Ram\&password=123"

```



---



\### 3. Verify Token



\*\*Endpoint\*\*: `POST /api/v1/auth/verify-token`



\*\*Description\*\*: Check if a token is valid



\*\*Query Parameters\*\*:

\- `token` (string, required): JWT token to verify



\*\*Success Response\*\* (200 OK):

```json

{

&nbsp; "valid": true,

&nbsp; "username": "Ram"

}

```



\*\*Error Response\*\* (401 Unauthorized):

```json

{

&nbsp; "detail": "Invalid token"

}

```



---



\## Ideas Endpoints



\### 1. Generate Business Ideas



\*\*Endpoint\*\*: `POST /api/v1/ideas/generate`



\*\*Description\*\*: Generate new business ideas using AI



\*\*Authentication\*\*: Required (Bearer token)



\*\*Request Body\*\*:

```json

{

&nbsp; "keywords": "AI, Machine Learning, Education",

&nbsp; "industry": "EdTech",

&nbsp; "num\_ideas": 3

}

```



\*\*Response Fields\*\*:

\- `keywords` (string): Search keywords

\- `industry` (string): Target industry

\- `num\_ideas` (integer): Number of ideas to generate (1-10)



\*\*Success Response\*\* (200 OK):

```json

\[

&nbsp; {

&nbsp;   "id": 1,

&nbsp;   "title": "AI-Powered EdTech Platform",

&nbsp;   "description": "An innovative education solution using AI...",

&nbsp;   "business\_model": "SaaS subscription model with tiered pricing...",

&nbsp;   "target\_audience": "Tech-savvy students and professionals",

&nbsp;   "swot\_analysis": "Strengths: Advanced AI, user-friendly interface...",

&nbsp;   "market\_potential": "The global AI market is projected to reach...",

&nbsp;   "industry": "EdTech",

&nbsp;   "keywords": "AI, Machine Learning, Education",

&nbsp;   "is\_favorite": false,

&nbsp;   "created\_at": "2025-11-09T10:00:00.000000",

&nbsp;   "user\_id": 1

&nbsp; }

]

```



\*\*Error Response\*\* (401 Unauthorized):

```json

{

&nbsp; "detail": "Not authenticated"

}

```



\*\*Error Response\*\* (500 Internal Server Error):

```json

{

&nbsp; "detail": "Error generating ideas: {error message}"

}

```



\*\*cURL Example\*\*:

```bash

curl -X POST http://localhost:8000/api/v1/ideas/generate \\

&nbsp; -H "Authorization: Bearer {access\_token}" \\

&nbsp; -H "Content-Type: application/json" \\

&nbsp; -d '{

&nbsp;   "keywords": "AI, Education",

&nbsp;   "industry": "EdTech",

&nbsp;   "num\_ideas": 2

&nbsp; }'

```



---



\### 2. Get User Ideas



\*\*Endpoint\*\*: `GET /api/v1/ideas/`



\*\*Description\*\*: Retrieve all ideas created by current user



\*\*Authentication\*\*: Required (Bearer token)



\*\*Query Parameters\*\*:

\- `skip` (integer, optional, default=0): Number of records to skip

\- `limit` (integer, optional, default=10): Maximum records to return



\*\*Success Response\*\* (200 OK):

```json

\[

&nbsp; {

&nbsp;   "id": 1,

&nbsp;   "title": "AI-Powered EdTech Platform",

&nbsp;   "description": "...",

&nbsp;   "business\_model": "...",

&nbsp;   "target\_audience": "...",

&nbsp;   "swot\_analysis": "...",

&nbsp;   "market\_potential": "...",

&nbsp;   "industry": "EdTech",

&nbsp;   "keywords": "AI, Education",

&nbsp;   "is\_favorite": false,

&nbsp;   "created\_at": "2025-11-09T10:00:00.000000",

&nbsp;   "user\_id": 1

&nbsp; }

]

```



\*\*cURL Example\*\*:

```bash

curl -X GET "http://localhost:8000/api/v1/ideas/?skip=0\&limit=10" \\

&nbsp; -H "Authorization: Bearer {access\_token}"

```



---



\### 3. Get Specific Idea



\*\*Endpoint\*\*: `GET /api/v1/ideas/{idea\_id}`



\*\*Description\*\*: Retrieve a specific idea by ID



\*\*Authentication\*\*: Required (Bearer token)



\*\*Path Parameters\*\*:

\- `idea\_id` (integer, required): ID of the idea



\*\*Success Response\*\* (200 OK):

```json

{

&nbsp; "id": 1,

&nbsp; "title": "AI-Powered EdTech Platform",

&nbsp; "description": "...",

&nbsp; "business\_model": "...",

&nbsp; "target\_audience": "...",

&nbsp; "swot\_analysis": "...",

&nbsp; "market\_potential": "...",

&nbsp; "industry": "EdTech",

&nbsp; "keywords": "AI, Education",

&nbsp; "is\_favorite": false,

&nbsp; "created\_at": "2025-11-09T10:00:00.000000",

&nbsp; "user\_id": 1

}

```



\*\*Error Response\*\* (404 Not Found):

```json

{

&nbsp; "detail": "Idea not found"

}

```



\*\*cURL Example\*\*:

```bash

curl -X GET http://localhost:8000/api/v1/ideas/1 \\

&nbsp; -H "Authorization: Bearer {access\_token}"

```



---



\### 4. Toggle Favorite Idea



\*\*Endpoint\*\*: `POST /api/v1/ideas/{idea\_id}/favorite`



\*\*Description\*\*: Mark/unmark idea as favorite



\*\*Authentication\*\*: Required (Bearer token)



\*\*Path Parameters\*\*:

\- `idea\_id` (integer, required): ID of the idea



\*\*Success Response\*\* (200 OK):

```json

{

&nbsp; "idea": {

&nbsp;   "id": 1,

&nbsp;   "title": "AI-Powered EdTech Platform",

&nbsp;   "...": "..."

&nbsp; },

&nbsp; "is\_favorite": true

}

```



\*\*cURL Example\*\*:

```bash

curl -X POST http://localhost:8000/api/v1/ideas/1/favorite \\

&nbsp; -H "Authorization: Bearer {access\_token}"

```



---



\### 5. Delete Idea



\*\*Endpoint\*\*: `DELETE /api/v1/ideas/{idea\_id}`



\*\*Description\*\*: Delete an idea



\*\*Authentication\*\*: Required (Bearer token)



\*\*Path Parameters\*\*:

\- `idea\_id` (integer, required): ID of the idea



\*\*Success Response\*\* (200 OK):

```json

{

&nbsp; "message": "Idea deleted successfully"

}

```



\*\*Error Response\*\* (404 Not Found):

```json

{

&nbsp; "detail": "Idea not found"

}

```



\*\*cURL Example\*\*:

```bash

curl -X DELETE http://localhost:8000/api/v1/ideas/1 \\

&nbsp; -H "Authorization: Bearer {access\_token}"

```



---



\## PDF Export Endpoints



\### 1. Export Single Idea to PDF



\*\*Endpoint\*\*: `GET /api/v1/pdf/export/{idea\_id}`



\*\*Description\*\*: Download a business idea as PDF



\*\*Authentication\*\*: Required (Bearer token)



\*\*Path Parameters\*\*:

\- `idea\_id` (integer, required): ID of the idea to export



\*\*Success Response\*\* (200 OK):

```

\[PDF file content]

```



\*\*Headers\*\*:

```

Content-Type: application/pdf

Content-Disposition: attachment; filename="business\_plan\_1\_AI-Powered\_EdTech\_Platform.pdf"

```



\*\*Error Response\*\* (404 Not Found):

```json

{

&nbsp; "detail": "Idea not found"

}

```



\*\*cURL Example\*\*:

```bash

curl -X GET http://localhost:8000/api/v1/pdf/export/1 \\

&nbsp; -H "Authorization: Bearer {access\_token}" \\

&nbsp; -o business\_plan.pdf

```



---



\### 2. Export Multiple Ideas to PDF



\*\*Endpoint\*\*: `POST /api/v1/pdf/export-multiple`



\*\*Description\*\*: Download multiple ideas as single PDF



\*\*Authentication\*\*: Required (Bearer token)



\*\*Request Body\*\*:

```json

{

&nbsp; "idea\_ids": \[1, 2, 3]

}

```



\*\*Success Response\*\* (200 OK):

```

\[PDF file content]

```



\*\*Headers\*\*:

```

Content-Type: application/pdf

Content-Disposition: attachment; filename="business\_plans\_combined\_3\_ideas.pdf"

```



\*\*cURL Example\*\*:

```bash

curl -X POST http://localhost:8000/api/v1/pdf/export-multiple \\

&nbsp; -H "Authorization: Bearer {access\_token}" \\

&nbsp; -H "Content-Type: application/json" \\

&nbsp; -d '{"idea\_ids": \[1, 2, 3]}' \\

&nbsp; -o business\_plans.pdf

```



---



\## Analytics Endpoints



\### 1. Get User Analytics



\*\*Endpoint\*\*: `GET /api/v1/analytics/user`



\*\*Description\*\*: Get user's personal statistics



\*\*Authentication\*\*: Required (Bearer token)



\*\*Success Response\*\* (200 OK):

```json

{

&nbsp; "total\_ideas": 5,

&nbsp; "favorite\_ideas": 2,

&nbsp; "user\_id": 1,

&nbsp; "search\_history": \[

&nbsp;   {

&nbsp;     "keywords": "AI, Education",

&nbsp;     "industry": "EdTech",

&nbsp;     "num\_ideas": 3,

&nbsp;     "created\_at": "2025-11-09T10:00:00.000000"

&nbsp;   }

&nbsp; ]

}

```



\*\*cURL Example\*\*:

```bash

curl -X GET http://localhost:8000/api/v1/analytics/user \\

&nbsp; -H "Authorization: Bearer {access\_token}"

```



---



\### 2. Get Platform Analytics



\*\*Endpoint\*\*: `GET /api/v1/analytics/platform`



\*\*Description\*\*: Get platform-wide statistics



\*\*Authentication\*\*: Required (Bearer token)



\*\*Success Response\*\* (200 OK):

```json

{

&nbsp; "total\_users": 10,

&nbsp; "total\_ideas": 50,

&nbsp; "popular\_industries": \[

&nbsp;   {

&nbsp;     "industry": "EdTech",

&nbsp;     "count": 15

&nbsp;   },

&nbsp;   {

&nbsp;     "industry": "Finance",

&nbsp;     "count": 20

&nbsp;   }

&nbsp; ]

}

```



\*\*cURL Example\*\*:

```bash

curl -X GET http://localhost:8000/api/v1/analytics/platform \\

&nbsp; -H "Authorization: Bearer {access\_token}"

```



---



\## Error Handling



\### HTTP Status Codes



\- `200 OK`: Request successful

\- `201 Created`: Resource created successfully

\- `400 Bad Request`: Invalid request parameters

\- `401 Unauthorized`: Authentication required or failed

\- `404 Not Found`: Resource not found

\- `500 Internal Server Error`: Server error



\### Error Response Format



All error responses follow this format:

```json

{

&nbsp; "detail": "Error message describing what went wrong"

}

```



---



\## Rate Limiting



Currently no rate limiting is implemented. For production deployment, consider implementing:

\- User-based rate limiting

\- IP-based rate limiting

\- Request throttling



---



\## Pagination



Use `skip` and `limit` query parameters for pagination:

```

GET /api/v1/ideas/?skip=0\&limit=10

GET /api/v1/ideas/?skip=10\&limit=10

```



---



\## Testing with Postman



1\. Import requests into Postman

2\. Set `{{base\_url}}` variable to `http://localhost:8000`

3\. Set `{{token}}` variable with your access token

4\. Run requests using the provided cURL examples



---



\## Troubleshooting



\### Token Expired

Error: `Invalid or expired token`

Solution: Login again to get new token



\### Database Connection Error

Error: `Could not connect to database`

Solution: Verify PostgreSQL is running and connection string is correct



\### CORS Error

Error: `Access to XMLHttpRequest blocked by CORS policy`

Solution: Verify backend CORS settings include frontend URL



\### API Not Responding

Error: `Connection refused`

Solution: Verify backend is running on port 8000

