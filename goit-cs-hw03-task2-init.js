use test

db.createCollection( "cats" ,
    {
   validator: {
      $jsonSchema: {
         bsonType: "object",
         required: [ "name", "age" ],
         properties: {
            name: {
               bsonType: "string",
               description: "'name' must be a string and is required"
            },
            age: {
               bsonType: "int",
            },
            features: {
               bsonType: "array"
            }
         }
      }
   }
} )

db.cats.insertOne({
    "_id": ObjectId("60d24b783733b1ae668d4a77"),
    "name": "barsik",
    "age": 3,
    "features": ["ходить в капці", "дає себе гладити", "рудий"]
})

db.cats.find()