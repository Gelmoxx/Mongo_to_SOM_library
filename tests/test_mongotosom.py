from mongo_to_som import mongotosom

def test_mongo_to_som():
    assert mongotosom.mongo_to_som(10,10, int(1*10e3), 4, 0.5, 'localhost', 27017, "som_db", "som_data")