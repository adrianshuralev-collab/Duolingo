from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Разрешаем запросы с фронтенда

# Наша импровизированная "база данных"
ROADMAP_DATA = [
    {
        "section_id": 1,
        "title": "Раздел 1: Small Talk",
        "is_active": True,
        "lessons": [
            {"id": 1, "status": "completed", "icon": "⭐", "is_boss": False},
            {"id": 2, "status": "completed", "icon": "⭐", "is_boss": False},
            {"id": 3, "status": "current", "icon": "👔", "is_boss": False},
            {"id": 4, "status": "locked", "icon": "🔒", "is_boss": False},
            {"id": 5, "status": "locked", "icon": "👑", "is_boss": True}
        ]
    },
    {
        "section_id": 2,
        "title": "Раздел 2: Холодные звонки",
        "is_active": False, # Раздел заблокирован
        "lessons": [
            {"id": 6, "status": "locked", "icon": "🔒", "is_boss": False},
            {"id": 7, "status": "locked", "icon": "🔒", "is_boss": False},
            {"id": 8, "status": "locked", "icon": "👑", "is_boss": True}
        ]
    },
    {
        "section_id": 1,
        "title": "Раздел 1: Small Talk",
        "is_active": True,
        "lessons": [
            {"id": 1, "status": "completed", "icon": "⭐", "is_boss": False, "url": "small-talk1.html"},
            {"id": 2, "status": "completed", "icon": "⭐", "is_boss": False, "url": "lesson.html?id=2"},
            # ... и так далее
        ]
    }
]

]

@app.route('/api/roadmap', methods=['GET'])
def get_roadmap():
    # Отдаем данные в формате JSON
    return jsonify(ROADMAP_DATA)

if __name__ == '__main__':
    print("Сервер запущен на http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
    
