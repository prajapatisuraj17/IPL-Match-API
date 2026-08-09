from flask import Flask,jsonify,request
import ipl


app=Flask(__name__)

@app.route('/')
def home():
    return 'home page'

@app.route('/api/teams')
def teams():
    team=ipl.get_teams()
    return jsonify({'team':team})

@app.route('/api/teamvteam')
def team1_vs_team2():
    team1=request.args.get('team1')
    team2=request.args.get('team2')

    result=ipl.team_vs_team(team1,team2)

    return jsonify(result)

@app.route('/api/allrecoed')
def allrecord():
    team=request.args.get('team')

    result=ipl.allRecord(team)

    return jsonify(result)

 


app.run(debug=True)