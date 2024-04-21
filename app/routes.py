from flask import request, jsonify
from . import app, db
from .models import UserData
from ml_models.nlp_model import summarize_text

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    text = data.get('text')

    summary = summarize_text(text)
    user_data = UserData(user_input=text, model_output=summary)
    db.session.add(user_data)
    db.session.commit()

    return jsonify({'input': text, 'summary': summary})
