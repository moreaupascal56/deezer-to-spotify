import json
import logging
import os
import webbrowser
from time import sleep

import deezer
from deezer_oauth.client import OAuthDancer
from deezer_oauth.server import run_server
from dotenv import load_dotenv


def main():
    logging.info("Loads .env variables")
    load_dotenv()

    logging.info("Get the deezer token")
    get_deezer_token()
    sleep(3)

    logging.info("Reloads .env variables")
    load_dotenv()

    logging.info("Get the user loved resources")
    loved_resources = get_loved_resources_as_json()

    logging.info("Save the loved resources to a json file")
    load_dict_to_file(loved_resources)


def get_deezer_token():
    """
    Opens a browser to get the Deezer token using OAuth and loads the token in the
    API_TOKEN environment variable
    """
    oauth_dancer = OAuthDancer(
        app_id=os.getenv("SOCIAL_AUTH_DEEZER_KEY"),
        app_secret=os.getenv("SOCIAL_AUTH_DEEZER_SECRET"),
    )
    start_url = oauth_dancer.get_auth_page()
    print(f"Opening {start_url} in web browser...")
    webbrowser.open(start_url)
    run_server(oauth_dancer)


def get_loved_resources_as_json():
    """
    Get loved Deezer resources of the user.
    :return: A dict containing data about loved resources of the user on Deezer
    """
    client = deezer.Client(
        app_id=os.getenv("SOCIAL_AUTH_DEEZER_KEY"),
        app_secret=os.getenv("SOCIAL_AUTH_DEEZER_SECRET"),
        access_token=os.getenv("API_TOKEN"),
    )

    user_deezer_data = {
        "loved_tracks": client.get_user_tracks(),
        "loved_albums": client.get_user_albums(),
        "loved_artists": client.get_user_artists(),
        "history": client.get_user_history(),
    }

    backup = dict()

    for resource_type, resources in user_deezer_data.items():
        backup[resource_type] = [resource.as_dict() for resource in resources]

    return backup


def load_dict_to_file(d: dict, filename="backup_deezer.json"):
    """
    Loads a dict to a file
    :param backup: backup dictionary
    :param filename: the filename
    """
    with open(filename, "w") as file:
        json.dump(d, file)


if __name__ == "__main__":
    main()
