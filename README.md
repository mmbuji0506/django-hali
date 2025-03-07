# Global Weather Dashboard

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Description

The **Global Weather Dashboard** is a web-based application that allows users to search and view weather information for cities around the world. It provides real-time weather data, including temperature, humidity, wind speed, pressure, and more. The dashboard is built with Django and integrates the OpenWeatherMap API to fetch live weather updates.

## Features

- **Search Functionality:** Users can search for weather data by entering a city name.
- **Real-Time Weather Data:** Displays temperature, humidity, wind speed, pressure, and weather description.
- **Detailed City Information:** Provides additional information like a local time clock.
- **Light/Dark Mode:** Toggle between light and dark themes for a personalized experience.
- **Responsive Design:** Optimized for various devices, including desktops, tablets, and mobile phones.

## Installation

Follow these steps to install and run the project:

### Prerequisites

Ensure you have the following installed on your system:
- Python (3.x recommended)
- Django
- Virtualenv (optional but recommended)

### Steps to Install

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mmbuji0506/Django-Global-Weather-News.git
   cd global-weather
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows use `env\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   - Create a `.env` file in the project root.
   - Add your OpenWeatherMap API key:
     ```
     OPENWEATHERMAP_API_KEY="bd5e378503939ddaee76f12ad7a97608"
     ```

5. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```
   The application should now be running at `http://127.0.0.1:8000/`.

## Usage

1. Open the application in your browser.
2. Enter a city name in the search bar.
3. View the real-time weather information displayed on the dashboard.
4. Switch between light and dark mode for a personalized experience.

## Technologies Used

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Weather API:** OpenWeatherMap API

## Contributing

Contributions are welcome! Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`
3. Make your changes and commit them: `git commit -m 'Add new feature'`
4. Push to the branch: `git push origin feature-branch`
5. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenWeatherMap API for providing weather data.
- Django documentation and community for development support.

## Contact

For any inquiries or suggestions, feel free to reach out:

- **Email:** mmbujijosameneza@gmail.com

+255 716 399 739/747 330 049

- **GitHub:** [mmbuji0506](https://github.com/mmbuji0506)

---

Happy coding! 🚀

