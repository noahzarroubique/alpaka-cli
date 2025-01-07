# Alpaka Installer

### Installation
Create a virtual environment and activate it
```bash
virtualenv venv
source venv/bin/activate
```

Install requirements
```bash
pip install requirements.txt
```

Setup an access token. Create a `token.json` file. Fill in a refresh token. It can be extracted using a proxy when logging in in Alpaka.
```json
{"refresh_token": "asdf"}
```

Create a whitelist of apps that should be installed. Use the file `whitelist.json` for this. Use the app Id found in the `/apps` request. A sample request can be found in `apps.json`. Choose the channel that should be installed, and give it a name (only used for progress indication).
It should be formatted as follows:
```json
{
    "apps": [
        {
            "id": 2,
            "name": "Fluid",
            "channel": "DEVELOP"
        },
        {
            "id": 26,
            "name": "MeteoSwiss",
            "channel": "DEVELOP"
        },
        {
            "id": 36,
            "name": "SBB Main",
            "channel": "DEVELOP"
        },
        {
            "id": 37,
            "name": "SBB Preview",
            "channel": "DEVELOP"
        },
        {
            "id": 39,
            "name": "Swisstopo",
            "channel": "DEVELOP"
        },
        {
            "id": 64,
            "name": "Phoenix",
            "channel": "DEVELOP"
        }
    ]
}
```


### Usage
Run `adbinstall.sh` periodically (e.g. with a cronjob `0 * * * * /home/noah/tools/alpaka-cli/adbinstall.sh`). It will only run once per day and try to install the newest builds in the corresponding channels of all apps in the `whitelist.json` file.

### Troubleshooting
You might have to change `adb.exe` to `adb` in the `main.py` file. Logs are saved to the `log.log` file

There is no error handling