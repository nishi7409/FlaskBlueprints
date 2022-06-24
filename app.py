# from urllib import request
from sys import modules
from flask import Flask
from .modules.ticket import ticket_blueprint

# old code
    # app = Flask(__name__)

    # @app.route("/create/", methods=['POST'])
    # def createTicket():
    #     """
    #     Create a ticket  
    #     """

    #     if request.method == 'POST':
    #         data = request.get_json()

    #         print(data['message'])
    #         return('Poop')
        
    #         return('A request other than a POST results in this error... No ticket has been created!!', status.HTTP_201_CREATED)

def create_app():
    app = Flask(__name__)

    # tickets/incidents
    app.register_blueprint(ticket_blueprint)

    # if we have other purposes for this flask app, then we can prefix each blueprint
    # app.register_blueprint(ticket_blueprint, url_prefix="/ticket")

    return(app)

if __name__ == "__main__":
    app = create_app()
    app.run(host="local", port=80)