from flask import Flask
from flask import render_template

app = Flask(__name__)

# Ruta del index


@app.route('/')
def inicio():
    return render_template('index.html')


# Rutas de los mapas

# 1


@app.route('/ascent')
def ascent():
    return render_template('mapas/ascent/ascent.html')


@app.route('/ascent/sova')
def ascentSova():
    return render_template('mapas/ascent/ascentSova.html')


@app.route('/ascent/viper')
def ascentViper():
    return render_template('mapas/ascent/ascentViper.html')

# 2


@app.route('/fracture')
def fracture():
    return render_template('mapas/fracture/fracture.html')


@app.route('/fracture/sova')
def fractureSova():
    return render_template('mapas/fracture/fractureSova.html')


@app.route('/fracture/viper')
def fractureViper():
    return render_template('mapas/fracture/fractureViper.html')

# 3


@app.route('/haven')
def haven():
    return render_template('mapas/haven/haven.html')


@app.route('/haven/sova')
def havenSova():
    return render_template('mapas/haven/havenSova.html')


@app.route('/haven/viper')
def havenViper():
    return render_template('mapas/haven/havenViper.html')

# 4


@app.route('/icebox')
def icebox():
    return render_template('mapas/icebox/icebox.html')


@app.route('/icebox/sova')
def iceboxSova():
    return render_template('mapas/icebox/iceboxSova.html')


@app.route('/icebox/viper')
def iceboxViper():
    return render_template('mapas/icebox/iceboxViper.html')

# 5


@app.route('/lotus')
def lotus():
    return render_template('mapas/lotus/lotus.html')


@app.route('/lotus/sova')
def lotusSova():
    return render_template('mapas/lotus/lotusSova.html')


@app.route('/lotus/viper')
def lotusViper():
    return render_template('mapas/lotus/lotusViper.html')

# 6


@app.route('/split')
def split():
    return render_template('mapas/split/split.html')


@app.route('/split/sova')
def splitSova():
    return render_template('mapas/split/splitSova.html')


@app.route('/split/viper')
def splitViper():
    return render_template('mapas/split/splitViper.html')

# 7


@app.route('/pearl')
def pearl():
    return render_template('mapas/pearl/pearl.html')


@app.route('/pearl/sova')
def pearlSova():
    return render_template('mapas/pearl/pearlSova.html')


@app.route('/pearl/viper')
def pearlViper():
    return render_template('mapas/pearl/pearlViper.html')


if __name__ == '__main__':
    app.run(debug=True)
