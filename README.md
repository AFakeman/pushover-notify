# pushover-notify - A tool to get push notified from shell

## Usage

The package provides two commands: pushover and pushover\_exec

### Configuration

Configuration file should be placed in `${XDG_CONFIG_HOME}/pushover.json`.
Currently there are only two settings:

    apiKey - the pushover api key
    defaultClient (optional) - the default client to send notifications to

Note that if the client is not provided to the pushover command the script will
not work.

### pushover

Usage:

    pushover -t <title> -m <message> -c <client>

Sends a push notification with `<message>`, `<title>` to the `<client>`.
Client and title are optional.


### pushover\_exec

Usage:

    pushover_exec some_command

Executes `some_command`, piping its output to both stdout and notifications to
the `defaultClient`
