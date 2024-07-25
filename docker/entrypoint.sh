#!/bin/sh

# Read the PODSLEEP environment variable (default to "no" if not set)
PODSLEEP=${PODSLEEP:-no}

# Check the value of PODSLEEP and act accordingly
if [ "$PODSLEEP" = "yes" ]; then
  echo "[ENTRYPOINT] PODSLEEP is set to yes. Sleeping the container for 9999 days..."
  sleep 9999d
else
  echo "[ENTRYPOINT] PODSLEEP is set to no. Running Flask..."
  python /app/main.py
fi
