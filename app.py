from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash
from flask import session

from sqlalchemy import func
from models import db, Gasto, Auditoria
from datetime import datetime

app = Flask(__name__)

app.config["SECRET_KEY"] = "gastos-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///gastos.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()


# -----------------------
# LOGIN
# -----------------------

@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        usuario = request.form["usuario"]
        clave = request.form["clave"]

        if usuario == "admin" and clave == "123":

            session["usuario"] = usuario

            return redirect(
                url_for("dashboard")
            )

        flash("Credenciales incorrectas")

    return render_template("login.html")


# -----------------------
# DASHBOARD
# -----------------------

@app.route("/dashboard")
def dashboard():

    if "usuario" not in session:
        return redirect(url_for("login"))

    total_gastos = Gasto.query.count()

    suma_total = db.session.query(
        func.sum(Gasto.monto)
    ).scalar()

    if suma_total is None:
        suma_total = 0

    return render_template(
        "dashboard.html",
        total_gastos=total_gastos,
        suma_total=suma_total
    )


# -----------------------
# NUEVO GASTO
# -----------------------

@app.route("/nuevo", methods=["GET", "POST"])
def nuevo_gasto():

    if "usuario" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":

        gasto = Gasto(
            fecha=request.form["fecha"],
            descripcion=request.form["descripcion"],
            monto=float(
                request.form["monto"]
            )
        )

        db.session.add(gasto)
        
        auditoria = Auditoria(
            fecha_hora=datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            usuario=session["usuario"],
            accion="REGISTRO",
            detalle=f"Se registró el gasto: {gasto.descripcion}"
        )

        db.session.add(auditoria)
        
        db.session.commit()

        flash("Gasto registrado")

        return redirect(
            url_for("reporte")
        )

    return render_template(
        "nuevo_gasto.html"
    )

##
# EDICION
##

@app.route("/editar/<int:id>",
           methods=["GET", "POST"])
def editar_gasto(id):

    if "usuario" not in session:
        return redirect(url_for("login"))

    gasto = Gasto.query.get_or_404(id)

    if request.method == "POST":

        descripcion_anterior = gasto.descripcion

        gasto.fecha = request.form["fecha"]
        gasto.descripcion = request.form["descripcion"]
        gasto.monto = float(
            request.form["monto"]
        )

        auditoria = Auditoria(
            fecha_hora=datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            usuario=session["usuario"],
            accion="EDICION",
            detalle=(
                f"Se editó el gasto "
                f"{descripcion_anterior}"
            )
        )

        db.session.add(auditoria)

        db.session.commit()

        flash("Gasto actualizado")

        return redirect(
            url_for("reporte")
        )

    return render_template(
        "editar_gasto.html",
        gasto=gasto
    )
    
#
# REPORTE DE AUDITORIA
#

@app.route("/auditoria")
def auditoria():

    if "usuario" not in session:
        return redirect(url_for("login"))

    registros = Auditoria.query.order_by(
        Auditoria.id.desc()
    ).all()

    return render_template(
        "auditoria.html",
        registros=registros
    )

# -----------------------
# REPORTE
# -----------------------

@app.route("/reporte")
def reporte():

    if "usuario" not in session:
        return redirect(url_for("login"))

    gastos = Gasto.query.all()

    total = db.session.query(
        func.sum(Gasto.monto)
    ).scalar()

    if total is None:
        total = 0

    return render_template(
        "reporte.html",
        gastos=gastos,
        total=total
    )


# -----------------------
# LOGOUT
# -----------------------

@app.route("/logout")
def logout():

    session.clear()

    return redirect(
        url_for("login")
    )


if __name__ == "__main__":
    app.run(debug=True)