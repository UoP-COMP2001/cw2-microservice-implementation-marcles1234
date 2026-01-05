from flask import render_template
import config
from models import Users

connex_app = config.connex_app
connex_app.add_api(
    config.basedir / "swagger.yml",
    base_path="/api"
)

app = connex_app.app


@app.route("/")
def home():
    users = Users.query.all()
    return render_template("home.html", users=users)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)


