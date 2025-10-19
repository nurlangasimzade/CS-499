from pymongo import MongoClient

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password, host, port):
        # The authSource tells MongoDB which database the user's credentials belong to.
        # The 'root' user belongs to the 'admin' database.
        uri = f"mongodb://{username}:{password}@{host}:{port}/?authSource=admin"
        
        # Initialize the MongoClient to access the MongoDB database
        self.client = MongoClient(uri)
        # We can still work with the 'AAC' database after connecting.
        self.database = self.client['AAC']
        self.collection = self.database['animals']
        print("Attempting to connect to the remote database...")
        self.client.admin.command('ping') # Test connection
        print("Connected to MongoDB successfully!")

    # Method to implement the R in CRUD
    def read(self, query: dict):
        return self.collection.find(query)

    # Method for Water Rescue query
    def find_water_rescue(self):
        query = {
            "sex_upon_outcome": "Intact Female",
            "breed": {"$in": ["Labrador Retriever Mix", "Chesapeake Bay Retriever", "Newfoundland"]},
            "age_upon_outcome_in_weeks": {"$gte": 26, "$lte": 156}
        }
        return self.collection.find(query, {"_id": 0})

    # Method for Mountain/Wilderness Rescue query
    def find_mountain_rescue(self):
        query = {
            "sex_upon_outcome": "Intact Male",
            "breed": {"$in": ["German Shepherd", "Alaskan Malamute", "Old English Sheepdog", "Siberian Husky", "Rottweiler"]},
            "age_upon_outcome_in_weeks": {"$gte": 26, "$lte": 156}
        }
        return self.collection.find(query, {"_id": 0})

    # Method for Disaster/Individual Tracking query
    def find_disaster_rescue(self):
        query = {
            "sex_upon_outcome": "Intact Male",
            "breed": {"$in": ["Doberman Pinscher", "German Shepherd", "Golden Retriever", "Bloodhound", "Rottweiler"]},
            "age_upon_outcome_in_weeks": {"$gte": 20, "$lte": 300}
        }
        return self.collection.find(query, {"_id": 0})