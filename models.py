from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Gasto(db.Model):
    """
    Tabla donde se almacenan los gastos registrados.
    """

    __tablename__ = "gastos"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    fecha = db.Column(
        db.String(20),
        nullable=False
    )

    descripcion = db.Column(
        db.String(200),
        nullable=False
    )

    monto = db.Column(
        db.Float,
        nullable=False
    )
    
class Auditoria(db.Model):
    """
    Registro de acciones realizadas
    por los usuarios del sistema.
    """

    __tablename__ = "auditoria"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    fecha_hora = db.Column(
        db.String(50),
        nullable=False
    )

    usuario = db.Column(
        db.String(50),
        nullable=False
    )

    accion = db.Column(
        db.String(100),
        nullable=False
    )

    detalle = db.Column(
        db.String(300),
        nullable=False
    )