from system.core.controller import *
import random


class Welcome(Controller):
	def __init__(self, action):
		super(Welcome, self).__init__(action)

	def index(self):
		if 'gold' in session:
			pass
		else:
			print 'here'
			session['gold'] = 0	
			session['activities'] = []
		if 'activities' not in session:
			session['activities'] = []	
		reverse_list = reversed(session['activities'])
		return self.load_view('index.html', activities=reverse_list)

	def process_money(self):
		if request.form['building'] == 'farm':
			gold_count = random.randrange(10,20)
			session['gold'] += gold_count
			session['activities'] += ["<p>You won %s</p>" % str(gold_count)]
		elif request.form['building'] == 'cave':
			gold_count = random.randrange(5,10)
			session['gold'] += gold_count
			session['activities'] += ["<p>You won %s</p>" % str(gold_count)] 
		elif request.form['building'] == 'house':
			gold_count = random.randrange(5,10)
			session['gold'] += gold_count	
			session['activities'] += ["<p>You won %s</p>" % str(gold_count)]
		elif request.form['building'] == 'casino':
			luck = random.randrange(1,10)
			gold_count = random.randrange(0,50)
			if luck > 7: 
				session['gold'] += gold_count
				session['activities'] += ["<p>You won %s</p>" % str(gold_count)]
			else:	
				session['gold'] -= gold_count	
				session['activities'] += ["<p>You lost %s</p>" % str(gold_count)] 
		return redirect('/')

	def reset(self):
		session.clear()
		return redirect('/')
	