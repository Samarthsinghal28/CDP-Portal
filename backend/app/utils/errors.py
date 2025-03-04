# app/utils/errors.py
from flask import jsonify

def register_error_handlers(app):
    @app.errorhandler(400)
    def bad_request(e):
        return jsonify({"error": "Bad Request", "message": str(e)}), 400
    
    @app.errorhandler(401)
    def unauthorized(e):
        return jsonify({"error": "Unauthorized", "message": "Authentication required"}), 401
    
    @app.errorhandler(403)
    def forbidden(e):
        return jsonify({"error": "Forbidden", "message": "You don't have permission to access this resource"}), 403
    
    @app.errorhandler(404)
    def not_found(e):
        return jsonify({"error": "Not Found", "message": "The requested resource was not found"}), 404
    
    @app.errorhandler(500)
    def internal_server_error(e):
        return jsonify({"error": "Internal Server Error", "message": "An unexpected error occurred"}), 500
