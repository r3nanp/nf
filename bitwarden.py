import json
import subprocess
import os

def unlock_vault(master_password: str):
  """
  Get the vault info from the Bitwarden.
  """
  result = subprocess.run(
    ["bw", "unlock", "--raw"],
    input=master_password.encode(),
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
  )

  if result.returncode != 0:
    raise Exception(f"Failed to unlock vault: {result.stderr.decode()}")

  return result.stdout.decode().strip()

def get_item(session_token: str, item_name: str):
  """
  Get the item from the Bitwarden.
  """
  result = subprocess.run(
    ["bw", "get", "item", item_name],
    env={**dict(**os.environ), "BW_SESSION": session_token},
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
  )

  if result.returncode != 0:
    raise Exception(f"Failed to get password: {result.stderr.decode()}")

  item = result.stdout.decode().strip()
  item_json = json.loads(item)

  item_username = item_json["login"]["username"]
  item_password = item_json["login"]["password"]

  return item_username, item_password
