# project_fitknight
FitKnight

FitKnight is a web platform that connects fitness enthusiasts, enabling them to find workout partners and join fitness groups. Users can choose to be either a Buddy Finder looking for workout partners or a Group Organizer creating and managing fitness groups.
Features

User Authentication

Custom username and password authentication
Profile picture upload with default options
Role selection during signup (Buddy Finder or Group Organizer)
Personalized onboarding flow based on user role

Buddy Finder Portal

Personalized dashboard with recommended workout partners
Advanced filtering system for finding compatible buddies
Access to available fitness groups
Detailed profile management

Personal information and fitness goals
Activity tracking and milestones
Customizable privacy settings


Real-time notifications for group updates

Group Portal

Comprehensive group management dashboard
Group creation and editing capabilities
Member management system
Join request handling
Detailed group profiles including:

Activity schedules
Location information
Member listings
Organizer details

Technical Stack

Backend: Django
Frontend: HTML, CSS, JavaScript, Bootstrap
Database: Django Default Database
Authentication: Django Auth System
Media Handling: Django File Storage
Static Files: Django Static Files

Installation

Clone the repository:

bashCopygit clone [repository-url]
cd fitknight

Create and activate a virtual environment:

bashCopypython -m venv my-venv
source my-venv/bin/activate  # On Windows: my-venv\Scripts\activate

Install dependencies:

bashCopypip install -r requirements.txt

Set up environment variables:
Create a .env file in the root directory and add:

CopyDEBUG=True
SECRET_KEY=your_secret_key
DATABASE_URL=your_database_url

Run migrations:

bashCopypython manage.py migrate

Create a superuser:

bashCopypython manage.py createsuperuser

Run the development server:

bashCopypython manage.py runserver
