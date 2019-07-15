# Program a GUI in Python (with Tkinter) !
Here is the source code for my video on how to program a graphical user interface application in python using the Tkinter library. The link to the video is here: https://youtu.be/D8-snVfekto

### API Key

This project utilizes the **OpenWeather API** to retrieve live weather data based on the location information supplied by the user. This API requires that callers provide a unique key with every request. Once you've obtained an API key of your own you can create a new file in the top level directory of your repository named `keyfile` and copy your key into it. The application will read your API key from that file instead of it being coded directly into the sources. The keyfile is also listed in the `.gitignore` file so that it will not be tracked by git and uploaded to a public repository accidentally. This helps keep your personal API key secret.

You can find additional API documentation and generate your own key by signing up here: [OpenWeatherMap Weather API](https://openweathermap.org/api).