import requests
import matplotlib.pyplot as plt
import seaborn as sns

# Replace with your OpenWeatherMap API key
API_KEY = 'e9f467466020c05d18d6e65d5ffd6610'
CITY = 'Mumbai'
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# Fetch data from API
response = requests.get(URL)
data = response.json()

# Check if city found
if data["cod"] != "200":
    print("City not found or API error")
    exit()

# Extract temperature and date info
dates = []
temps = []

for entry in data['list']:
    dates.append(entry['dt_txt'])
    temps.append(entry['main']['temp'])

# Visualization using Seaborn
plt.figure(figsize=(12, 6))
sns.lineplot(x=dates, y=temps, marker='o', color='blue')
plt.xticks(rotation=45)
plt.title(f'Temperature Forecast for {CITY}')
plt.xlabel('Date & Time')
plt.ylabel('Temperature (°C)')
plt.tight_layout()
plt.show()
