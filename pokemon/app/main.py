from flask import Flask, render_template, request, url_for
from mongo import get_sample, get_types_combination, get_all_types
app = Flask(__name__)
app.secret_key = 'flask'


@app.route('/', methods=['get', 'post'])
def index():
    all_types = get_all_types()
    samples = get_sample()
    print(request.method)
    if request.method == 'POST':
        ty1 = request.form['type1']
        ty2 = request.form['type2']
        if ty1 == 'nulo' and ty2 == 'nulo':
            return render_template('index.html', all_types=all_types, pokes=samples)
        elif ty2 == 'nulo':
            pokes = get_types_combination(ty1)
        elif ty1 == 'nulo':
            pokes = get_types_combination(ty2)
        else:
            pokes = get_types_combination(ty1, ty2)
        return render_template('index.html', all_types=all_types, pokes=pokes)
    else:
        return render_template('index.html', all_types=all_types, pokes=samples)


app.run(debug=True)