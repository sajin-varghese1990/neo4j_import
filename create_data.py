from connect_driver import HelloWorldExample

import json
import os

with open(os.path.join('config', 'config.json'), 'r') as f:
    config = json.load(f)


uri = config["DB"]["URI"]


user = config["DB"]["USER"]
password = config["DB"]["PASSWORD"]
remote_path = config["REMOTE"]["PATH"]

connectObj = HelloWorldExample(uri, user, password)

connectObj.load_data_csv(remote_path)

