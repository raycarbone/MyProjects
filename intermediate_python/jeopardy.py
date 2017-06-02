
import sqlite3

connection = sqlite3.connect("jeopardy.db")

cursor = connection.cursor()

# get a random game
cursor.execute("SELECT game FROM category ORDER BY RANDOM() LIMIT 1")
results = cursor.fetchall()
game_id = results[0][0]
print("Categories for game #%d:" % (game_id,))

# Get the categories for that game.
query = """SELECT name, round FROM category
WHERE game=%d ORDER BY round""" % (game_id,)
cursor.execute(query)
results = cursor.fetchall()

print("Example Categories:\n")
for result in results:
	# round 0 = Jeopardy Round
	# round 1 =  Double Jeopardy
	# round 2 = Final Jeopardy
	name, round  = result

	print("Round %d: %s" % (round, name) )

connection.close()


