# Tardis Toolkit

## Overview

**Tardis Toolkit** is a specialized two-in-one tool designed to streamline and enhance your Date Time calculations. Whether you need to calculate the difference between now and a user-input time across various time zones or add/subtract days from an entered date, Tardis Toolkit provides a fast, intuitive, and efficient solution.

## Why Tardis?

- **Efficiency**: Paste your date and time directly into the text field, and Tardis will automatically parse it, saving you time and reducing errors.
  
- **Convenience**: Instantly copy the result of your calculations with a single click for easy reference and documentation.

- **Flexibility**: Currently, you can select from 4 predefined time zones, with future updates planned to allow for the addition of new ones.

- **Precision**: Get the exact information you need in a streamlined manner, making your workflow smoother and more effective.

## Features

1. **Time Difference Calculator**
   - Calculate the time difference between the current time and a user-specified datetime across multiple time zones.
   - Automatic parsing of pasted date and time strings.
   - Supports 4 predefined time zones (additional zones coming soon).

2. **Add/Subtract Days Tool**
   - Easily add or subtract days from a specified date.
   - Intuitive interface with an on/off toggle to switch between adding and subtracting days.

## Installation

### Backend (FastAPI)

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/tardis-toolkit.git
   cd tardis-toolkit
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

### Frontend (React)

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install the required dependencies:
   ```bash
   npm install
   ```

3. Start the React development server:
   ```bash
   npm start
   ```

4. The React app should now be running at `http://localhost:3000`.

## Usage

- **Access the Toolkit**: Visit `http://localhost:3000` in your browser to start using the Tardis Toolkit.
- **Calculate Time Difference**: Select a time zone, paste your datetime string, and hit submit to get the time difference.
- **Add/Subtract Days**: Navigate to the 'Add/Subtract Days' page, enter your date, toggle the action (add or subtract), and see your result instantly.

## Future Enhancements

- **Custom Time Zones**: Soon, you'll be able to add and manage your own time zones.
- **Dark Mode**: A dark mode option with a smooth toggle is on the roadmap.

## Contributing

We welcome contributions! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-name`).
6. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

