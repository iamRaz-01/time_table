# Ex03 Time Table
# Date: 26 / 11 / 2024
# AIM
To write a html webpage page to display your slot timetable.

# ALGORITHM
## STEP 1
Create a Django-admin Interface.

## STEP 2
Create a static folder and inert HTML code.

## STEP 3
Create a simple table using `<table>` tag in html.

## STEP 4
Add header row using `<th>` tag.

## STEP 5
Add your timetable using `<td>` tag.

## STEP 6
Execute the program using runserver command.

# PROGRAM
### Settings.py 
```
import os
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'slot_time_table'
]
```

### Views.py
```
from django.http import HttpResponse

def timetable (request):
    host = request.get_host()
    port = host.split(':')[1]
    print(f'The server is running on the port {port}')
    print('GET request received...')
    html_content = """
          <!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        * {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        td {
            text-align: center;

        }

        .highlight {
            background-color: black;
            color: white;
        }
    </style>
</head>

<body>
    <div>
        <img src="https://raw.githubusercontent.com/iamRaz-01/Web-application-ex-pictures/refs/heads/main/Web%20Banner.png" alt="Banner" width="100%" height="150px">
        <div>
            <h1>Slot Time Table Abdul - 24901014 </h1>
            <table border="1px solid black ; font-family:">
                <tr class="highlight">
                    <th>Day/time</th>
                    <th>Monday</th>
                    <th>Tuesday</th>
                    <th>Wednesday</th>
                    <th>Thursday</th>
                    <th>Friday</th>
                    <th>Saturday</th>
                </tr>
                <tr>
                    <td class="highlight">8-10</td>
                    <td colspan="2">free slot</td>
                    <td>Maths</td>
                    <td>ML </td>
                    <td>ML </td>
                    <td>English</td>
                </tr>
                <tr>
                    <td class="highlight">10 - 12 </td>
                    <td>Web </td>
                    <td>Physics
                    </td>
                    <td>Eng</td>
                    <td>Maths</td>
                    <td>
                        free slot
                    </td>
                    <td>Maths</td>
                </tr>
                <tr>
                    <td class="highlight">12 - 1 </td>
                    <td colspan="6"> lunch </td>
                </tr>
                <tr>
                    <td class="highlight">1 - 3 </td>
                    <td> free slot </td>
                    <td>Mat</td>
                    <td>Mentor</td>
                    <td>web</td>
                    <td>free slot </td>
                    <td>Physics</td>
                </tr>
                <tr>
                    <td class="highlight">3 - 5 </td>
                    <td colspan="5"> free slot </td>

                    <td>Web </td>
                </tr>


            </table>
            <h2>Subject Code</h2>
            <table border="1px solid black ; font-family:">
                <tr class="highlight">
                    <th>Sno</th>
                    <th>Code</th>
                    <th>Subject Name</th>
                </tr>
                <tr>
                    <td class="highlight">1</td>
                    <td>19AI301C</td>
                    <td>Maths</td>
                </tr>
                <tr>
                    <td class="highlight">2</td>
                    <td>19AI410</td>
                    <td>Introduction to ML </td>
                </tr>
                <tr>
                    <td class="highlight">3</td>
                    <td>19AI414</td>
                    <td>Fundamentals of webapplication</td>
                </tr>
                <tr>
                    <td class="highlight">4</td>
                    <td>19EN101</td>
                    <td>English</td>
                </tr>
                <tr>
                    <td class="highlight">5</td>
                    <td>SH3214</td>
                    <td>physics</td>
                </tr>
            </table>

        </div>


    </div>
</body>

</html>
    """
    response = HttpResponse(html_content, status=200) 
    print(f'Status code {response.status_code}')
    print('HTML response sent successfully.')
    return response 
 
```

### App's urls.py
```
from django.urls import path
from .views import timetable

urlpatterns = [
    path('', timetable, name='timetable'),
]
```

### Project's urls.py 
```
from django.contrib import admin
from django.urls import path ,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('slot_time_table.urls')),
]
```

# OUTPUT
### Browser's Output 
![image](https://github.com/user-attachments/assets/a9b77dce-a2d7-4b9a-921d-b20a141e242f)

### Terminal's Output 
![image](https://github.com/user-attachments/assets/fe883f79-0c37-4a29-8991-6a046d3154a4)


# RESULT
The program for creating slot timetable using basic HTML tags is executed successfully.
