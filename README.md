💧 Smart water dispensing System

The Smart water dispensing System is a smart web-based application developed using Django (Python) that allows users to conveniently order water and make secure digital payments through QR code scanning. This project aims to automate the water dispensing process and reduce manual effort by integrating web technology with digital payments and future IoT support.

Users can select the required quantity of water in liters through a simple and user-friendly interface. Based on the selected quantity, the system automatically calculates the total amount and generates a dynamic UPI QR code. The user can scan this QR code using any UPI-enabled application such as Google Pay, PhonePe, or Paytm to complete the payment. Once the payment is completed, the system updates the order status and proceeds further.

The system is designed with scalability in mind and includes API endpoints that can be integrated with hardware devices like automated water taps or valves. After successful payment verification, the system can trigger the hardware to dispense water, making it suitable for smart water distribution systems.

---

Features

- Online water ordering based on required quantity
- Dynamic QR code generation for UPI payments
- Secure and simple payment process
- Order status tracking (paid / unpaid / dispensed)
- API support for hardware integration
- Clean and responsive user interface

---

Technologies Used

- Backend: Django (Python)
- Frontend: HTML, CSS
- Database: MySQL
- API: Django REST Framework
- QR Code Generation: Python `qrcode` library

---

Project Structure

Water_project/
│
├── manage.py
├── MySQL
│
├── water_project/
│ ├── settings.py
│ ├── urls.py
│
├── water_app/
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│
├── templates/
│ ├── home.html
│ ├── order.html
│ ├── payment.html
│ ├── success.html
│
├── static/
│ └── images/

Installation & Setup

Clone the repository and navigate into the project directory:

```bash
git clone https://github.com/your-username/water-supply-project.git
cd water-supply-project

Create and activate a virtual environment:

python -m venv venv
venv\Scripts\activate

Install required dependencies:

pip install django djangorestframework pymysql qrcode[pil]

Configure MySQL database in settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'water_db',
        'USER': 'root',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

Apply migrations and start the server:

python manage.py makemigrations
python manage.py migrate
python manage.py runserver

#Open in browser:

http://127.0.0.1:8000/

System Workflow
User visits the website and places a water order
System calculates total amount based on liters
QR code is generated for payment
User scans and completes payment using UPI
System updates payment status
Water dispensing process can be triggered via API
Order is marked as completed
