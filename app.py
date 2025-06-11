from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

artworks = [
    {
        "image_url": "https://iiif.micr.io/hZepb/98,71,5737,4761/%5E1024,/0/default.webp",
        "text": "this is a cool swan",
        "source": "Rijksmuseum",
        "more_info_url": "https://www.rijksmuseum.nl/nl/collectie/object/De-bedreigde-zwaan--22040f90565e730131983a44a85b989f?tab=data"
    },
    {
        "image_url": "https://iiif.micr.io/hZepb/98,71,5737,4761/%5E1024,/0/default.webp",
        "text": "this is a cool swan",
        "source": "Rijksmuseum",
        "more_info_url": "https://www.rijksmuseum.nl/nl/collectie/object/De-bedreigde-zwaan--22040f90565e730131983a44a85b989f?tab=data"
    },
    {
        "image_url": "https://iiif.micr.io/hZepb/98,71,5737,4761/%5E1024,/0/default.webp",
        "text": "this is a cool swan",
        "source": "Rijksmuseum",
        "more_info_url": "https://www.rijksmuseum.nl/nl/collectie/object/De-bedreigde-zwaan--22040f90565e730131983a44a85b989f?tab=data"
    }
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    # Simulate analysis — return artworks for demo
    return jsonify({"artworks": artworks})

if __name__ == "__main__":
    app.run(debug=True)
