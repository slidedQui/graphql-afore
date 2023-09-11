from db.db import catprefijos,Base,engine


print("Creating database......")


Base.metadata.create_all(bind=engine)
