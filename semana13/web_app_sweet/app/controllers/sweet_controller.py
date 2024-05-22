from flask import Blueprint, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from models.sweet_model import Sweet
from views import sweet_view

# Importamos el decorador de role
from utils.decorators import role_required

sweet_bp = Blueprint("sweet", __name__)


@sweet_bp.route("/sweets")
@login_required
@role_required(role=["admin","user"])
def list_sweets():
   sweets = Sweet.get_all()
   return sweet_view.list_sweets(sweets)


@sweet_bp.route("/sweets/create", methods=["GET", "POST"])
@login_required
@role_required(role=["admin"])
def create_sweet():
   if request.method == "POST":
      if current_user.has_role("admin"):
         brand = request.form["brand"]
         weight = request.form["weight"]
         flavor = request.form["flavor"]
         origin = request.form["origin"]
         sweet = Sweet(brand=brand, weight=weight, flavor=flavor, origin=origin)
         sweet.save()
         flash("Dulce creado exitosamente", "success")
         return redirect(url_for("sweet.list_sweets"))
      else:
         print(current_user)
         return jsonify({"message": "Unauthorized"}), 403
   return sweet_view.create_sweet()


@sweet_bp.route("/sweets/<int:id>/update", methods=["GET", "POST"])
@login_required
@role_required(role=["admin", "user"])
def update_sweet(id):
   sweet = Sweet.get_by_id(id)
   if not sweet:
      return "Dulce no encontrado", 404
   if request.method == "POST":
      if current_user.has_role("admin") or current_user.has_role("user"):
         brand = request.form["brand"]
         weight = request.form["weight"]
         flavor = request.form["flavor"]
         origin = request.form["origin"]
         sweet.update(brand=brand, weight=weight, flavor=flavor, origin=origin)
         flash("Dulce actualizado exitosamente", "success")
         return redirect(url_for("sweet.list_sweets"))
      else:
         return jsonify({"message": "Unauthorized"}), 403
   return sweet_view.update_sweet(sweet)


@sweet_bp.route("/sweets/<int:id>/delete")
@login_required
@role_required(role=["admin", "user"])
def delete_sweet(id):
   sweet = Sweet.get_by_id(id)
   if not sweet:
      return "Dulce no encontrado", 404
   if current_user.has_role("admin") or current_user.has_role("user"):
      sweet.delete()
      flash("Dulce eliminado exitosamente", "success")
      return redirect(url_for("sweet.list_sweets"))
   else:
      return jsonify({"message": "Unauthorized"}), 403