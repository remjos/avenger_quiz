import os
import jinja2
from website import create_app


from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
