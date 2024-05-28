'''
### Day 2: Installing and Setting Up Python

#### Step 1: Download Python

1. **Visit the Official Python Website**:
   - Go to [python.org](https://www.python.org/downloads/).
   - The website should automatically suggest the latest version for your operating system (Windows, macOS, Linux).

2. **Download the Installer**:
   - Click the "Download Python" button to download the installer for your operating system.

#### Step 2: Install Python

1. **Windows Installation**:
   - Run the downloaded installer.
   - Make sure to check the box that says "Add Python to PATH".
   - Choose "Install Now" or customize the installation if needed.
   - Wait for the installation to complete and then close the installer.

2. **macOS Installation**:
   - Open the downloaded `.pkg` file.
   - Follow the prompts to complete the installation.
   - Ensure the installer adds Python to your PATH.

3. **Linux Installation**:
   - Open a terminal.
   - Use a package manager to install Python (this example uses `apt` for Debian-based systems):
     ```sh
     sudo apt update
     sudo apt install python3
     ```

#### Step 3: Verify the Installation

1. **Open Command Line Interface (CLI)**:
   - On Windows, open Command Prompt or PowerShell.
   - On macOS or Linux, open Terminal.

2. **Check Python Version**:
   - Run the following command:
     ```sh
     python --version
     ```
     or, if that doesn’t work,
     ```sh
     python3 --version
     ```
   - You should see output similar to `Python 3.x.x`, indicating that Python is installed correctly.

#### Step 4: Install a Code Editor or Integrated Development Environment (IDE)

1. **Visual Studio Code (VS Code)**:
   - Visit the [VS Code download page](https://code.visualstudio.com/Download) and download the installer for your operating system.
   - Install VS Code by following the prompts.
   - After installation, open VS Code and install the Python extension. You can do this by:
     - Clicking on the Extensions view icon on the Sidebar or pressing `Ctrl+Shift+X`.
     - Searching for "Python" and clicking "Install" for the extension by Microsoft.

2. **Other Editors/IDEs**:
   - **PyCharm**: Download from [JetBrains](https://www.jetbrains.com/pycharm/download/).
   - **Jupyter Notebook**: Install using pip:
     ```sh
     pip install notebook
     ```
   - **Spyder**: Often included with the Anaconda distribution, or install using pip:
     ```sh
     pip install spyder
     ```

#### Step 5: Install Virtual Environment (Optional but Recommended)

1. **Create a Virtual Environment**:
   - Navigate to your project directory in the CLI.
   - Run the following command to create a virtual environment:
     ```sh
     python -m venv myenv
     ```
     Replace `myenv` with your preferred environment name.

2. **Activate the Virtual Environment**:
   - On Windows:
     ```sh
     myenv\Scripts\activate
     ```
   - On macOS and Linux:
     ```sh
     source myenv/bin/activate
     ```

3. **Deactivate the Virtual Environment**:
   - To deactivate the virtual environment, simply run:
     ```sh
     deactivate
     ```

#### Step 6: Install Necessary Packages

1. **Use `pip` to Install Packages**:
   - With the virtual environment activated, you can install packages using `pip`. For example:
     ```sh
     pip install requests numpy pandas
     ```

2. **Freeze Requirements (Optional)**:
   - To save the list of installed packages for future use, run:
     ```sh
     pip freeze > requirements.txt
     ```

3. **Install from Requirements File (Optional)**:
   - To install packages from a `requirements.txt` file, run:
     ```sh
     pip install -r requirements.txt
     ```

#### Step 7: Write and Run a Simple Python Script

1. **Create a Python Script**:
   - Open your code editor and create a new file named `hello.py`.

2. **Write a Simple Python Program**:
   ```python
   print("Hello, World!")
   ```

3. **Run the Python Script**:
   - In the CLI, navigate to the directory containing `hello.py`.
   - Run the script:
     ```sh
     python hello.py
     ```
     or
     ```sh
     python3 hello.py
     ```

Congratulations! You have successfully installed and set up Python. You are now ready to start coding in Python.
'''