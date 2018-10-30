#! env sh

ARGS="$@"
if [ $# -eq 0 ]; then
    echo "Usage: pushover_exec <command>"
else
    "$@" | tee /dev/tty | pushover -t "$ARGS";
fi
