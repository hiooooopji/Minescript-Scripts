# @param: speed | type: float | default: 1.0 | min: 0.1 | max: 5.0
# @param: count | type: int | default: 10 | min: 1 | max: 100
# @param: debug_mode | type: bool | default: False
# @param: mode | type: list | options: ["Fast", "Safe", "Precision"] | default: "Safe"
# @param: username | type: str | default: "Player"

import json
import os
import sys
import minescript as m
# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
script_name = os.path.splitext(os.path.basename(__file__))[0]
config_path = os.path.join(script_dir, f"{script_name}_config.json")

# Print header
m.echo("=" * 40)
m.echo("METADATA TEST SCRIPT")
m.echo("=" * 40)

# Read and display the config
m.echo(f"Looking for config at: {config_path}")

if os.path.exists(config_path):
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    m.echo("")
    m.echo("CONFIG VALUES RECEIVED:")
    m.echo("-" * 30)
    
    # Display each parameter with its type
    for key, value in config.items():
        value_type = type(value).__name__
        m.echo(f"  {key}: {value} ({value_type})")
    
    m.echo("")
    m.echo("Testing parameter usage:")
    
    # Test using the values
    speed = config.get('speed', 1.0)
    count = config.get('count', 10)
    debug_mode = config.get('debug_mode', False)
    mode = config.get('mode', 'Safe')
    username = config.get('username', 'Player')
    
    m.echo(f"  Speed * 2 = {speed * 2}")
    m.echo(f"  Count + 5 = {count + 5}")
    m.echo(f"  Debug enabled: {debug_mode}")
    m.echo(f"  Selected mode: {mode}")
    m.echo(f"  Hello, {username}!")
    
    m.echo("")
    m.echo("METADATA TEST: SUCCESS!")
else:
    m.echo("ERROR: Config file not found!")
    m.echo("Make sure to run this script through the launcher UI.")
    m.echo("The launcher writes the config before executing.")

m.echo("=" * 40)
