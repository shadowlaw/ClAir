from app import create_app
from Config import Config

conf = Config()
app = create_app(conf)

if __name__ == "__main__":
    if conf.ENV.lower() == "development":
        app.run(host="127.0.0.1", debug=True, port=8080)
    else:
        app.run(host="0.0.0.0", port=80)
