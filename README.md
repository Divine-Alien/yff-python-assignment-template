## How to Run the Program

To run this program, follow these steps:

1. Create a `.env` file in the project's root directory.

2. Create an OpenWeather account and generate an API key:  
   https://home.openweathermap.org/api_keys

3. Add your API key to the `.env` file:
   API_KEY=xxxxxxxxxxxxxxxx

4. Activate the virtual environment by running the appropriate command from the project's root directory:

   **Windows (PowerShell):**
   powershell
   .\venv\Scripts\Activate.ps1
   
   **macOS/Linux:**
   bash
   source venv/bin/activate
   
5. Start the program:
   bash
   python src/main.py