from flask import Flask, request, abort, render_template, send_from_directory
from functions.getFilteredUser import get_filtered_user

app = Flask(__name__)


@app.route('/get-filtered-user', methods=['GET', 'POST'])
def local_api():
    return get_filtered_user(request)


if __name__ == '__main__':
    app.run()
