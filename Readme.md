# Deezer To Spotify

I did this to move my loved resources from deezer to spotify, it succeed but I am working again on this to make a clean and reusable version, so this is a work in progress. The readme is there for anyone that wants to use what is already done!

For now it takes your data from deezer and download them into a JSON file. 

## Usage

Get your SOCIAL_AUTH_DEEZER_KEY and SOCIAL_AUTH_DEEZER_SECRET from Deezer developers website ([https://developers.deezer.com/myapps](https://developers.deezer.com/myapps)), you will need to create a Deezer App.

![Gimp skills are bad... sorry](./img/deezer_dev_app.png?raw=true "Deezer Developer App")


Use poetry to install dependencies.

Run a first time the script to get your API_TOKEN, it will open a web browser with the token. The token should get copied to your `.env` file and then download your deezer loved resources to the `backup_deezer.json` file.