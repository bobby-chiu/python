#Filename:dictionary.py 


class person:

	def __init__(self,persontuple):
		self.name = persontuple[0]		#name
		self.address = persontuple[1]	#address
		self.group = persontuple[2]		#group


	def __str__(self):
		info = 'Name:"%s" Address:"%s" Group:"%s"\n'\
				% (self.name,self.address,self.group)
		return info

	def add_person(self,lst):
		if lst.has_key(self.name) == 1:
			print 'warning:this person has been in the addressBook'
			return False	
		else:
			lst[self.name] = [self.address,self.group]


	def update_person(self,lst):
		if lst.has_key(self.name) == 0:
			print 'warning:addressBook has no this person'
			return False	
		else:
			lst[self.name] = [self.address,self.group]

	def delete_person(self,lst):
		if lst.has_key(self.name) == 0:
			print 'warning:addressBook has no this person'
			return False	
		else:
			del lst[self.name]

	def search_person(self,lst):
		if lst.has_key(self.name) == 0:
			print 'warning:addressBook has no this person'
			return False
		else:
			return lst[self.name]





