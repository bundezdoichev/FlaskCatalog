from application import app
from application.extentions import register_extentions


if __name__ == '__main__':
    register_extentions(app)
    app.run(debug=True, host='0.0.0.0')

