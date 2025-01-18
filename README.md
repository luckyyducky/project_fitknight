# FitKnight

FitKnight is a web platform designed to connect fitness enthusiasts, helping them find workout partners or create and manage fitness groups. Users can sign up as either a **Buddy Finder** or a **Group Organizer** for a personalized fitness experience.

## Features

### User Authentication
- Custom username and password-based authentication
- Profile picture upload with default option
- Role selection during signup: Buddy Finder or Group Organizer
- Personalized onboarding flow based on selected role

### Buddy Finder Portal
- Personalized dashboard with recommended workout partners
- Advanced filtering system for finding compatible workout buddies
- Access to available fitness groups
- Detailed profile management:
  - Personal information and fitness goals
  - Activity tracking and milestones
  - Customizable privacy settings
- Real-time notifications for group updates and join requests

### Group Portal
- Comprehensive group management dashboard
- Group creation and editing capabilities
- Member management system
- Join request handling
- Detailed group profiles including:
  - Activity schedules
  - Location information
  - Member listings
  - Organizer details

## Technical Stack
- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Database**: Django Default Database (SQLite)
- **Authentication**: Django Auth System
- **Media Handling**: Django File Storage
- **Static Files**: Django Static Files

**Note:** The files listed in the repository are organized in the same order as they appear in the project structure.

## Installation

Clone the repository:

```
git clone [repository-url]
cd fitknight
```
Create and activate a virtual environment:

```
python -m venv my-venv
source my-venv/bin/activate  # On Windows: my-venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Run migrations:

```
python manage.py migrate
```

Create a superuser:

```
python manage.py createsuperuser
```

Run the development server:

```
python manage.py runserver
```

