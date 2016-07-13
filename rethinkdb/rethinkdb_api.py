import rethinkdb as r
r.connect('localhost', 28015).repl()
# r.db('test').table_create('tv_shows').run()
# r.table('tv_shows').insert({ 'name': 'Star Trek TNG' }).run()

def insert_entries():
    r.db("test").table_create("authors").run()
    entries = r.table("authors").insert([
        { "name": "William Adama", "tv_show": "Battlestar Galactica",
          "posts": [
            {"title": "Decommissioning speech", "content": "The Cylon War is long over..."},
            {"title": "We are at war", "content": "Moments ago, this ship received..."},
            {"title": "The new Earth", "content": "The discoveries of the past few days..."}
          ]
        },
        { "name": "Laura Roslin", "tv_show": "Battlestar Galactica",
          "posts": [
            {"title": "The oath of office", "content": "I, Laura Roslin, ..."},
            {"title": "They look like us", "content": "The Cylons have the ability..."}
          ]
        },
        { "name": "Jean-Luc Picard", "tv_show": "Star Trek TNG",
          "posts": [
            {"title": "Civil rights", "content": "There are some words I've known since..."}
          ]
        }
    ]).run()

def fetch_entries():
    cursor = r.table("authors").run()
    for document in cursor:
        print(document)

    cursor = r.table("authors").filter(r.row["name"] == "William Adama").run()
    for document in cursor:
        print(document)

    print "\nFiltered Results\n"
    cursor = r.table("authors").filter(r.row["posts"].count() > 2).run()
    for document in cursor:
        print document

    # print "\nGet Specific Element\n"
    # print r.db("test").table("authors").get('5cea63dd-555c-4c5c-a18c-2b546ff623f0').run()

    # print "\nUpdate Elements\n"
    # r.table("authors").update({"type": "fictional"}).run()
    # r.table("authors").filter(r.row['name'] == "William Adama").update({"rank": "Admiral"}).run()
    # r.table("authors").filter(r.row["name"] == "Jean-Luc Picard").update(r.row["posts"].append([
    #     {"title": "Shakespeare",
    #     "content": "What a piece of work is man..."},
    #     {"title": "New Top Gear",
    #     "content": "What a piece of shit, man!"}
    # ])).run()

    r.table("authors").filter(r.row["name"] == "William Adama").update({"rank":"Major"}).run()

    print "\nGet Specific Element\n"
    x = r.table("authors").filter(r.row["name"] == "William Adama").run()
    for document in x:
        print document



def track_changes():
    print "\nTrack Changed Elements\n"
    cursor = r.table("authors").changes().run()
    for document in cursor:
        print(document)


if __name__ == "__main__":
    fetch_entries()