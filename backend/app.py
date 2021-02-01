from flask import Flask, request, jsonify
from flask_graphql import GraphQLView
from database import init_db
from schema import schema
from flask_cors import CORS
# from model import query, mutation
# from ariadne import graphql_sync
# from ariadne import make_executable_schema, gql
# from ariadne import gql, load_schema_from_path
# from ariadne.constants import PLAYGROUND_HTML


app = Flask(__name__)
CORS(app)
app.debug = True

query = '''
query {
  users 
  {
    id,
    email,
    password
  }
}'''.strip()
#result = schema.execute(query)
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))


# We'll create this schema soon
# type_defs = gql(load_schema_from_path("./schema.graphql"))

# schema = make_executable_schema(type_defs, query)



# @app.route("/graphql", methods=["GET"])
# def graphql_playground():
#     return PLAYGROUND_HTML, 200


# @app.route("/graphql", methods=["POST"])
# def graphql_server():
#     data = request.get_json()
#     success, result = graphql_sync(
#         schema,
#         data,
#         context_value=request,
#         debug=app.debug
#     )
#     status_code = 200 if success else 400
#     return jsonify(result), status_code


if __name__ == '__main__':
  #init_db()
  app.run(debug=True)

# @app.route('/')
# def hello():
#   return 'Hello'
