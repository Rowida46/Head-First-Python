from flask import Flask, jsonify , request , render_template 
from flask_sqlalchemy import SQLAlchemy
"""
DBcm stand for data base context manegar
 
 ch 9 head first python



 

with UseDataBase(app.config['dbconfig']) as cursor:
    """
    The use db class except to recive a dic of database conection.
    Log details of the web request and the results.
    """
    _SQL = """insert into log
                    (phrase, letters, ip, browser_string, results)
                    values
                    (%s, %s, %s, %s, %s)"""
    cursor.execute(_SQL, (req.form['phrase'],
                              req.form['letters'],
                              req.remote_addr,
                              req.user_agent.browser,
                              res, )) 
"""
import mysql.connector
class UseDataBase:
	"""
	We Know that, in order for our class to create a context manger it has to:
		1- provide a __init__ `init dender` to provide and perform initialization 

		2- provide __enter__ `enter dender` to include any setup code 

		3- privide __exit__ `exit dender` to include any tear/shutdown code
	"""
	def __init__(self, config: dict) -> None:
		self.configuration = config
	
	def __enter__(self)-> 'cursor':
        self.conn = mysql.connector.connect(**self.configuration)
        self.cursor = self.conn.cursor()
        return self.cursor

	def __exit__(self, exc_type, exc_value, exc_trace) -> None:
		self.conn.commit()
        self.cursor.close()
        self.conn.close()