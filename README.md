# REST API Automation Test
This repository contains automation tests for a REST API using both Python and JavaScript. The tests are designed to validate the behavior of the API endpoints and ensure that they meet the expected specifications.

Table of Contents
Overview
Prerequisites
Installation
Usage
Project Structure
Contributing
License
Overview
This project includes automated tests for a REST API that provides data based on specific parameters. The API requires a mandatory parameter symbol and an optional parameter date. The test cases cover various scenarios, including valid calls with different combinations of parameters and invalid calls without the required parameters.

Prerequisites
Before running the tests, ensure that you have the following prerequisites installed on your machine:

Python (for Python tests)
Node.js (for JavaScript tests)
npm (Node.js package manager)
Installation
Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/DYagmur/Automation-test-for-REST-API
cd api-automation-tests
Install Python dependencies:

bash
Copy code
pip install -r requirements.txt
Install JavaScript dependencies:

bash
Copy code
cd js-tests
npm install
Usage
Python Tests
Run the Python tests using the following command:

bash
Copy code
python test_api.py
JavaScript Tests
Run the JavaScript tests using the following command:

bash
Copy code
cd js-tests
npm test
Project Structure
python-tests: Contains Python scripts for API automation tests.
test_api.py: Main Python test script.
requirements.txt: Dependencies for Python tests.
js-tests: Contains JavaScript scripts for API automation tests.
test_api.js: Main JavaScript test script.
package.json: Configuration file for npm.
package-lock.json: Lock file for npm dependencies.
Contributing
If you would like to contribute to this project, feel free to fork the repository and submit pull requests. Contributions are welcome!

License
This project is licensed under the MIT License.