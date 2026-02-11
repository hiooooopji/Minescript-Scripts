import minescript

x, y, z = [int(p) for p in minescript.player().position]

# .as_async(...) causes the script function to return a "future" value:
future = minescript.await_loaded_region.as_async(x - 50, z - 50, x + 50, z + 50)

# Do other work while the chunks are loading in the background...
minescript.echo("Waiting for chunks around player to finish loading...")

# Wait for future to complete, i.e. wait for chunks to finish loading:
future.wait()
minescript.echo("Chunks around player finished loading.")