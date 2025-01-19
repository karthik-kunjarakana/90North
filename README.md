Apologies for the confusion. Here's a tailored **README.md** based on your end submission:

```markdown
# Chat Application with Responsive Webpage and AWS Integration

## Project Overview
This project is a complete chat application with a responsive front end, built using Django and JavaScript. The project includes essential features like user authentication, real-time chat through WebSocket, and integration with AWS Lambda for number addition and file storage in S3. It also features a dynamically responsive layout for a better user experience across different screen sizes.

## Key Features

### Frontend Features
1. **Responsive Design**:
   - A fixed navbar that remains in place while scrolling.
   - Three main sections: a collapsible left menu, a central content area, and a right-side panel.
   - A footer fixed at the bottom of the page.

2. **Collapsible Left Menu**:
   - Displays all registered users who can be selected for chat.

3. **Page Shrinkage on Resize**:
   - Page shrinks dynamically based on the screen width:
     - 992px to 1600px: Shrink by 90%.
     - 700px to 767px: Shrink by 80%.
     - 600px to 700px: Shrink by 75%.
     - 600px or below: Shrink by 50%.

### Django Backend
1. **User Authentication**:
   - Users can sign up and log in.
   - All users are displayed in a collapsible menu.

2. **Chat Interface**:
   - Users can select another user to start a chat.
   - Real-time chat is enabled via WebSocket.
   - Old messages are displayed when opening a chat.

3. **Database**:
   - All user data and chat messages are stored in the database.

### AWS Integration
1. **Lambda Function for Number Addition**:
   - A Lambda function that adds two numbers and returns the result.

2. **Lambda Function for File Upload**:
   - A Lambda function to store documents or PDFs in an S3 bucket.

## Installation and Setup

### Step 1: Clone the Repository
Clone the repository to your local machine:

```bash
git clone https://github.com/karthik-kunjarakana/90North
```

### Step 2: Install Dependencies
Navigate to the project folder and install the required dependencies.


### Step 3: Set Up the Database
Run the migrations to set up the database:

```bash
python manage.py migrate
```

### Step 4: Create a Superuser (For Admin Access)
To access the Django admin panel, create a superuser:

```bash
python manage.py createsuperuser
```

### Step 5: Run the Development Server
Start the development server:

```bash
python manage.py runserver
```

You can access the application at `http://127.0.0.1:8000/`.
And Also Hosted on **PythonAnywhere** `https://karthikkunjarakana.pythonanywhere.com/`.

## Deployment

### PythonAnywhere / AWS Deployment
1. Host the project on **PythonAnywhere** or **AWS**.
2. Follow the respective hosting platform’s guides to configure and deploy the app.

- For **PythonAnywhere**, set up a new web app and link the project.
- For **AWS**, use EC2 or Elastic Beanstalk to deploy the project.

## Submission
1. Code has been pushed to the GitHub repository.
2. README file has been included for setup and instructions.
3. Hosted the Django project (including frontend) on PythonAnywhere/AWS.
4. GitHub repository URL and hosted link have been shared with `Hr@enfund.io`.



## Acknowledgments
- [Django Framework](https://www.djangoproject.com/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket)
```
