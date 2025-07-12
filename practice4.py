from flask import Flask, jsonify, request

# Create a Flask app
app = Flask(__name__)

# Sample data: List of quote dictionaries
quotes = [
    {
        "id": 1,
        "author": "Dozie",
        "quote": "Trust God"
    },
    {
        "id": 2,
        "author": "Mattew",
        "quote": "Always Have Fun"
    }
]

# Route to return all quotes (when you visit /message)
@app.route('/message', methods=['GET'])
def get_quotes():
    return jsonify(quotes)

#route to add a qoute
@app.route('/message',methods=['POST'])
def add_quotes():
    data=request.get_json()
    new_quote={
        "id": len(quotes) + 1,
        "author": data["author"],
        "quote": data["quote"]
    }
    quotes.append(new_quote)
    return jsonify({"message": "Quote added", "quote": new_quote}), 201

#route to delete quote
@app.route('/message/<int:id>',methods=['DELETE'])
def delete_quotes(id):
    for quote in quotes:
        if quote["id"]==id:
            quotes.remove(quote)
            return jsonify({"message": f"the quote with id {id} has been deleted", "remaining qoute":quotes }),201
    return jsonify({"error":"quote not found"}),404

#route to edit qoute using put
@app.route('/message/<int:id>', methods=['PUT'])
def update_quote(id):
    data=request.get_json()
    for quote in quotes:
        if quote["id"]==id:
            quote["author"] = data["author"]
            quote["quote"] = data["quote"]
            return jsonify({"message":"quote updated", "quote":quote}), 200
    return jsonify({"error":"qoute not found"}), 404

#route to edit using patch, just a segment of an item
@app.route('/message/<int:id>', methods=['PATCH'])
def patch_quote(id):
    data = request.get_json()

    for quote in quotes:
        if quote["id"] == id:
            # Only update fields that were provided
            if "author" in data:
                quote["author"] = data["author"]
            if "quote" in data:
                quote["quote"] = data["quote"]
            return jsonify({"message": "Quote updated", "quote": quote}), 200

    return jsonify({"error": "Quote not found"}), 404

# Start the server
if __name__ == '__main__':
    app.run(debug=True)
